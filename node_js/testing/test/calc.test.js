const calc = require("../calc");
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

describe("Test calculator basics with chai", () => {
  it("basic mul 3 * 4 == 12", () => {
    actual_result = calc.multiply(3, 4);
    expected_result = 12;
    expect(expected_result).to.equal(actual_result);
  });
  it("basic div 10 / 5 == 2", () => {
    actual_result = calc.divide(10, 5);
    expected_result = 2;
    expect(expected_result).to.equal(actual_result);
  });
  it("basic div 7 / 0 == ERROR", () => {
    expect(() => {
      calc.divide(7, 0);
    }).to.throw("Cannot divide by 0!");
    expected_result = 2;
    expect(expected_result).to.equal(actual_result);
  });
});

// test min - assert
// test div - equal

// npm test
