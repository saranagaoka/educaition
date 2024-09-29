import { faCheck } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";

const className = "w-full p-3 text-center rounded-lg font-semibold relative";

export default function Button({
  text,
  variant = "primary",
  onClick,
  href,
  done,
}: {
  text: string;
  variant?: "primary" | "secondary" | "alt";
  onClick?: () => void;
  href?: string;
  done?: boolean;
}) {
  return onClick ? (
    <button
      type="button"
      onClick={onClick}
      className={`${className} ${variant === "secondary" ? "border-4 border-purple-700 box-border" : variant === "alt" ? "bg-indigo-700" : "bg-purple-700"}`}
    >
      {done && (
        <div className="absolute top-1/2 right-2 -translate-x-1/2 -translate-y-1/2">
          <div className="rounded-full bg-green-500 w-5 h-5 relative">
            <FontAwesomeIcon
              icon={faCheck}
              className="fas fa-check absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
              style={{ color: "white", fontSize: 12 }}
            />
          </div>
        </div>
      )}
      {text}
    </button>
  ) : (
    <Link
      className={`${className} ${variant === "secondary" ? "border-4 border-purple-700 box-border" : variant === "alt" ? "bg-indigo-700" : "bg-purple-700"}`}
      href={href || ""}
    >
      {done && (
        <div className="absolute top-1/2 right-2 -translate-x-1/2 -translate-y-1/2">
          <div className="rounded-full bg-green-500 w-5 h-5 relative">
            <FontAwesomeIcon
              icon={faCheck}
              className="fas fa-check absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
              style={{ color: "white", fontSize: 12 }}
            />
          </div>
        </div>
      )}
      {text}
    </Link>
  );
}
