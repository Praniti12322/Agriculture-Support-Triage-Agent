import { useState, useRef, useEffect } from "react";
import "./App.css";
import AuthForm from "./AuthForm";

// Helper function to convert raw markdown to React styled elements
const formatResponseText = (text) => {
  if (!text) return null;

  // Split the text by the bold markdown **
  const parts = text.split(/(\*\*.*?\*\*)/g);
  return parts.map((part, index) => {
    // If it's a bold segment, remove asterisks and wrap in <strong>
    if (part.startsWith('**') && part.endsWith('**')) {
      return <strong key={index}>{part.slice(2, -2)}</strong>;
    }

    // For regular text, respect newlines by mapping \n to <br/>
    const lines = part.split('\n');
    return (
      <span key={index}>
        {lines.map((line, i) => (
          <span key={i}>
            {line}
            {i !== lines.length - 1 && <br />}
          </span>
        ))}
      </span>
    );
  });
};

export default function App() {
  const [token, setToken] = useState(
    localStorage.getItem("access_token") || ""
  );
  const [authMode, setAuthMode] = useState("login");

  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  // Auto-scroll to bottom of chat when messages change
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  const handleAuthSuccess = (accessToken) => {
    setToken(accessToken);
    localStorage.setItem("access_token", accessToken);
  };

  const handleLogout = () => {
    setToken("");
    localStorage.removeItem("access_token");
    setChat([]);
  };

  const send = async () => {
    if (!msg.trim()) return;

    // Immediately push user's message to UI
    const userMessage = msg;
    setChat((prev) => [...prev, { user: userMessage, bot: null }]);
    setMsg("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ message: userMessage }),
      });

      if (res.status === 401) {
        handleLogout();
        return;
      }

      const data = await res.json();

      // Update the last message in chat array with the bot's response
      setChat((prev) => {
        const newChat = [...prev];
        newChat[newChat.length - 1].bot = data.response;
        return newChat;
      });

    } catch (err) {
      console.error(err);
      setChat((prev) => {
        const newChat = [...prev];
        newChat[newChat.length - 1].bot = "Error: Could not reach the server.";
        return newChat;
      });
    } finally {
      setLoading(false);
    }
  };

  if (!token) {
    return (
      <div className="auth-wrapper">
        <AuthForm
          mode={authMode}
          onSuccess={handleAuthSuccess}
          switchMode={setAuthMode}
        />
      </div>
    );
  }

  return (
    <div className="App">
      <header className="header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>🌾 Krishi AI Assistant</h1>
        <button onClick={handleLogout} style={{ background: 'transparent', color: 'white', border: '1px solid white', padding: '5px 15px', borderRadius: '4px', cursor: 'pointer' }}>Logout</button>
      </header>

      <div className="chat-container">
        {chat.map((c, i) => (
          <div key={i} style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            {c.user && (
              <div className="message-wrapper user">
                <div className="chat-bubble user">
                  {c.user}
                </div>
              </div>
            )}
            {c.bot ? (
              <div className="message-wrapper bot">
                <div className="chat-bubble bot">
                  {formatResponseText(c.bot)}
                </div>
              </div>
            ) : (
              <div className="message-wrapper bot">
                <div className="chat-bubble bot" style={{ fontStyle: "italic", color: "#888" }}>
                  Assistant is typing...
                </div>
              </div>
            )}
          </div>
        ))}
        {/* Invisible div to scroll to */}
        <div ref={chatEndRef} />
      </div>

      <footer className="footer">
        <div className="input-group">
          <input
            value={msg}
            onChange={(e) => setMsg(e.target.value)}
            placeholder="Type your crop issue here..."
            onKeyPress={(e) => e.key === "Enter" && send()}
            autoFocus
          />
          <button onClick={send} disabled={loading || !msg.trim()}>
            Send
          </button>
        </div>
      </footer>
    </div>
  );
}
