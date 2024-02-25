// DOM Elements
const AppElement = document.querySelector(".App");
const TaskListElement = document.querySelector(".TaskList__list");
const TaskListLink = document.querySelector(".TaskList__link");
const TaskSearchBarButton = document.querySelector(".TaskSearchBar__button");
const darkThemeToggleElement = document.querySelector(".DarkThemeToggle");
const inputElement = document.querySelector(".TaskSearchBar__input");

// Interacting with local storage
const fetchData = (key) => {
  const data = localStorage.getItem(key);
  return data ? JSON.parse(data) : false;
};

const saveToDB = (key, data) => {
  localStorage.setItem(key, JSON.stringify(data));
};

// Task list and Empty state
const renderTaskList = (tasks) => {
  let taskList = "";

  tasks.forEach((task) => {
    taskList += `<li class="TaskList__taskContent${
      task.isCompleted ? " TaskList__taskContent--isActive" : ""
    }">
      <div class='TaskList__checkbox' tabindex="0" role="button">
        <img class='TaskList__checkboxImg' src="assets/icon-checkmark.svg" alt="checkmark" />
      </div>
      <div class='TaskList__valueContent'>
        <p class='TaskList__value'>
          ${task.value}
        </p>
        <img src="assets/icon-basket.svg"
            class='TaskList__deleteIcon'
            alt="basket-icon"
        />
      </div>
    </li>`;
  });

  TaskListElement.innerHTML = taskList;
  inputElement.value = "";
};

const renderEmptyState = () => {
  TaskListElement.innerHTML = `<li class='EmptyList'>
      <img class='EmptyList__img' src="assets/icon-empty.svg" alt="list is empty" />
      <p>قائمة المهام فارغة</p>
    </li>`;
};

// Task list interactions
const initTaskListeners = () => {
  getDeleteIcons().forEach((icon, index) => {
    icon.addEventListener("click", (e) => deleteTask(e, index));
  });
  getCheckboxElements().forEach((box, index) => {
    box.addEventListener("click", (e) => toggleTask(e, index));
    box.addEventListener(
      "keydown",
      (e) => e.key === "Enter" && toggleTask(e, index)
    );
  });
};

// Task completion status
const toggleTask = (e, index) => {
  const tasks = fetchData("tasks");
  e.currentTarget.parentElement.classList.toggle(
    "TaskList__taskContent--isActive"
  );
  tasks[index].isCompleted = !tasks[index].isCompleted;
  saveToDB("tasks", tasks);
};

// Adding a new task
const addTask = (e) => {
  e.preventDefault();
  const taskValue = inputElement.value;

  if (!taskValue) return;

  const task = {
    value: taskValue,
    isCompleted: false,
  };

  const tasks = fetchData("tasks") || [];

  tasks.push(task);
  saveToDB("tasks", tasks);

  initTaskList(tasks);
};

// Deleting a task
const deleteTask = (e, index) => {
  const answer = confirm("هل أنت متأكد من حذف المهمة؟");
  if (answer === false) return;
  const tasks = fetchData("tasks");
  tasks.splice(index, 1);
  saveToDB("tasks", tasks);
  initTaskList(tasks);
};

const getDeleteIcons = () => document.querySelectorAll(".TaskList__deleteIcon");
const getCheckboxElements = () =>
  document.querySelectorAll(".TaskList__checkbox");

// Dark mode
const toggleDarkMode = () => {
  AppElement.classList.toggle("App--isDark");
  saveToDB("darkModeFlag", AppElement?.classList.contains("App--isDark"));
};

// Initializing
const initDataOnStartup = () => {
  fetchData("darkModeFlag") && toggleDarkMode();
  initTaskList(fetchData("tasks"));
};

const initListeners = () => {
  darkThemeToggleElement.addEventListener("click", toggleDarkMode);
  TaskSearchBarButton.addEventListener("click", addTask);
  TaskListLink.addEventListener("click", () => {
    TaskListElement.classList.toggle("TaskList__list--hideCompleted");
    TaskListLink.classList.toggle("TaskList__link--isActive");
  });
};

const initTaskList = (tasks) => {
  if (tasks?.length) {
    renderTaskList(tasks);
    initTaskListeners();
  } else {
    renderEmptyState();
  }
};

initDataOnStartup();
initListeners();
