import Button from "@/components/Button";
import Card from "@/components/Card";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck } from "@fortawesome/free-solid-svg-icons";
import Link from "next/link";
import { faArrowLeftLong } from "@fortawesome/free-solid-svg-icons/faArrowLeftLong";

export default async function Recent() {
  const r = await fetch(`${process.env.NEXT_API_URL}/notes/`);
  const response = await r.json();

  console.log(response);

  return (
    <div className="min-h-svh">
      <h1 className="text-2xl mb-2">
        <Link href={"/"}>
          <FontAwesomeIcon
            icon={faArrowLeftLong}
            className="mr-4"
            style={{ color: "white", fontSize: 24 }}
          />
        </Link>
        Poprzednie notatki
      </h1>
      <div className="flex items-center gap-4">
        <p className="font-extralight">
          Tutaj znajdziesz swoje poprzednie notatki oraz postęp nauki.
        </p>
      </div>
      <div className="my-4 flex flex-col gap-4">
        {response.map((i: any) => (
          <Card
            description={i.first_question}
            slug={`/note/${i.id}`}
            duration={i.duration}
            title={i.subject}
          />
        ))}
      </div>
      <div className="flex flex-col gap-2 mt-16">
        <Button text="Dodaj nowy" href="add" />
      </div>
    </div>
  );
}
