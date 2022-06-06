import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          BORIS GROUP LTD. LORD OF REACT.JS!!! <br />
          <p>Not accepting new applicants. Sorry Elad.</p>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          targ
          et="_blank"
          rel="noopener noreferrer"
        >
          Click here to not join us.
        </a>
      </header>
    </div>
  );
}

export default App;
