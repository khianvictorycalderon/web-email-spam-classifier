export default function App() {
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
          <button
            className="
              cursor-pointer
              px-12 py-2 rounded-md
              bg-blue-600 text-white hover:bg-blue-500
              trasition duration-300
            "
          >Check Server</button>

          <button
            className="
              cursor-pointer
              px-12 py-2 rounded-md
              bg-green-600 text-white hover:bg-green-500
              trasition duration-300
            "
          >Check AI Service</button>
        </div>

        <hr className="my-4" />

      </div>
      
    </main>
  )
}