import React, { useEffect, useState } from "react";
import axios from "axios";
import TableBoard from "../../UI/Table/TableBoard";
import Card from "../../UI/Card/Card";
import FlightForm from "./FlightForm";
import RemoveForm from "./RemoveForm";

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
  const [updateFlightId, setUpdateFlightId] = useState("");
  const [isUpdateAction, setIsUpdateAction] = useState(false);
  const [isRemoveAction, setIsRemoveAction] = useState(false);
  const [isReturnAction, setIsReturnAction] = useState(true);

  useEffect(() => {
    axios
      .get(`http://localhost:8080/airlines/flights/${props.username}`)
      .then((res) => {
        setMyFlights(res.data.flights);
      });
  }, []);

  const updateFlightHandler = (event) => {
    setUpdateFlightId(event.target.value);
    console.log(updateFlightId);
  };

  const updateActionHandler = (event) => {
    setIsRemoveAction(false);
    setIsReturnAction(false);
    setIsUpdateAction(true);
  };

  const removeActionHandler = (event) => {
    setIsUpdateAction(false);
    setIsReturnAction(false);
    setIsRemoveAction(true);
  };

  const returnActionHandler = (event) => {
    setIsUpdateAction(false);
    setIsRemoveAction(false);
    setIsReturnAction(true);
  };

  const submitRemoveHandler = (flightData) => {
    axios
      .delete(`http://localhost:8080/airlines/flights/${props.username}`, {
        data: { flightData },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  const submitUpdateHandler = (flightData) => {
    const sentFlightData = {
      ...flightData,
      flightId: updateFlightId,
    };
    axios
      .put(
        `http://localhost:8080/airlines/flights/${props.username}`,
        sentFlightData
      )
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
        {!isReturnAction && (
          <button
            className="btn btn-outline-info"
            onClick={returnActionHandler}
          >
            Return
          </button>
        )}
        <Card className="">
          {isReturnAction && (
            <button className="btn btn-danger" onClick={removeActionHandler}>
              Remove a Flight
            </button>
          )}
          {isReturnAction && <br />}
          {isReturnAction && (
            <button className="btn btn-success" onClick={updateActionHandler}>
              Update a Flight
            </button>
          )}
          {isRemoveAction && (
            <RemoveForm
            myFlights={myFlights}
              username={props.username}
              pwd={props.pwd}
              onSubmit={submitRemoveHandler}
            />
          )}
          {isUpdateAction && (
            <div className="">
              <label className="text-decoration-underline">
                Select Flight # To Update
              </label>
              <br />
              <br />
              <select
                aria-label="Default select example"
                onChange={updateFlightHandler}
              >
                <option selected value={"0"} />
                {myFlights.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.id}
                  </option>
                ))}
              </select>
              <FlightForm
                username={props.username}
                pwd={props.pwd}
                onSubmit={submitUpdateHandler}
              />
            </div>
          )}
        </Card>
      </div>
    </React.Fragment>
  );
};

export default MyFlights;
