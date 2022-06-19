const airlock_repo = require("./airlock-repo");

async function myFunction() {
  try {
    const users = await airlock_repo.getAll("users");
    //update mongo
    return document.getElementById("demo").innerHTML = users[1];
  } catch (err) {
    return document.getElementById("demo").innerHTML = err;
  }
}

module.exports = {
  myFunction,
};
