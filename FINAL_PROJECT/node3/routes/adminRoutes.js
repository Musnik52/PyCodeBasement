const { Router } = require("express");
const router = Router();
const {
  updateAirline,
  addFlight,
  deleteFlight,
  updateFlight,
} = require("../controllers/airlineController");
const {
  addCustomer,
  getAllFlights,
  getFlightById,
} = require("../controllers/anonymusController");
const {
  deleteCustomer,
  updateCustomer,
} = require("../controllers/customerController");
const {
  getAllCustomers,
  getCustomerById,
  getAllAdmins,
  getAdminById,
  deleteAdmin,
  updateAdmin,
  addAdmin,
  getAllAirlines,
  getAirlineById,
  deleteAirline,
  addAirline,
} = require("../controllers/adminController");

router
  .route("/airlines/:id")
  .get(getAirlineById)
  .delete(deleteAirline)
  .put(updateAirline);
router
  .route("/customers/:id")
  .get(getCustomerById)
  .delete(deleteCustomer)
  .put(updateCustomer);
router
  .route("/flights/:id")
  .get(getFlightById)
  .delete(deleteFlight)
  .put(updateFlight);
router.route("/airlines/").get(getAllAirlines).post(addAirline);
router.route("/customers/").get(getAllCustomers).post(addCustomer);
router.route("/flights/").get(getAllFlights).post(addFlight);
router.route("/:id").get(getAdminById).delete(deleteAdmin).put(updateAdmin);
router.route("/").get(getAllAdmins).post(addAdmin);

module.exports = router;
