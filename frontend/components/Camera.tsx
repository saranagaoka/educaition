"use client";

import { useState } from "react";
import Button from "./Button";

interface Img {
  src: any;
  uuid: string;
}

export default function Camera() {
  const [images, setImages] = useState<Img[]>([]);
  const [image, setImage] = useState<Img | null>(null);

  const sendImages = () => {
    console.log(JSON.stringify({ uuids: images.map((i) => i.uuid) }));
    fetch(`${process.env.NEXT_API_URL}/notes/create/`, {
      method: "POST",
      headers: new Headers({
        Accept: "application/json",
        "Content-Type": "application/json",
      }),
      body: JSON.stringify({ uuids: images.map((i) => i.uuid) }),
    })
      .then((resp) => resp.json())
      .then(() => setImages([]));
  };

  const getUUID = (img: any) => {
    if (!img) return;
    var data = new FormData();
    data.append("file", img);
    data.append("user", "hubot");

    fetch(`${process.env.NEXT_API_URL}/file/upload/`, {
      method: "POST",
      headers: new Headers(),
      body: data,
    })
      .then((resp) => resp.json())
      .then((r) => {
        // setImage({ src: img, uuid: r.uuid }))
        let reader = new FileReader();
        reader.onload = function (ev) {
          setImage({ src: ev.target?.result, uuid: r.uuid });
        };
        reader.readAsDataURL(img);
      });
  };

  return (
    <div className="min-h-svh">
      <div>
        {image?.src ? (
          <>
            <img
              src={image.src}
              className="w-full relative rounded-xl overflow-hidden mb-4"
              alt="Taken photo"
            />
            <div className="flex gap-4">
              <Button
                onClick={() => {
                  setImages((prev) => [...prev, image]);
                  setImage(null);
                }}
                text="Wybierz"
              />
              <Button
                onClick={() => setImage(null)}
                text="Odrzuć"
                variant="secondary"
              />
            </div>
          </>
        ) : (
          <>
            <div className="[&>div]:w-full [&>div]:h-[calc(100vh_-_200px)] [&>div]:relative [&>div]:rounded-xl [&>div]:overflow-hidden mb-4">
              <label>
                <input
                  id="myFileInput"
                  type="file"
                  accept="image/*"
                  capture="camera"
                  className="hidden"
                  onChange={(e) =>
                    e.target.files?.[0] && getUUID(e.target.files?.[0])
                  }
                />
                <div className="w-full p-3 text-center rounded-lg font-semibold bg-indigo-700">
                  Zrób zdjęcie
                </div>
              </label>
            </div>
          </>
        )}
        <div className="grid grid-cols-3 gap-4 mt-4 mb-10">
          {images.map((i, idx) => (
            <div key={`${i.uuid}-${idx}`}>
              <img src={i.src} alt="Taken photo" />
            </div>
          ))}
        </div>
        <div className="flex flex-col gap-4">
          {images.length > 0 && (
            <>
              <Button onClick={sendImages} text="Wyślij" />
              <Button
                text="Usuń wszystkie"
                onClick={() => setImages([])}
                variant="secondary"
              />
            </>
          )}
        </div>
      </div>
    </div>
  );
}

// <ReactCamera
//   ref={camera}
//   facingMode="environment"
//   errorMessages={{ canvas: "" }}
// />
