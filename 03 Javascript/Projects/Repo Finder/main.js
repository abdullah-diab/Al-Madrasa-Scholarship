const buttonElement = document.querySelector(".button");
const searchInput = document.querySelector(".input");
const usersInputElement = document.querySelector('input[value="users"]');
const cardsElement = document.querySelector(".cards");
const messageElement = document.querySelector(".message");
const loaderElement = document.querySelector(".loader");

const USERS_API = "https://api.github.com/search/users?q=";

const setSearchResult = (data) => {
  let result = "";

  if (data?.length === 0) {
    result = "<p>No results found.</p>";
  } else if (data === null) {
    result = "";
  } else if (data?.length) {
    data.map((item) => {
      result += `
      <article class="card">
          <img class="img" loading="lazy" src="${item.avatar_url}"/>
          <h2 class="name"> ${item.login}</h2>
      </article>
      `;
    });
  }

  cardsElement.innerHTML = result;
};

const setLoadingState = (loadingState) => {
  loaderElement.classList.toggle("hidden", !loadingState);
  loadingState && setSearchResult(null);
};

const getMessage = () => {
  return messageElement.innerText;
};

const setMessage = (message) => {
  messageElement.textContent = message ? `*${message}` : "";
};

const performSearch = (searchTerm, isUserSelected) => {
  getMessage() && setMessage("");

  const typeQuery = isUserSelected ? "+type:user" : "+type:org";

  if (!searchTerm.trim()) {
    setMessage("Please fill out the search field 👆");
    return;
  }

  setLoadingState(true);

  fetch(`${USERS_API}${searchTerm}${typeQuery}`)
    .then((result) => result.json())
    .then((response) => setSearchResult(response.items))
    .finally(() => setLoadingState(false));
};

buttonElement.addEventListener("click", (e) => {
  e.preventDefault();
  performSearch(searchInput.value, usersInputElement.checked);
});
