const USERS_KEY = "recipeFinderUsers";
const CURRENT_USER_KEY = "currentUser";

function getUsers() {
  return JSON.parse(localStorage.getItem(USERS_KEY)) || [];
}

function saveUsers(users) {
  localStorage.setItem(USERS_KEY, JSON.stringify(users));
}

const signupForm = document.getElementById("signupForm");

if (signupForm) {
  signupForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const firstName = document.getElementById("firstName").value.trim();
    const lastName = document.getElementById("lastName").value.trim();
    const dob = document.getElementById("dob").value;
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim().toLowerCase();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    const selectedRole = document.querySelector('input[name="role"]:checked');
    const role = selectedRole ? selectedRole.value : "user";

    const formMessage = document.getElementById("formMessage");
    if (formMessage) formMessage.textContent = "";

    if (!firstName || !lastName || !dob || !username || !email || !password || !confirmPassword) {
      if (formMessage) formMessage.textContent = "Please fill in all required fields.";
      return;
    }

    if (password.length < 8) {
      if (formMessage) formMessage.textContent = "Password must be at least 8 characters.";
      return;
    }

    if (password !== confirmPassword) {
      if (formMessage) formMessage.textContent = "Passwords do not match.";
      return;
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      if (formMessage) formMessage.textContent = "Please enter a valid email format (e.g., user@example.com).";
      return;
    }

    const users = getUsers();

    const existingUser = users.find(
      (user) =>
        user.username.toLowerCase() === username.toLowerCase() ||
        user.email === email
    );

    if (existingUser) {
      if (formMessage) formMessage.textContent = "Username or email already exists.";
      return;
    }

    const newUser = {
      id: Date.now(),
      name: `${firstName} ${lastName}`,
      firstName,
      lastName,
      dob,
      username,
      email,
      password,
      role
    };

    users.push(newUser);
    saveUsers(users);
    localStorage.setItem(CURRENT_USER_KEY, JSON.stringify(newUser));

    if (formMessage) formMessage.textContent = "Account created successfully. Redirecting...";

    signupForm.reset();

    setTimeout(() => {
      window.location.href = "homepage.html";
    }, 1000);
  });
}

const loginForm = document.getElementById("loginForm");

if (loginForm) {
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const identifier = document.getElementById("loginIdentifier").value.trim().toLowerCase();
    const password = document.getElementById("loginPassword").value;

    const formMessage = document.getElementById("formMessage");
    if (formMessage) formMessage.textContent = "";

    if (!identifier || !password) {
      if (formMessage) formMessage.textContent = "Please enter username/email and password.";
      return;
    }

    const users = getUsers();

    const foundUser = users.find(
      (user) =>
        (user.username.toLowerCase() === identifier || user.email === identifier) &&
        user.password === password
    );

    if (!foundUser) {
      if (formMessage) formMessage.textContent = "Invalid username/email or password.";
      return;
    }

    localStorage.setItem(CURRENT_USER_KEY, JSON.stringify(foundUser));

    if (foundUser.role === "admin") {
      window.location.href = "admin_pages/admin_dashboard.html";
    } else {
      window.location.href = "homepage.html";
    }
  });
}