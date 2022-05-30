const index = require("../index");
const assert = require("assert");
const expect = require("chai").expect;

describe("Test calculator basics", () => {
  it("basic add 1 + 1 == 2", () => {
    actual_result = calc.add(1, 1);
    expected_result = 2;
    assert.strictEqual(actual_result, expected_result);
  });
  it("basic sub 4 - 1 == 3", () => {
    actual_result = calc.substract(4, 1);
    expected_result = 3;
    assert.strictEqual(actual_result, expected_result);
  });
});
