import React, { useEffect, useState } from "react";
import axios from "axios";
import TableBoard from "../../UI/Table/TableBoard";
import Card from "../../UI/Card/Card";
import Button from "../../UI/Button/Button";

const MyFlights = (props) => {
  const colNames = [
    "flight id",
    "origin country",
    "destinamtion country",
    "departure time",
    "landing time",
    "remaining tickets",
  ];
  const [myFlights, setMyFlights] = useState([]);
  const [removeFlightId, setRemoveFlightId] = useState([]);
  useEffect(() => {
    axios
      .get(`http://localhost:8080/airlines/flights/${props.username}`)
      .then((res) => {
        setMyFlights(res.data.flights);
      });
  }, []);

  const removeFlightHandler = (event) => {
    setRemoveFlightId(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const flightData = {
      username: props.username,
      password: props.pwd,
      id: removeFlightId,
    };
    axios
      .delete(`http://localhost:8080/airlines/flights/${props.username}`, {
        data: { flightData },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  return (
    <React.Fragment>
      <div className="container">
        <h4 className="">My Flights</h4>
        <TableBoard list={myFlights} tableCol={colNames} />
        <Card className="">
          <form onSubmit={submitHandler}>
            <label className="text-decoration-underline">
              Select Flight # To Remove
            </label>
            <br />
            <br />
            <select
              aria-label="Default select example"
              onChange={removeFlightHandler}
            >
              {myFlights.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.id}
                </option>
              ))}
            </select>
            <Button className="control" type="submit">
              Remove Flight
            </Button>
          </form>
        </Card>
      </div>
    </React.Fragment>
  );
};

export default MyFlights;
