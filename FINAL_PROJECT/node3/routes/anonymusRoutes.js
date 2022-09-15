const { Router } = require("express");
const router = Router();
const {
  Logout,
  Login,
  // LoginCheck,
  addCustomer,
  getAllFlights,
  getFlightById,
  getAllCountries,
  getFlightByCountries,
} = require("../controllers/anonymusController");

router.route("/flights/:origin/:destination").get(getFlightByCountries);
router.route("/flights/:id").get(getFlightById);
router.route("/countries").get(getAllCountries);
router.route("/flights").get(getAllFlights);
router.route("/login").post(Login)//.get(LoginCheck);
router.route("/logout").get(Logout);
router.route("/").post(addCustomer);

module.exports = router;
