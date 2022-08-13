const { Router } = require("express");
const router = Router();
const {
  Sync,
  Login,
  Signup,
  addCustomer,
  getAllFlights,
  getFlightById,
} = require("../controllers/anonymusController");

router.route("/flights/:id").get(getFlightById);
router.route("/flights").get(getAllFlights);
router.route("/signup").post(Signup); // router.route("/").post(addCustomer);
router.route("/login").post(Login);
router.route("/sync").post(Sync);

module.exports = router;
