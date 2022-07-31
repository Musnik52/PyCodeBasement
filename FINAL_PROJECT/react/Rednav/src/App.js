// import logo from "./logo.svg";
import "./App.css";
import Home from "./components/Home";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Navbar from "./components/Navbar";
import About from "./components/About";
import Contact from "./components/Contact";
import Post from "./components/Post";
import { BrowserRouter, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App">
          <Navbar />
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/signup" component={Signup} />
          <Route exact path="/contact" component={Contact} />
          <Route exact path="/about" component={About} />
          <Route path="/posts/:post_id" component={Post} />
        </header>
      </div>
    </BrowserRouter>
  );
}

export default App;
