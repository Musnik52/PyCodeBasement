import React, { useEffect, useState } from "react";
import Card from "../../UI/Card/Card";
import axios from "axios";
import Button from "../../UI/Button/Button";

const NewFlight = (props) => {
  const [myCountries, setMyCountries] = useState([]);
  const [enteredRemainingTickets, setEnteredRemainingTickets] = useState("");
  const [enteredDepartureTime, setEnteredDepartureTime] = useState("");
  const [enteredLandingTime, setEnteredLandingTime] = useState("");
  const [enteredOriginCountryId, setEnteredOriginCountryId] = useState("");
  const [enteredDestinationCountryId, setEnteredDestinationCountryId] =
    useState("");
  const [enteredAirlineId, setAirlineId] = useState("");

  useEffect(() => {
    axios
      .get(`http://localhost:8080/countries`)
      .then((res) => {
        setMyCountries(res.data.countries);
      })
      .catch((err) => console.log(err));
    axios
      .get(`http://localhost:8080/airlines/${props.username}`)
      .then((res) => {
        setAirlineId(res.data.airline.id);
      })
      .catch((err) => console.log(err));
  }, []);

  const originCountryIdHandler = (event) => {
    setEnteredOriginCountryId(event.target.value);
  };
  const destinationCountryIdHandler = (event) => {
    setEnteredDestinationCountryId(event.target.value);
  };
  const departurTimeIdHandler = (event) => {
    setEnteredDepartureTime(event.target.value);
  };
  const landingTimeHandler = (event) => {
    setEnteredLandingTime(event.target.value);
  };
  const remainingTicketsHandler = (event) => {
    setEnteredRemainingTickets(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const flightData = {
      username: props.username,
      password: props.pwd,
      airlineId: enteredAirlineId,
      originId: enteredOriginCountryId,
      destinationId: enteredDestinationCountryId,
      departurTime: enteredDepartureTime,
      landingTime: enteredLandingTime,
      remainingTickets: enteredRemainingTickets,
    };
    axios
      .post(
        `http://localhost:8080/airlines/flights/${props.username}`,
        flightData
      )
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  return (
    <React.Fragment>
      <Card className="">
        <h4 className="">New Flight</h4>
        <form>
          <div className="">
            <label className="control text-decoration-underline">
              Origin Country
            </label>
            <select
              className="form-select"
              aria-label="Default select example"
              onChange={originCountryIdHandler}
            >
              <option selected value={"*"}>
                Fly From
              </option>
              {myCountries.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
            <label className="control text-decoration-underline">
              Destination Country
            </label>
            <select
              className="form-select"
              aria-label="Default select example"
              onChange={destinationCountryIdHandler}
            >
              <option selected value={"*"}>
                Fly To
              </option>
              {myCountries.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
            <label className="control text-decoration-underline">
              Departure Time
            </label>
            <input
              className="control"
              type="datetime-local"
              onChange={departurTimeIdHandler}
            />
            <label className="control text-decoration-underline">
              Landing Time
            </label>
            <input
              className="control"
              type="datetime-local"
              onChange={landingTimeHandler}
            />
            <label className="control text-decoration-underline">
              Remaining Tickets
            </label>
            <input
              className="control"
              type="number"
              onChange={remainingTicketsHandler}
            />
            <Button onClick={submitHandler}>Add Flight</Button>
          </div>
        </form>
      </Card>
    </React.Fragment>
  );
};

export default NewFlight;
