import React, { useEffect, useState } from "react";
import TableBoard from "../UI/Table/TableBoard";
import TimeFilter from "./TimeFilter";
import axios from "axios";
import "./Flights.css"

const Flights = (props) => {
  const colNames = [
    "id",
    "airline",
    "origin country",
    "destination country",
    "departure time",
    "landing time",
    "remaining tickets",
  ];

  const [flights, setFlights] = useState([]);
  const [isReset, setIsReset] = useState(false);
  const [departureTime, setDeparturTime] = useState("");
  const [landingTime, setLandingTime] = useState("");

  useEffect(() => {
    axios.get(`http://localhost:8080/flights`).then((res) => {
      console.log(res.data.flights)
      setFlights(res.data.flights);
    });
  }, [isReset]);

  const resetFilterHandler = () => {
    setIsReset(!isReset);
    setDeparturTime("");
    setLandingTime("");
  };

  const departureFilterHandler = (departurTime) => {
    const d = new Date()
    console.log(d)
    setDeparturTime(departurTime);
  };

  const landingFilterHandler = (landingTime) => {
    setLandingTime(landingTime);
  };

  return (
    <React.Fragment>
      <div className="container__im">
        <br />
        <h3 className="center__headline">Flights Board</h3>
        <br />
        <button onClick={resetFilterHandler}>Reset Filter</button>
        <TimeFilter type="Departure" onChangeFilter={departureFilterHandler} />
        <TimeFilter type="Landing" onChangeFilter={landingFilterHandler} />
        <TableBoard list={flights} tableCol={colNames} />
      </div>
    </React.Fragment>
  );
};

export default Flights;
