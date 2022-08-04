const cors = require("cors");
const config = require("config");
const port = config.get("ports");
const express = require("express");
const mongoose = require("mongoose");
const { logger } = require("./logger");
const adminRoutes = require("./routes/adminRoutes");
const flightRoutes = require("./routes/flightRoutes");
const airlineRoutes = require("./routes/airlineRoutes");
const customerRoutes = require("./routes/customerRoutes");
const anonymusController = require("./controllers/anonymusController");

logger.debug("====== System startup ======");
const app = express();

// middleware
app.use(cors());
app.use(express.static("public"));
app.use(express.urlencoded({ extended: false }));
app.use("/admins", adminRoutes);
app.use("/flights", flightRoutes);
app.use("/airlines", airlineRoutes);
app.use("/customers", customerRoutes);

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
app.get("/", (req, res) => res.status(200).render("index"));
