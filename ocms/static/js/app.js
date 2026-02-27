const API = "http://127.0.0.1:8000/api/";

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    if (!email || !password) {
        alert("Please enter both email and password.");
        return;
    }

    fetch(API + "auth/login/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.access) {
            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);
            window.location.href = "/dashboard/";
        } else {
            alert("Login failed. Please check your credentials.");
        }
    })
    .catch(err => {
        console.error("Error:", err);
        alert("An error occurred. Please try again later.");
    });
}

function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/login/";
}
