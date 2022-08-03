import React from "react";
import Card from "../UI/Card/Card";
import "./About.css";
import airlock_logo from "../../Assets/airlock.png";

const About = (props) => {
  console.log(props);
  return (
    <div>
      <div className="container">
        <br />
        <h4 className="center">About</h4>
        <span className="text-decoration-underline">
          Our Company, Airlock, was founded by Boris Group LTD in 2022. <br />
          Ever since its inception, Airlock managged to book a flight for every
          single customer.
        </span>
        <br /> <br />
        <Card className="achievements">
          <ul className="list-group list-group-flush">
            <li className="list-group-item active" aria-current="true">
              Among our numerous achievements are:
            </li>
            <li className="list-group-item list-group-item-action">
              Solving world hunger.
            </li><li className="list-group-item list-group-item-action">
            Deviding by 0.
          </li>
          <li className="list-group-item list-group-item-action">
              Understanding the movie "Matrix" on the first watch.
            </li>
            <li className="list-group-item list-group-item-action">
              Bringing equal rights to 9.9 billion people.
            </li>
            <li className="list-group-item list-group-item-action">
              Finding Waldo.
            </li>
            <li className="list-group-item list-group-item-action">
              Counting to infinity. Twice!.
            </li>
          </ul>
          <img className="" src={airlock_logo} />
        </Card>
      </div>
    </div>
  );
};

export default About;
