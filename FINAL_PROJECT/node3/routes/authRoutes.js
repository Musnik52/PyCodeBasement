const { Router } = require("express");
const authController = require("../controllers/authController");

const router = Router();

router.route("/signup").post(authController.signup_post);
router.route("/login").post(authController.login_post);
router.route("/logout").get(authController.logout_get);

module.exports = router;
