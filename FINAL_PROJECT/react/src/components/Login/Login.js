import React, { useState } from "react";
import Card from "../UI/Card/Card";
import Button from "../UI/Button/Button";
import "./Login.css";

const Login = (props) => {
  const [enteredUsername, setEnteredUsername] = useState("");
  const [usernameIsValid, setUsernameIsValid] = useState();
  const [enteredPassword, setEnteredPassword] = useState("");
  const [passwordIsValid, setPasswordIsValid] = useState();
  const [enteredRole, setEnteredRole] = useState("customer");
  const [formIsValid, setFormIsValid] = useState(false);

  const usernameChangeHandler = (event) => {
    setEnteredUsername(event.target.value);
    setFormIsValid(enteredPassword.trim().length > 6);
  };

  const passwordChangeHandler = (event) => {
    setEnteredPassword(event.target.value);
    setFormIsValid(event.target.value.trim().length > 6);
  };

  const roleChangeHandler = (event) => {
    setEnteredRole(event.target.value);
  };

  const validateUsernameHandler = () => {
    setUsernameIsValid(enteredUsername.length > 3);
  };

  const validatePasswordHandler = () => {
    setPasswordIsValid(enteredPassword.trim().length > 6);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const loginData = {
      username: enteredUsername,
      password: enteredPassword,
      role: enteredRole,
    };
    console.log(loginData);
    // RABBITMQ HERE TO LOGIN
    props.onLogin(enteredUsername, enteredPassword);
  };

  return (
    <React.Fragment>
      <div className="container">
        <br />
        <h3 className="center">Login</h3>
        <Card className="login">
          <form onSubmit={submitHandler}>
            <div
              className={`control ${
                usernameIsValid === false ? "invalid" : ""
              }`}
            >
              <label calssName="control" htmlFor="text">
                Username{" "}
              </label>
              <input
                calssName="control"
                type="text"
                id="text"
                value={enteredUsername}
                onChange={usernameChangeHandler}
                onBlur={validateUsernameHandler}
              />
            </div>
            <div
              className={`control ${
                passwordIsValid === false ? "invalid" : ""
              }`}
            >
              <br />
              <label calssName="control" htmlFor="password">
                Password{" "}
              </label>
              <input
                calssName="control"
                type="password"
                id="password"
                value={enteredPassword}
                onChange={passwordChangeHandler}
                onBlur={validatePasswordHandler}
              />
            </div>
            <div calssName="control">
              <label calssName="control">Sign in as:</label>
              <select
                className="form-select"
                id="floatingSelect"
                aria-label="Floating label select example"
                onChange={roleChangeHandler}
              >
                <option defaultValue value="customer">
                  A Customer
                </option>
                <option value="airline">An Airport Company</option>
                <option value="admin">An Admin</option>
              </select>
            </div>
            <div className="actions">
              <br />
              <Button type="submit" disabled={!formIsValid}>
                Login
              </Button>
            </div>
            <p>
              {" "}
              Don't have an account? <br />
              <span className="line">
                <a href="/signup">Sign up</a>
              </span>
            </p>
          </form>
        </Card>
      </div>
    </React.Fragment>
  );
};

export default Login;
