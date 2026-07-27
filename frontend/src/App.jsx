import ChatBox from "./components/ChatBox";
import Dashboard from "./components/Dashboard";
import "./App.css";

function App() {
  return (
    <div className="app">

      <header className="header">
        <h1>🚀 Skylark BI Agent</h1>
        <p>AI Business Intelligence powered by Monday.com</p>
      </header>

      <Dashboard />

      <ChatBox />

    </div>
  );
}

export default App;