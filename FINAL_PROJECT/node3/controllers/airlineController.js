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
    const airline = await connectedKnex("airline_companies")
      .select("*")
      .where("id", id)
      .first();
    const userDel = await connectedKnex("users")
      .where("id", customer.user_id)
      .del();
    const airlineDel = connectedKnex("airline_companies").where("id", id).del();
    res.status(200).json({ num_records_deleted: airlineDel });
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
    user = {
      username: req.body.username,
      password: req.body.password,
      email: req.body.email,
      user_role: 3,
    };
    const resultUser = await connectedKnex("users").insert(user);
    const newUser = await connectedKnex("users")
      .select("*")
      .where("username", req.body.username)
      .first();
    const resultAirline = await connectedKnex("airline_companies").insert({
      name: req.body.name,
      country_id: req.body.country_id,
      user_id: newUser.id,
    });
    res.status(201).json({
      res: "success",
      url: `/airlines/${resultAirline[0]}`,
      resultAirline,
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
