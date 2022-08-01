import { NavLink, withRouter } from "react-router-dom";

const Navbar = (props) => {
  console.log(props);

  return (
    <nav className="nav-wrapper black">
      <div className="container">
        <div className="brand-logo center">Airlock</div>
        <ul className="right">
          <li>
            <NavLink to="/home">Home</NavLink>
          </li>
          <li>
            {!props.isLoggedIn && <NavLink to="/login">Login/Signup</NavLink>}
          </li>
          <li>{props.isLoggedIn && <NavLink to="/">Logout</NavLink>}</li>
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
