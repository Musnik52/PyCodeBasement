import React, { useEffect, useState } from "react";
import TableBoard from "../UI/Table/TableBoard";
import TimeFilter from "./TimeFilter";
import axios from "axios";

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
  const [departureTime, setDeparturTime] = useState("");
  const [landingTime, setLandingTime] = useState("");
  const [isReset, setIsReset] = useState(false);

  useEffect(() => {
    axios.get(`http://localhost:8080/flights`).then((res) => {
      setFlights(res.data.flights);
    });
  }, [isReset]);

  const resetFilterHandler = () => {
    setIsReset(!isReset);
  };

  const departureFilterHandler = (departurTime) => {
    setDeparturTime(departurTime);
  };

  const landingFilterHandler = (landingTime) => {
    setLandingTime(landingTime);
  };

  return (
    <React.Fragment>
      <div className="container">
        <br />
        <h3>Flights Board</h3>
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
