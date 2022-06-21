const airlock_repo = require("../airlock-repo");

module.exports.user_get = async (req, res) => {
  try {
    const users = await airlock_repo.getAll("users");
    res.status(201).json(users);
  } catch (err) {
    res.status(400).json({ err });
  }
};
