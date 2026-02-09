const loadBtn = document.getElementById("loadBtn");
const statusEl = document.getElementById("status");
const titleEl = document.getElementById("title");
const bodyEl = document.getElementById("body");

loadBtn.addEventListener("click", async () => {
  statusEl.textContent = "Loading...";

  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    if (!res.ok) throw new Error("Request failed: " + res.status);

    const data = await res.json();
    titleEl.textContent = data.title;
    bodyEl.textContent = data.body;
    statusEl.textContent = "Loaded ✅";
  } catch (err) {
    statusEl.textContent = "Error ❌";
    titleEl.textContent = "Failed";
    bodyEl.textContent = String(err);
  }
});
