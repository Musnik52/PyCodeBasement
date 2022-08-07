import "./App.css";
import React, { useState } from "react";
import airlock_img from "./Assets/airlock1.png";
import customer_bg from "./Assets/abs_bg.jpg";
import Flights from "./components/Flights/Flights";
import Login from "./components/Login/Login";
import Signup from "./components/Signup/Signup";
import Navbar from "./components/Navbar";
import About from "./components/Miscellaneous/About";
import Contact from "./components/Miscellaneous/Contact";
import Reviews from "./components/Miscellaneous/Reviews";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LandingPage from "./components/LandingPage/LandingPage";
import CustomerProfile from "./components/Profiles/Customer/CustomerProfile";
import AirlineProfile from "./components/Profiles/Airline/AirlineProfile";
import AdminProfile from "./components/Profiles/Admin/AdminProfile";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [loggedUser, setLoggedUser] = useState("");

  const loginHandler = (username, password) => {
    // check username and password
    console.log(username)
    setLoggedUser(username)
    setIsLoggedIn(true);
  };

  const logoutHandler = () => {
    setIsLoggedIn(false);
  };
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App">
          <Navbar isLoggedIn={isLoggedIn} onLogout={logoutHandler} />
          <Switch className="App">
            <Route exact path="/">
              <LandingPage img={airlock_img} />
            </Route>
            <Route exact path="/Flights">
              <Flights />
            </Route>
            <Route exact path="/login">
              <Login onLogin={loginHandler} />
            </Route>
            <Route exact path="/signup">
              <Signup />
            </Route>
            <Route exact path="/contact">
              <Contact />
            </Route>
            <Route exact path="/about">
              <About />
            </Route>
            <Route exact path="/Reviews">
              <Reviews />
            </Route>
            <Route exact path="/profile/customer">
              <CustomerProfile img={customer_bg} login_name={loggedUser}/>
            </Route>
            <Route exact path="/profile/airline">
              <AirlineProfile />
            </Route>
            <Route exact path="/profile/admin">
              <AdminProfile />
            </Route>
          </Switch>
        </header>
      </div>
    </BrowserRouter>
  );
}

export default App;
