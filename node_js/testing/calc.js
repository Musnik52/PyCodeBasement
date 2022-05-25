const calc = {};

calc.add = (num1, num2) => {
  return num1 + num2;
};

calc.multiply = (num1, num2) => {
  return num1 * num2;
};

calc.substract = (num1, num2) => {
  return num1 - num2;
};

calc.divide = (num1, num2) => {
  if (num2 == 0) {
    throw "Cannot divide by 0!";
  }
  return num1 / num2;
};

module.exports = calc;
