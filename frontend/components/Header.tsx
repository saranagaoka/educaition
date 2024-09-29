import { faArrowLeftLong } from "@fortawesome/free-solid-svg-icons/faArrowLeftLong";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";

interface IProps {
  title: string;
  subtitle: string;
  isRead: boolean;
  isQuizDone: boolean;
  href?: string;
}

const Done = () => <div className="w-4 h-4 rounded-full bg-green-500" />;
const Separator = ({ done }: { done?: boolean }) => (
  <div
    className={`w-3 h-1 rounded-full ${done ? "bg-green-500" : "bg-white"}`}
  />
);
const NotDone = () => (
  <div className="w-4 h-4 rounded-full border-2 border-white" />
);

export default function Header(props: IProps) {
  return (
    <header>
      <div className="flex items-center justify-between">
        <h1 className="text-2xl">
          <Link href={props.href || "/"}>
            <FontAwesomeIcon
              icon={faArrowLeftLong}
              className="mr-4"
              style={{ color: "white", fontSize: 24 }}
            />
          </Link>
          {props.title}
        </h1>
        <div className="flex gap-1 items-center">
          <Done />
          {props.isRead ? (
            <>
              <Separator done />
              <Done />
            </>
          ) : (
            <>
              <Separator />
              <NotDone />
            </>
          )}
          {props.isQuizDone ? (
            <>
              <Separator done />
              <Done />
            </>
          ) : (
            <>
              <Separator />
              <NotDone />
            </>
          )}
        </div>
      </div>
      <p className="font-extralight">{props.subtitle}</p>
    </header>
  );
}
