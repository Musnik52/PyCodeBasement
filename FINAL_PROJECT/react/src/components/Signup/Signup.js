import SignupForm from "./SignupForm";
import Card from "../UI/Card/Card";
import axios from "axios";
import "./Signup.css";

const Signup = (props) => {
  const saveCustomerDataHandler = async (enteredCustomerData) => {
    console.log(enteredCustomerData);
    axios
      .post("http://localhost:8080/customers", enteredCustomerData)
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
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
