import { NavLink, withRouter } from "react-router-dom";
import airlock_logo from "../Assets/airlock.png"

const Navbar = (props) => {
  console.log(props);

  return (
    <nav className="navbar navbar-dark navbar-expand-lg bg-light bg-dark">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Airlock
        </NavLink>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li>
              <NavLink className="nav-link" aria-current="page" to="flights">
                Flights
              </NavLink>
            </li>
            {!props.isLoggedIn && 
              <li className="nav-item">
                <NavLink className="nav-link active" to="/login">
                  Login/Sign-Up
                </NavLink>
              </li>
            }
            {props.isLoggedIn && 
              <li className="nav-item">
                <NavLink
                  className="nav-link active"
                  to="/flights"
                  onClick={props.onLogout}
                >
                  Logout
                </NavLink>
              </li>
            }
            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Misc
              </a>
              <ul className="dropdown-menu">
                <li>
                  <NavLink className="dropdown-item" to="/about">
                    About Airlock
                  </NavLink>
                </li>
                <li>
                  <NavLink className="dropdown-item" to="/contact">
                    Contact Us!
                  </NavLink>
                </li>
                <li>
                  <hr className="dropdown-divider" />
                </li>
                <li>
                  <NavLink className="dropdown-item" to="/reviews">
                    Read What People Think!
                  </NavLink>
                </li>
              </ul>
            </li>
            <li className="nav-item">
              <a className="nav-link disabled">Teleporting: Coming Soon</a>
            </li>
          </ul>
        </div>
        <img src={airlock_logo} alt="Airlock Logo" width="45" height="45" className="d-inline-block align-text-right"/>
      </div>
    </nav>
  );
};

export default withRouter(Navbar);
