import { useState } from "react";

export default function AuthForm({ mode, onSuccess, switchMode }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const endpoint = mode === "login" ? "login" : "signup";
    const base = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";
    try {
      const res = await fetch(`${base}/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      const text = await res.text();
      let data = {};
      try {
        data = JSON.parse(text || "{}");
      } catch (e) {
        // non-json response
      }
      if (!res.ok) {
        alert(data.detail || text || "Authentication error");
        return;
      }
      onSuccess(data.access_token);
    } catch (err) {
      console.error(err);
      alert("Network error: could not reach backend");
    }
  };

  return (
    <div className="auth-form">
      <h2>{mode === "login" ? "Login" : "Sign Up"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">
          {mode === "login" ? "Login" : "Sign Up"}
        </button>
      </form>
      <p>
        {mode === "login" ? "Don't have an account?" : "Already have an account?"}{" "}
        <button
          type="button"
          className="mode-toggle"
          onClick={() =>
            switchMode(mode === "login" ? "signup" : "login")
          }
        >
          {mode === "login" ? "Sign Up" : "Login"}
        </button>
      </p>
    </div>
  );
}
