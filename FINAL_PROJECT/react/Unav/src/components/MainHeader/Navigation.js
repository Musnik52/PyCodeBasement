import React from "react";

import "./Navigation.css";

const Navigation = (props) => {
  return (
    <nav className="nav">
      <ul>
        {props.isLoggedIn && (
          <li>
            <a href="/my_info">My Info</a>
          </li>
        )}
        {props.isLoggedIn && (
          <li>
            <a href="/flights">Flights</a>
          </li>
        )}
        {props.isLoggedIn ? (
          <li>
            <button onClick={props.onLogout}>Logout</button>
          </li>
        ) : (
          <li>
            <button onClick={props.onLogout}>
              <a href="/login">Login</a>
            </button>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default Navigation;
