import React from "react";
import FlightBoard from "./FlightBoard";

const Flights = (props) => {
  const columns = [
    "airline",
    "origin country",
    "destination country",
    "departure time",
    "landing time",
    "remaining tickets",
  ];
  const flights = [
    {
      airline_company_id: 1,
      origin_country_id: 2,
      destination_country_id: 3,
      departure_time: "10:15",
      landing_time: "11:11",
      remaining_tickets: 22,
    },
    {
      airline_company_id: 2,
      origin_country_id: 3,
      destination_country_id: 4,
      departure_time: "14:32",
      landing_time: "20:22",
      remaining_tickets: 22,
    },
  ];
  return (
    <React.Fragment>
      <div className="container">
        <br />
        <h4 className="center">Flights Board</h4>
        <FlightBoard list={flights} colNames={columns} />
      </div>
    </React.Fragment>
  );
};

export default Flights;
