const { Router } = require("express");
const router = Router();
const {
  getAllFlights,
  getFlightById,
  deleteFlight,
  updateFlight,
  addFlight,
} = require("../controllers/flightController");
const {
  getAllCustomers,
  getCustomerById,
  deleteCustomer,
  updateCustomer,
  addCustomer,
} = require("../controllers/customerController");
const {
  getAllAdmins,
  getAdminById,
  deleteAdmin,
  updateAdmin,
  addAdmin,
} = require("../controllers/adminController");

router.route("/").get(getAllAdmins).post(addAdmin);
router.route("/:id").get(getAdminById).delete(deleteAdmin).put(updateAdmin);

module.exports = router;
