const counterValueEl = document.getElementById("counterValue");
const counterIncBtn = document.getElementById("counterIncBtn");
const counterDecBtn = document.getElementById("counterDecBtn");
const counterResetBtn = document.getElementById("counterResetBtn");

const postIdInput = document.getElementById("postIdInput");
const loadPostBtn = document.getElementById("loadPostBtn");
const loadPost1Btn = document.getElementById("loadPost1Btn");
const loadPost2Btn = document.getElementById("loadPost2Btn");
const postStatusEl = document.getElementById("postStatus");
const postTitleEl = document.getElementById("postTitle");
const postBodyEl = document.getElementById("postBody");

let counterValue = 0;

const renderCounter = () => {
  counterValueEl.textContent = String(counterValue);
};

counterIncBtn.addEventListener("click", () => {
  counterValue += 1;
  renderCounter();
});

counterDecBtn.addEventListener("click", () => {
  counterValue -= 1;
  renderCounter();
});

counterResetBtn.addEventListener("click", () => {
  counterValue = 0;
  renderCounter();
});

const loadPost = async (postId) => {
  postStatusEl.textContent = "Loading...";

  try {
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${postId}`
    );
    if (!res.ok) throw new Error("Request failed: " + res.status);

    const data = await res.json();
    postTitleEl.textContent = data.title;
    postBodyEl.textContent = data.body;
    postStatusEl.textContent = `Loaded ${postId} ✅`;
  } catch (err) {
    postStatusEl.textContent = "Error ❌";
    postTitleEl.textContent = "Failed";
    postBodyEl.textContent = String(err);
  }
};

loadPostBtn.addEventListener("click", () => {
  const postId = Number(postIdInput.value || 1);
  loadPost(postId);
});

loadPost1Btn.addEventListener("click", () => loadPost(1));
loadPost2Btn.addEventListener("click", () => loadPost(2));

renderCounter();
