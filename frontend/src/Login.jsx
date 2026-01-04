import { useState } from "react";
import api from "./api/axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const res = await api.post("token/", { username, password });
      localStorage.setItem("access", res.data.access);
      alert("Login successful");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Login</h2>
      <input
        className="w-full border p-2 mb-3 rounded"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        className="w-full border p-2 mb-3 rounded"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button
        className="w-full bg-blue-600 text-white py-2 rounded"
        onClick={login}
      >
        Login
      </button>
    </div>
  );
}

export default Login;
