const airlock_repo = require("./airlock-repo");

async function syncData() {
  try {
    const users = await airlock_repo.getAll("users");
    //update mongo
    console.log(users);
    return {};
  } catch (err) {
    return err;
  }
}

module.exports = {
  syncData,
};
