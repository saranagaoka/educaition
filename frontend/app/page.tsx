import Button from "@/components/Button";
import Card from "@/components/Card";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck } from "@fortawesome/free-solid-svg-icons";

export default async function Home() {
  const r = await fetch(`${process.env.NEXT_API_URL}/notes/`);
  const response = await r.json();

  return (
    <div className="min-h-svh">
      <h1 className="text-2xl mb-2">Cześć Jakub!</h1>
      <div className="flex items-center gap-4">
        <p className="font-extralight">Zadanie na dziś wykonane!</p>
        <div className="rounded-full bg-green-500 w-5 h-5 relative">
          <FontAwesomeIcon
            icon={faCheck}
            className="fas fa-check absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
            style={{ color: "white", fontSize: 12 }}
          />
        </div>
      </div>
      <p className="font-extralight mt-2">
        Sprawdź zadania innych osób aby poszerzyć swoją wiedzę.
      </p>
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
        <Button text="Dodaj nowy" href="/add" />
        <Button variant="secondary" href="/recent" text="Poprzednie notatki" />
      </div>
    </div>
  );
}
