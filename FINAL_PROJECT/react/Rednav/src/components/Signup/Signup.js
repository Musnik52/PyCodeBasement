import SignupForm from "./SignupForm";
import Card from "../UI/Card/Card";
import "./Signup.css"

const Signup = (props) => {
  const saveCustomerDataHandler = (enteredCustomerData) => {
    const customerData = {
      ...enteredCustomerData,
      id: Math.random().toString(),
    };
    props.onAddCustomer(customerData);
    
  };

  return (
    <div>
      <div className="container">
        <h4 className="center">Signup</h4>
        <Card className="signup">
          <SignupForm
            onSaveCustomerData={saveCustomerDataHandler}
          />
        </Card>
      </div>
    </div>
  );
};

export default Signup;
