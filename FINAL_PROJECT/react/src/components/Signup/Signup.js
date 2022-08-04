import { useEffect, useState } from "react";
import SignupForm from "./SignupForm";
import Card from "../UI/Card/Card";
import axios from "axios"
import "./Signup.css";

const Signup = (props) => {
  const saveCustomerDataHandler = (enteredCustomerData) => {
    const customerData = {
      ...enteredCustomerData,
    };
    console.log(customerData);
    axios.post(`http://localhost:8080/customers`,customerData).then((res) => {
      console.log(res.data);
    });
  };

  return (
    <div className="mb-3">
      <br />
      <h3>Signup</h3>
      <Card className="signup">
        <SignupForm onSaveCustomerData={saveCustomerDataHandler} />
      </Card>
    </div>
  );
};

export default Signup;
