import { faCheck } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";

interface IProps {
  title: string;
  duration: number;
  description: string;
  slug: string;
  complete?: boolean;
}

export default function Card(props: IProps) {
  return (
    <div className="bg-black p-4 rounded-lg shadow-2xl shadow-violet-950 relative z-0">
      <Link href={props.slug}>
        {props.complete && (
          <div className="absolute top-4 right-4">
            <div className="rounded-full bg-green-500 w-5 h-5 relative">
              <FontAwesomeIcon
                icon={faCheck}
                className="fas fa-check absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{ color: "white", fontSize: 12 }}
              />
            </div>
          </div>
        )}
        <div className="flex gap-4">
          <span className="font-bold">{props.title}</span>
          <span className="font-extralight">
            {props.duration}{" "}
            {props.duration === 1
              ? "minuta"
              : props.duration < 5
                ? "minuty"
                : "minut"}
          </span>
        </div>
        <p className="mt-2">{props.description}</p>
      </Link>
    </div>
  );
}
