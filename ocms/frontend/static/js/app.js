const API = "/api/";

function getHeaders() {
    const token = localStorage.getItem("access");
    return {
        "Content-Type": "application/json",
        ...(token ? { "Authorization": `Bearer ${token}` } : {})
    };
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const res = await fetch(API + "accounts/auth/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });
        const data = await res.json();

        if (data.access) {
            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);
            window.location.href = "/student-dashboard/";
        } else {
            alert("Login failed: " + (data.detail || "Check credentials"));
        }
    } catch (err) {
        console.error("Error:", err);
        alert("Server error. Try again.");
    }
}

function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/login/";
}

document.addEventListener('DOMContentLoaded', () => {
    // Add any global initialization here
});
