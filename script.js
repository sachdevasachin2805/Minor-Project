async function generateQuiz() {
  const topic = document.getElementById("topic").value;
  const output = document.getElementById("output");
  output.textContent = "⏳ Generating quiz... please wait.";

  const response = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic })
  });

  const data = await response.json();
  output.textContent = data.quiz;
}top: 20px;
}