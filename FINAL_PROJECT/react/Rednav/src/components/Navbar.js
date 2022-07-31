import React, { useState } from "react";
import { NavLink, withRouter } from "react-router-dom";

const Navbar = (props) => {
  console.log(props);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const loginHandler = (username, password) => {
    // check username and password
    setIsLoggedIn(true);
  };

  const logoutHandler = () => {
    setIsLoggedIn(false);
  };

  return (
    <nav className="nav-wrapper black">
      <div className="container">
        <div className="brand-logo center">Airlock</div>
        <ul className="right">
          <li>
            <NavLink to="/home">Home</NavLink>
          </li>
          <li>
            <NavLink to="/login">Login</NavLink>
          </li>
          <li>
            <NavLink to="/signup">Signup</NavLink>
          </li>
          <li>
            <NavLink to="/">Signout</NavLink>
          </li>
          <li>
            <NavLink to="/about">About</NavLink>
          </li>
          <li>
            <NavLink to="/contact">Contact</NavLink>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default withRouter(Navbar);
