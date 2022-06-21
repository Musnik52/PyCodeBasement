const { Router } = require("express");
const authController = require("../controllers/authController");
const exportController = require("../controllers/exportController");

const router = Router();

router.get("/signup", authController.signup_get);
router.post("/signup", authController.signup_post);
router.get("/login", authController.login_get);
router.post("/login", authController.login_post);
router.get("/logout", authController.logout_get);
router.get("/export", exportController.user_get);

module.exports = router;
