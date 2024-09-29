import Button from "@/components/Button";
import Header from "@/components/Header";

export default async function Note(props: any) {
  const r = await fetch(
    `${process.env.NEXT_API_URL}/notes/${props.params.id}/`,
  );
  const response = await r.json();
  console.log(response);

  return (
    <div className="min-h-svh">
      <Header
        isQuizDone={response.is_quiz_done}
        isRead={response.is_read || response.is_listened}
        subtitle={response.topic}
        title={response.subject}
      />
      <p className="mt-10 text-xl">Nauka</p>
      <p className="mt-2 font-extralight">
        Przeczytaj podsumowanie notatki lub posłuchaj podcastu. Możesz również
        śprowadzić rozmowę na temat notatki.
      </p>
      <div className="flex flex-col gap-2 mt-4">
        <Button
          text="Przeczytaj notatkę"
          href={`/note/${response.id}/text`}
          done={response.is_read}
        />
        <Button
          text="Posłuchaj audio"
          href={`/note/${response.id}/audio`}
          variant="alt"
          done={response.is_listened}
        />
      </div>

      <p className="mt-10 text-xl">Test</p>
      <p className="mt-2 font-extralight">
        Sprawdź swoją wiedzę poprzez test przygotowany na podstawie Twojej
        notatki.
      </p>
      <div className="flex flex-col gap-2 mt-4">
        <Button
          text="Przejdź do testu"
          href={`/note/${response.id}/test`}
          done={response.is_quiz_done}
        />
      </div>
    </div>
  );
}
