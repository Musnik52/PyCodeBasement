const connectedKnex = require("../knex-connector");
const { logger } = require("../logger");

const getAllAirlines = async (req, res) => {
  const airlines = await connectedKnex("airline_companies").select("*");
  res.status(200).json({ airlines });
};

const getAirlineById = async (req, res) => {
  const id = req.params.id;
  const airline = await connectedKnex("airline_companies")
    .select("*")
    .where("id", id)
    .first();
  res.status(200).json({ airline });
};

const deleteAirline = async (req, res) => {
  const id = req.params.id;
  try {
    const airline = connectedKnex("airline_companies").where("id", id).del();
    res.status(200).json({ num_records_deleted: airline });
  } catch (e) {
    logger.error(`failed to delete an airline. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

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

const addAirline = async (req, res) => {
    try {
      airline = req.body;
      const result = await connectedKnex("airline_companies").insert(airline);
      res.status(201).json({
        res: "success",
        url: `/airlines/${result[0]}`,
        result,
      });
    } catch (e) {
      logger.error(`failed to add an airline. Error: ${e}`);
      res.status(400).send({
        status: "error",
        message: e.message,
      });
    }
  };

module.exports = {
  getAllAirlines,
  getAirlineById,
  deleteAirline,
  updateAirline,
  addAirline,
};
