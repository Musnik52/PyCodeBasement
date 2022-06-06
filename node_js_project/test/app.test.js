const index = require("../app");
const assert = require("assert");
const expect = require("chai").expect;

describe("Test GET reports", () => {
  it("GET all reports", () => {
    actual_result = calc.add(1, 1);
    expected_result = 2;
    assert.strictEqual(actual_result, expected_result);
  });
  it("GET report by ID", () => {
    actual_result = calc.substract(4, 1);
    expected_result = 3;
    assert.strictEqual(actual_result, expected_result);
  });
  it("GET report by param", () => {
    actual_result = calc.substract(4, 1);
    expected_result = 3;
    assert.strictEqual(actual_result, expected_result);
  });
});
