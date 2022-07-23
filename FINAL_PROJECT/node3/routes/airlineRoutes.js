const { Router } = require("express");
const router = Router();
const {
  getAllAirlines,
  getAirlineById,
  deleteAirline,
  updateAirline,
  addAirline,
} = require("../controllers/airlineController");

const {
  getAllFlights,
  getFlightById,
  deleteFlight,
  updateFlight,
  addFlight,
} = require("../controllers/flightController");

router.route("/").get(getAllAirlines).post(addAirline);
router
  .route("/:id")
  .get(getAirlineById)
  .delete(deleteAirline)
  .put(updateAirline);

module.exports = router;
