const inputEl = document.querySelectorAll(".card__input");
const calculateBtn = document.querySelector(".card__button");
const dayEl = document.querySelector(".card__input[name='day']");
const monthEl = document.querySelector(".card__input[name='month']");
const yearEl = document.querySelector(".card__input[name='year']");
const resultEl = document.querySelector(".card__resultValue");

const calculateAge = function (year, month, day) {
  const today = new Date();
  const birthdate = new Date(year, month - 1, day);

  let age = today.getFullYear() - birthdate.getFullYear();
  const monthCheck = today.getMonth() - birthdate.getMonth();
  const dayCheck = today.getDate() < birthdate.getDate();

  if (monthCheck < 0 || (monthCheck === 0 && dayCheck)) {
    age--;
  }
  return age;
};

// -- Validation --
const validateDay = function (day) {
  if (day && day > 0 && day <= 31) {
    return true;
  }
};

const validateMonth = function (month) {
  if (month && month > 0 && month <= 12) {
    return true;
  }
};

const validateYear = function (year) {
  const curYear = new Date().getFullYear();
  if (year && year > 0 && year <= curYear) {
    return true;
  }
};

const isDateValid = (dayEl, monthEl, yearEl) => {
  let isValid = [false, false, false];

  if (!validateDay(dayEl.value)) {
    dayEl.classList.add("card__input--error");
  } else {
    isValid[0] = true;
    dayEl.classList.remove("card__input--error");
  }

  if (!validateMonth(monthEl.value)) {
    monthEl.classList.add("card__input--error");
  } else {
    isValid[1] = true;
    monthEl.classList.remove("card__input--error");
  }

  if (!validateYear(yearEl.value)) {
    yearEl.classList.add("card__input--error");
  } else {
    isValid[2] = true;
    yearEl.classList.remove("card__input--error");
  }

  return isValid.every((item) => item === true);
};

const onClickHandler = function () {
  if (!isDateValid(dayEl, monthEl, yearEl)) {
    resultEl.textContent = "--";
    return;
  }
  resultEl.textContent = calculateAge(yearEl.value, monthEl.value, dayEl.value);
};

calculateBtn.addEventListener("click", onClickHandler);

// -- Keyboard Accessibility --
inputEl.forEach((item) =>
  item.addEventListener("keydown", (e) => {
    e.key === "Enter" && onClickHandler();
  })
);
