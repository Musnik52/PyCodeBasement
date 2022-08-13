const connectedKnex = require("../knex-connector");
const { logger } = require("../logger");

const updateAirline = async (req, res) => {
  const id = req.params.id;
  try {
    airline = req.body;
    const result = await connectedKnex("airline_companies")
      .where("id", id)
      .update(airline);
    res.status(200).json({
      res: "success",
      url: `/airlines/${id}`,
      result,
    });
  } catch (e) {
    logger.error(`failed to update airline. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const getMyFlights = async (req, res) => {
  const flights = await connectedKnex("flights")
    .select(
      "flights.id",
      "flights.airline_company_id",
      "countries.name",
      "flights.destination_country_id", //"countries.name as c2"
      "flights.departure_time",
      "flights.landing_time",
      "flights.remaining_tickets"
    )
    .where("airline_company_id", id)
    .orderBy("flights.id", "asc")
    .join("countries", function () {
      this.on("flights.origin_country_id", "=", "countries.id");
    });
  res.status(200).json({ flights });
};

const deleteFlight = async (req, res) => {
  const id = req.params.id;
  try {
    const flights = connectedKnex("flights").where("id", id).del();
    res.status(200).json({ num_records_deleted: flights });
  } catch (e) {
    logger.error(`failed to delete a flight. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const updateFlight = async (req, res) => {
  const id = req.params.id;
  try {
    flight = req.body;
    const result = await connectedKnex("flights")
      .where("id", id)
      .update(flight);
    res.status(200).json({
      res: "success",
      url: `/flights/${id}`,
      result,
    });
  } catch (e) {
    logger.error(`failed to update flight. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const addFlight = async (req, res) => {
  try {
    flight = req.body;
    const result = await connectedKnex("flights").insert(flight);
    res.status(201).json({
      res: "success",
      url: `/flights/${result[0]}`,
      result,
    });
  } catch (e) {
    logger.error(`failed to add a flight. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

module.exports = {
  getMyFlights,
  updateAirline,
  deleteFlight,
  updateFlight,
  addFlight,
};
