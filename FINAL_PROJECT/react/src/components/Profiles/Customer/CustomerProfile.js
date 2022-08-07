import React from "react";
import Card from "../../UI/Card/Card";
import customer_pic from "../../../Assets/customer_pic.jpg";

const CustomerProfile = (props) => {
  return (
    <React.Fragment>
      <Card className="">
        <h4 className="">Welcome, {props.login_name}</h4>
        <img src={customer_pic} alt="customer" />
        <br />
        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" class="btn btn-secondary">
            Left
          </button>
          <button type="button" class="btn btn-secondary">
            Middle
          </button>
          <button type="button" class="btn btn-secondary">
            Right
          </button>
        </div>
      </Card>
    </React.Fragment>
  );
};

export default CustomerProfile;
