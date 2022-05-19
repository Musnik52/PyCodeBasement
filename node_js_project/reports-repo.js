const connectedKnex = require("./knex-connector");

function getAllReports() {
  return connectedKnex("reports").select("*");
}

function getReportByid(id) {
  return connectedKnex("reports").select("*").where("id", id).first();
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
  getRaw,
  addReport,
  updateReport,
  deleteReport,
};
