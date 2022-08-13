const connectedKnex = require("../knex-connector");
const { logger } = require("../logger");
const { sendMsg } = require("../producer");
const { recieveMsg } = require("../consumer");
const uuid = require("uuid");
const User = require("../models/User");
const jwt = require("jsonwebtoken");

// handle errors
const handleErrors = (err) => {
  console.log(err.message, err.code);
  let errors = { username: "", password: "" };

  // incorrect username
  if (err.message === "incorrect username") {
    errors.username = "That username is not registered";
  }

  // incorrect password
  if (err.message === "incorrect password") {
    errors.password = "That password is incorrect";
  }

  // duplicate username error
  if (err.code === 11000) {
    errors.username = "that username is already registered";
    return errors;
  }

  // validation errors
  if (err.message.includes("user validation failed")) {
    Object.values(err.errors).forEach(({ properties }) => {
      errors[properties.path] = properties.message;
    });
  }
  return errors;
};

// create json web token
const maxAge = 3 * 24 * 60 * 60;
const createToken = (id) => {
  return jwt.sign({ id }, "secret key", {
    expiresIn: maxAge,
  });
};

const Login = async (req, res) => {
    const { username, password } = req.body;
  
    try {
      const user = await User.login(username, password);
      const token = createToken(user._id);
      res.cookie("jwt", token, { httpOnly: true, maxAge: maxAge * 1000 });
      res.status(200).json({ user: user.username, role: user.role });
    } catch (err) {
      const errors = handleErrors(err);
      res.status(400).json({ errors });
    }
  };
  
//   const logout = (req, res) => {
//     res.cookie("jwt", "", { maxAge: 1 });
//     res.redirect("/");
//   };

// const Login = (req, res) => {
//   try {
//     const username = req.body.username;
//     const password = req.body.password;
//     const user = connectedKnex("users")
//       .select("*")
//       .where("username", username)
//       .first();
//     console.log(user);
//     console.log(user.password);
//   } catch (err) {
//     logger.error(err);
//   }
// };

const Signup = async (req, res) => {
  const { username, password, email, publicId, role } = req.body;
  try {
    const user = await User.create({
      username,
      password,
      email,
      publicId,
      role,
    });
    const token = createToken(user._id);
    res.cookie("jwt", token, { httpOnly: true, maxAge: maxAge * 1000 });
    res
      .status(201)
      .json({ id: user._id, user: user.username, role: user.role });
  } catch (err) {
    const errors = handleErrors(err);
    res.status(400).json({ errors });
  }
};

const addCustomer = async (req, res) => {
  const qResName = `customer ${uuid.v4()}`;
  try {
    reqMsg = {
      action: "add",
      username: req.body.username,
      password: req.body.password,
      email: req.body.email,
      first_name: req.body.firstName,
      last_name: req.body.lastName,
      address: req.body.address,
      phone_number: req.body.phone,
      credit_card_number: req.body.ccn,
      queue_name: `response ${qResName}`,
    };
    recieveMsg(reqMsg.queue_name, res);
    await sendMsg("customer", reqMsg);
  } catch (e) {
    logger.error(`failed to add a customer. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const getAllFlights = async (req, res) => {
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
    .orderBy("flights.id", "asc")
    .join("countries", function () {
      this.on("flights.origin_country_id", "=", "countries.id");
    });
  res.status(200).json({ flights });
};

const getFlightById = async (req, res) => {
  const id = req.params.id;
  const flight = await connectedKnex("flights")
    .select("*")
    .where("id", id)
    .first();
  res.status(200).json({ flight });
};

module.exports = {
  Login,
  Signup,
  addCustomer,
  getAllFlights,
  getFlightById,
};
