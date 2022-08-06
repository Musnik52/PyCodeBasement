const connectedKnex = require("../knex-connector");
const { logger } = require("../logger");
const { sendMsg } = require("../producer");
const { recieveMsg } = require("../consumer");
const uuid = require("uuid");

const Login = (req, res) => {
    try {
        const username = req.body.username
        const password = req.body.password
        const user = connectedKnex("users").select("*").where("username", username).first();
        console.log(user)
        console.log(user.password)
    } catch (err) {
        logger.error(err)
    }
};

module.exports = {
  Login,
};
