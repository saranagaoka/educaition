"use client";

import { useState } from "react";
import Button from "./Button";
import { Question } from "@/app/note/[id]/test/page";

interface IProps {
  questions: Question[];
}

export default function Quiz(props: IProps) {
  const [showAnswers, setShowAnswers] = useState(false);

  return (
    <form className="z-10">
      <ol className="list-decimal ml-6 flex flex-col gap-10">
        {props.questions.map((q) => {
          return (
            <li>
              <p>{q.text}</p>
              <ol className="flex flex-col gap-2 mt-4 -ml-6">
                {q.answers.map((a) => {
                  return (
                    <li>
                      <label className="flex gap-4">
                        <input
                          type="radio"
                          name={q.id.toString()}
                          className="opacity-0 absolute peer"
                          disabled={showAnswers}
                        />
                        <div
                          className={`min-w-4 h-4 rounded-full border-2 ${!showAnswers || (showAnswers && a.correct) ? "peer-checked:bg-green-500" : "peer-checked:bg-red-500"} peer-checked:border-none mt-1`}
                        />
                        <p
                          className={`font-extralight ${showAnswers && a.correct ? "font-semibold text-green-500" : ""}`}
                        >
                          {a.text}
                        </p>
                      </label>
                    </li>
                  );
                })}
              </ol>
            </li>
          );
        })}
      </ol>
      <div className="flex flex-col gap-2 mt-16 fixed bottom-4 right-8 z-10">
        <Button
          text={showAnswers ? "Schowaj odpowiedzi" : "Sprawdź odpowiedzi"}
          onClick={() => setShowAnswers((prev) => !prev)}
        />
      </div>
    </form>
  );
}
