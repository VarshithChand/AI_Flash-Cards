document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("topicForm");
  const input = document.getElementById("topicInput");
  const flashcards = document.getElementById("flashcards");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const topic = input.value.trim();
    if (!topic) return;

    flashcards.innerHTML = "<p class='text-center'>⏳ Generating questions...</p>";

    fetch("/get_questions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic }),
    })
      .then((res) => res.json())
      .then((data) => {
        flashcards.innerHTML = ""; // Clear previous flashcards
        data.forEach((card, index) => {
          const key = `flashcard_${topic}_${index}`;
          const isDone = localStorage.getItem(key) === "done";

          const div = document.createElement("div");
          div.className = `bg-gray-800 p-5 rounded-xl shadow-lg ${
            isDone ? "bg-green-700" : ""
          }`;

          const q = document.createElement("p");
          q.className = "font-bold";
          q.textContent = card.question;

          const a = document.createElement("p");
          a.className = "mt-3 hidden";
          a.textContent = card.answer;

          const btn = document.createElement("button");
          btn.textContent = "Show Answer";
          btn.className = "mt-4 px-3 py-1 bg-blue-600 hover:bg-blue-700 rounded";

          btn.addEventListener("click", () => {
            a.classList.toggle("hidden");
            localStorage.setItem(key, "done");
            div.classList.add("bg-green-700");
          });

          div.appendChild(q);
          div.appendChild(a);
          div.appendChild(btn);
          flashcards.appendChild(div);
        });
      });
  });
});
