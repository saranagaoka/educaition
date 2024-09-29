"use client";

import { faPlay } from "@fortawesome/free-solid-svg-icons";
import { faBackward } from "@fortawesome/free-solid-svg-icons/faBackward";
import { faForward } from "@fortawesome/free-solid-svg-icons/faForward";
import { faPause } from "@fortawesome/free-solid-svg-icons/faPause";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useEffect, useState } from "react";

export default function AudioPlayer({ audioPath }: { audioPath: string }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [duration, setDuration] = useState(0);
  const [audio, setAudio] = useState(
    new Audio(`${process.env.NEXT_API_BASE_URL}${audioPath}`),
  );

  const togglePlay = () => {
    isPlaying ? audio.pause() : audio.play();
    setIsPlaying((prev) => !prev);
  };

  useEffect(() => {
    let interval: any;

    if (isPlaying) {
      interval = setInterval(() => {
        const duration =
          (audio.duration - (audio.duration - audio.currentTime)) /
          audio.duration;
        setDuration(duration);

        if (duration === 1) {
          audio.pause();
          audio.currentTime = 0;
          setIsPlaying(false);
        }
      }, 300);
    }

    return () => clearInterval(interval);
  }, [isPlaying]);

  return (
    <div className="mt-2">
      <div className="flex justify-evenly py-10">
        <button onClick={() => (audio.currentTime -= 1)}>
          <FontAwesomeIcon
            icon={faBackward}
            style={{ color: "white", fontSize: 24 }}
          />
        </button>
        <button onClick={togglePlay}>
          <FontAwesomeIcon
            icon={isPlaying ? faPause : faPlay}
            style={{ color: "white", fontSize: 36 }}
          />
        </button>
        <button onClick={() => (audio.currentTime += 1)}>
          <FontAwesomeIcon
            icon={faForward}
            style={{ color: "white", fontSize: 24 }}
          />
        </button>
      </div>
      <div className="w-full h-1 bg-gray-700">
        <div
          className={`h-full bg-purple-500`}
          style={{ width: `${duration * 100}%`, transition: "300ms linear" }}
        />
      </div>
      <p className="text-center mt-1 font-extralight">
        {Math.floor(Math.floor(duration * audio.duration || 0) / 60)}:
        {Math.floor((duration * audio.duration || 0) % 60)
          .toString()
          .padStart(2, "0")}{" "}
        / {Math.floor(Math.floor(audio.duration || 0) / 60)}:
        {Math.floor((audio.duration || 0) % 60)
          .toString()
          .padStart(2, "0")}
      </p>
    </div>
  );
}
