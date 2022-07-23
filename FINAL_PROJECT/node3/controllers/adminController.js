const connectedKnex = require("../knex-connector");
const { logger } = require("../logger");

const getAllAdmins = async (req, res) => {
  const admins = await connectedKnex("administrators").select("*");
  res.status(200).json({ admins });
};

const getAdminById = async (req, res) => {
  const id = req.params.id;
  const admin = await connectedKnex("administrators")
    .select("*")
    .where("id", id)
    .first();
  res.status(200).json({ admin });
};

const deleteAdmin = async (req, res) => {
  const id = req.params.id;
  try {
    const admin = connectedKnex("administrators").where("id", id).del();
    res.status(200).json({ num_records_deleted: admin });
  } catch (e) {
    logger.error(`failed to delete an admin. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const updateAdmin = async (req, res) => {
  const id = req.params.id;
  try {
    admin = req.body;
    const result = await connectedKnex("administrators")
      .where("id", id)
      .update(admin);
    res.status(200).json({
      res: "success",
      url: `/admins/${id}`,
      result,
    });
  } catch (e) {
    logger.error(`failed to update admin. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

const addAdmin = async (req, res) => {
  try {
    admin = req.body;
    const result = await connectedKnex("administrators").insert(admin);
    res.status(201).json({
      res: "success",
      url: `/admins/${result[0]}`,
      result,
    });
  } catch (e) {
    logger.error(`failed to add an admin. Error: ${e}`);
    res.status(400).send({
      status: "error",
      message: e.message,
    });
  }
};

module.exports = {
  getAllAdmins,
  getAdminById,
  deleteAdmin,
  updateAdmin,
  addAdmin,
};
