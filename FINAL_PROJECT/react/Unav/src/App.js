import React, { useState } from "react";

import Login from "./components/Login/Login";
import MyPage from "./components/MyPage/MyPage";
import MainHeader from "./components/MainHeader/MainHeader";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const loginHandler = (email, password) => {
    // We should of course check email and password
    // But it's just a dummy/ demo anyways
    setIsLoggedIn(true);
  };

  const logoutHandler = () => {
    setIsLoggedIn(false);
  };

  return (
    <React.Fragment>
      <MainHeader isAuthenticated={isLoggedIn} onLogout={logoutHandler} />
      <main>
        <h1>
          {" "}
          Welcome to the best & biggest flight hub!
          <br /> Airlock
        </h1>
        {!isLoggedIn && <Login onLogin={loginHandler}/>}
        {isLoggedIn && <MyPage onLogout={logoutHandler} />}
      </main>
    </React.Fragment>
  );
}

export default App;
