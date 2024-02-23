const labelElements = document.querySelectorAll("label");
const sectionElements = document.querySelectorAll("section");

// Accessiblity function
labelElements.forEach((item) =>
  item.addEventListener("keydown", (e) => {
    if (e.key === "Enter") item.click();
  })
);

// Add Animation Feature
function observeElements(sectionElements) {
  const options = { threshold: 1 };

  const callback = (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
      }
    });
  };

  const observer = new IntersectionObserver(callback, options);

  sectionElements.forEach((element) => {
    observer.observe(element);
  });
}

observeElements(sectionElements);
