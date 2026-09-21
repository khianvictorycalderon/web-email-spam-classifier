import { useReducer, useState } from "react";
import Button from "./components/Button";
import checkReducer, { checkInitialState } from "./reducers/checkReducer";
import predictReducer, { predictInitialState } from "./reducers/predictionReducer";
import axios from "axios";
import SubmitButtonInput from "./components/SubmitButtonInput";

const ENV = import.meta.env;

export default function App() {

  const [serverState, serverDispatch] = useReducer(checkReducer, checkInitialState);
  const [aiServerState, aiServerDispatch] = useReducer(checkReducer, checkInitialState);
  const [classificationState, classificationDispatch] = useReducer(predictReducer, predictInitialState);

  const [contentInput, setContentInput] = useState<string>("");
  
  const checkServerState = async () => {
    serverDispatch({ type: "FETCH_START" });
    try {
      const res = await axios.get(`${ENV.VITE_API_URL}/health`);
      serverDispatch({ type: "FETCH_SUCCESS", payload: res.data });
    } catch (e: unknown) {
      serverDispatch({ type: "FETCH_ERROR", payload: e instanceof Error ? e.message : String(e)});
    }
  }

  const checkAIServerState = async () => {
    aiServerDispatch({ type: "FETCH_START" });
    try {
      const res = await axios.get(`${ENV.VITE_API_URL}/services/ai-service/health`);
      aiServerDispatch({ type: "FETCH_SUCCESS", payload: res.data });
    } catch (error: unknown) {
      aiServerDispatch({ type: "FETCH_ERROR", payload: error instanceof Error ? error.message : String(error)});
    }
  }

  const classifyEmailContent = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    classificationDispatch({ type: "FETCH_START" });

    try {
      const res = await axios.post(`${ENV.VITE_API_URL}/api/ai-service/classify`, {
        emain_content: contentInput
      });
      classificationDispatch({ type: "FETCH_SUCCESS", payload: res.data });
    } catch (e: unknown) {
      classificationDispatch({ type:"FETCH_ERROR", payload: e instanceof Error ? e.message : String(e) });
    }

  }

  return (
    <main
      className="
        min-h-screen w-full
        flex flex-row
        items-center justify-center
      "
    >
      
      <div
        className="text-center"
      >
        <h2
          className="text-2xl font-bold"
        >Web Email Spam Classifier Demo</h2>
        <ul
          className="mt-4"
        >
          {/* <li>Typescript React + Tailwind CSS (Frontend)</li>  
          <li>ASP.NET Core Web API (Backend)</li>
          <li>Flask + Tensorflow (AI Service)</li> */}
        </ul>
        <hr className="my-4" />

        <div
          className="flex flex-col lg:flex-row gap-2"
        >
          <Button
            disabled={serverState.loading}
            className={serverState.error 
              ? "bg-red-600 text-white hover:bg-red-500" 
              : "bg-blue-600 text-white hover:bg-blue-500"
            }
            onClick={checkServerState}
          >{serverState.loading ? "Checking..." 
            : serverState.data?.status
              ?? serverState.error
              ?? "Check Server"
            }</Button>

          <Button
            disabled={aiServerState.loading}
            className={aiServerState.error
              ? "bg-red-600 text-white hover:bg-red-500"
              : "bg-green-600 text-white hover:bg-green-500"
            }
            onClick={checkAIServerState}
          >{aiServerState.loading ? "Checking..."
            : aiServerState.data?.status
              ?? aiServerState.error
              ?? "Check AI Service"
          }</Button>
        </div>

        <hr className="my-4" />

        <form
          className="flex flex-col gap-4"
          onSubmit={classifyEmailContent}
        >
          <div
            className="flex flex-col lg:flex-row gap-2 items-center justify-center"
          >
            <label>Email Content: </label>
            <input 
              value={contentInput}
              onChange={(e) => setContentInput(e.target.value)}
              type="text"
              className="
                w-full
                rounded-md p-2
                focus:outline-blue-600
                focus:bg-neutral-100
                border-2
                border-neutral-700
              "
            />
          </div>

          {classificationState.loading == false && classificationState.data || classificationState.error ? (
            <p
              className={`
                font-bold text-xl
                ${classificationState.data?.classification
                ? classificationState.data.classification > 0.5
                  ? "text-red-600"
                  : "text-green-600"
                : "text-yellow-500"}  
              `}
            >Classification: {
              classificationState.data?.classification
              ? classificationState.data.classification > 0.5
                ? "Spam"
                : "Not Spam"
              : "Unknown or Failed"
            }</p>
          ) : null}

          <SubmitButtonInput>Classify</SubmitButtonInput>
        </form>

      </div>
      
    </main>
  )
}