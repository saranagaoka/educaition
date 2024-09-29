import Camera from "@/components/Camera";
import { faArrowLeftLong } from "@fortawesome/free-solid-svg-icons/faArrowLeftLong";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";

export default function Add() {
  return (
    <div>
      <h1 className="text-2xl mb-2">
        <Link href="/">
          <FontAwesomeIcon
            icon={faArrowLeftLong}
            className="mr-4"
            style={{ color: "white", fontSize: 24 }}
          />
        </Link>
        Dodaj nową notatkę
      </h1>
      <Camera />
    </div>
  );
}
