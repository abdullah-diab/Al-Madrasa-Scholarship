/*
 * 1. Update Redux -> Node.js, React Testing Library -> MongoDB
 * 2. Add new skill -> Typescript, after javascript, 2 years
 * 3. Remove "Download CV" element
 * 4. Personal image: width -> 36rem
 * 5. Bonus: Highlight skills items: li -> click -> .underline
 */

const reduxItem = document.querySelector("[data-name=Redux] .skills__title");
const RTLItem = document.querySelector(
  '[data-name="React testing library"] .skills__title'
);

reduxItem.innerText = "Node.js";
RTLItem.innerText = "MongoDB";

// ---

const jsItem = document.querySelector("[data-name=Javascript]");
const tsString = `<li data-name="HTML" class="skills__column">
<h2 class="skills__title">Typescript</h2>
<span class="skills__years">2 years</span>
</li>`;

jsItem?.insertAdjacentHTML("afterend", tsString);

// ---

const findOutLink = document.querySelector(".find-out-link");
findOutLink.remove();

// ---

const bioPic = document.querySelector(".bio__pic");
bioPic.style.width = "36rem";

// ---

const skillsList = document.querySelectorAll(".skills__column");

[...skillsList].map((item) => {
  item.addEventListener("click", () => {
    const activeElement = document.querySelector(".underline");

    if (activeElement) {
      activeElement.classList.remove("underline");
    }

    item.classList.add("underline");
  });
});
