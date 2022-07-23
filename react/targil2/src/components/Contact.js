import React from "react";

const Contact = (props) => {
  console.log(props);
  console.log(props.history.length);
  //setTimeout(() => {
  //props.history.push('/about')
  //}, 3000)
  return (
    <div>
      <div className="container">
        <h4 className="center">Contact</h4>
        <p>3...2...1... about</p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda in
          voluptas dolorem recusandae quae expedita similique nobis neque
          accusamus, architecto suscipit saepe odio aliquam nostrum ducimus
          laborum esse optio voluptate.
        </p>
      </div>
    </div>
  );
};

export default Contact;
