import React from "react";
import { NavLink, withRouter } from "react-router-dom";

const Navbar = (props) => {
  console.log(props);
  return (
    <nav className="nav-wrapper black">
      <div className="container">
        <div className="brand-logo center">Airlock</div>
        <ul className="right">
          <li>
            <NavLink to="/">Home</NavLink>
          </li>
          <li>
            <NavLink to="/login">Login</NavLink>
          </li>
          <li>
            <NavLink to="/signup">Signup</NavLink>
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
