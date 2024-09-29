import Button from "@/components/Button";
import Card from "@/components/Card";
import Header from "@/components/Header";
import AudioPlayer from "@/components/Audio";

export default async function Text(props: any) {
  const r = await fetch(
    `${process.env.NEXT_API_URL}/notes/${props.params.id}/`,
    {
      method: "GET",
    },
  );
  const response = await r.json();

  return (
    <div className="min-h-svh">
      <Header
        isQuizDone={response.is_quiz_done}
        isRead={response.is_read || response.is_lisened}
        subtitle={response.topic}
        title={response.subject}
        href={`/note/${response.id}`}
      />
      <p className="mt-10 text-xl">Nauka (audio)</p>
      <AudioPlayer audioPath={response.audio_file_absolute} />

      <p className="mt-16 mb-4 text-xl">
        Sprawdź inne materiały z tego samego tematu
      </p>
      <Card
        description={response.next_note.first_question}
        duration={response.next_note.duration}
        slug={`/note/${response.next_note.id}`}
        title={response.next_note.subject}
      />
      <div className="flex flex-col gap-2 mt-16">
        <Button text="Przejdź do testu" href={`/note/${response.id}/test`} />
      </div>
    </div>
  );
}
