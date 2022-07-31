import React, { useState } from "react";
import Card from "./UI/Card/Card";
import Button from "./UI/Button/Button";
import "./Login.css";

const Login = (props) => {
  console.log(props);

  const [enteredEmail, setEnteredEmail] = useState("");
  const [emailIsValid, setEmailIsValid] = useState();
  const [enteredPassword, setEnteredPassword] = useState("");
  const [passwordIsValid, setPasswordIsValid] = useState();
  const [formIsValid, setFormIsValid] = useState(false);

  const emailChangeHandler = (event) => {
    // live update of input
    setEnteredEmail(event.target.value);

    setFormIsValid(
      // valodate email includes @ and password length is more than 6
      event.target.value.includes("@") && enteredPassword.trim().length > 6
    );
  };

  const passwordChangeHandler = (event) => {
    // live update of input
    setEnteredPassword(event.target.value);

    setFormIsValid(
      // valodate email includes @ and password length is more than 6
      event.target.value.trim().length > 6 && enteredEmail.includes("@")
    );
  };

  const validateEmailHandler = () => {
    setEmailIsValid(enteredEmail.includes("@"));
  };

  const validatePasswordHandler = () => {
    setPasswordIsValid(enteredPassword.trim().length > 6);
  };

  const submitHandler = (event) => {
    // page doesn't refresh on submit
    event.preventDefault();
    props.onLogin(enteredEmail, enteredPassword);
  };

  return (
    <div>
      <div className="container">
        <h4 className="center">Login</h4>
        <Card className="login">
          <form onSubmit={submitHandler}>
            <div
              className={`control ${emailIsValid === false ? "invalid" : ""}`}
            >
              <label htmlFor="email">E-Mail</label>
              <input
                type="email"
                id="email"
                value={enteredEmail}
                onChange={emailChangeHandler}
                onBlur={validateEmailHandler}
              />
            </div>
            <div
              className={`control ${
                passwordIsValid === false ? "invalid" : ""
              }`}
            >
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={enteredPassword}
                onChange={passwordChangeHandler}
                onBlur={validatePasswordHandler}
              />
            </div>
            <div className="actions">
              <Button type="submit" disabled={!formIsValid}>
                Login
              </Button>
            </div>
          </form>
        </Card>
      </div>
    </div>
  );
};

export default Login;
