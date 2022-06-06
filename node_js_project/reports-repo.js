const connectedKnex = require("./knex-connector");

function getAllReports() {
  return connectedKnex("reports").select("*");
}

function getReportByid(id) {
  return connectedKnex("reports").select("*").where("id", id).first();
}

function getReportByParams(license_plate, driver_id, speed) {
  if (license_plate | driver_id | speed) {
    return connectedKnex("reports")
      .select("*")
      .where("license_plate", license_plate)
      .orWhere("driver_id", driver_id)
      .orWhere("speed", speed);
  } else {
    return connectedKnex("reports").select("*");
  }
}

function getRaw(query) {
  return connectedKnex.raw(query);
}

function addReport(report) {
  return connectedKnex("reports").insert(report);
}

function updateReport(report, id) {
  return connectedKnex("reports").where("id", id).update(report);
}

function deleteReport(id) {
  return connectedKnex("reports").where("id", id).del();
}

module.exports = {
  getAllReports,
  getReportByid,
  getReportByParams,
  getRaw,
  addReport,
  updateReport,
  deleteReport,
};
