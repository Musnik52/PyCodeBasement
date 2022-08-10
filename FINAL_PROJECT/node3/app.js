const cors = require("cors");
const config = require("config");
const port = config.get("ports");
const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("./routes/authRoutes");
const cookieParser = require("cookie-parser");
const { logger } = require("./logger");
const adminRoutes = require("./routes/adminRoutes");
const flightRoutes = require("./routes/flightRoutes");
const airlineRoutes = require("./routes/airlineRoutes");
const customerRoutes = require("./routes/customerRoutes");
const anonymusController = require("./controllers/anonymusController");
const { requireAuth, checkUser } = require("./middleware/authMiddleware");

logger.debug("====== System startup ======");
const app = express();

// middleware
app.use(cors({ origin: "*" }));
app.use(express.static("public"));
app.use(express.json());
app.use(cookieParser());
app.use(express.urlencoded({ extended: false }));
app.use(authRoutes);
app.use("/admins", requireAuth, adminRoutes);
app.use("/flights", flightRoutes);
app.use("/airlines", requireAuth, airlineRoutes);
app.use("/customers", requireAuth, customerRoutes);

// Mongodb connection
const dbURI = config.get("mongo");
mongoose
  .connect(dbURI.conn_str, { useNewUrlParser: true, useUnifiedTopology: true })
  .then((result) => {
    console.log(result.connection);
    app.listen(port.listening, () =>
      logger.info(`Listening to http://localhost:${port.listening}`)
    );
  })
  .catch((err) => logger.info(err));

// // routes
app.get("*", checkUser);
app.get("/", (req, res) => res.status(200).render("index"));
