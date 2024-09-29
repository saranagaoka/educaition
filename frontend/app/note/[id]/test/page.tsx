import Card from "@/components/Card";
import Header from "@/components/Header";
import Quiz from "@/components/Quiz";

export interface ApiResponse<T> {
  is_ready: boolean;
  is_read: boolean;
  is_listened: boolean;
  is_quiz_done: boolean;
  questions: Question[];
}

interface Answer {
  id: number;
  text: string;
  correct: boolean;
}

export interface Question {
  id: number;
  text: string;
  answers: Answer[];
  type: "open" | "closed";
}

export default async function Test(props: any) {
  const r = await fetch(
    `${process.env.NEXT_API_URL}/notes/${props.params.id}/quiz/`,
    {
      method: "GET",
    },
  );
  const response = await r.json();
  console.log(response);

  return (
    <div className="min-h-svh mb-16">
      <Header
        isQuizDone={response.is_quiz_done}
        isRead={response.is_read || response.is_lisened}
        subtitle={response.topic}
        title={response.subject}
        href={`/note/${props.params.id}`}
      />
      <p className="mt-10 mb-2 text-xl">Test</p>
      <Quiz
        questions={response.questions.map((q) => ({
          ...q,
          answers: q.answers.toSorted(() => Math.random() - 0.5),
        }))}
      />
      <p className="mt-16 mb-4 text-xl">
        Sprawdź inne materiały z tego samego tematu
      </p>
      <Card
        description={response.next_note.first_question}
        duration={response.next_note.duration}
        slug={`/note/${response.next_note.id}`}
        title={response.next_note.subject}
      />
    </div>
  );
}
