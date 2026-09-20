import { useReducer } from "react";
import Button from "./components/Button";
import checkReducer, { checkInitialState } from "./reducers/checkReducer";
import predictReducer, { predictInitialState } from "./reducers/predictionReducer";

export default function App() {

  const [serverState, serverDispatch] = useReducer(checkReducer, checkInitialState);
  const [aiServerState, aiServerDispatch] = useReducer(checkReducer, checkInitialState);
  const [predictionState, predictionDispatch] = useReducer(predictReducer, predictInitialState);

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
          <li>Typescript React + Tailwind CSS (Frontend)</li>  
          <li>ASP.NET Core Web API (Backend)</li>
          <li>Flask + Tensorflow (AI Service)</li>
        </ul>
        <hr className="my-4" />

        <div
          className="flex flex-col lg:flex-row gap-2"
        >
          <Button
            className="bg-blue-600 text-white hover:bg-blue-500"
          >Check Server</Button>

          <Button
            className="bg-green-600 text-white hover:bg-green-500"
          >Check AI Service</Button>
        </div>

        <hr className="my-4" />

      </div>
      
    </main>
  )
}