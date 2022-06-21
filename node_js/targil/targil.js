const EventEmitter = require("events");
const divide_event = new EventEmitter();
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

divide_event.on("zero_divide", (num1) => {
  console.log(`Can't devide ${num1} by 0.`);
});

divide_event.on("can_divide", (numbers) => {
  console.log(
    `${numbers[0]} divided by ${numbers[1]} is: ${numbers[0] / numbers[1]}`
  );
});

readline.question("Enter nominator: ", (num1) => {
  readline.question("Enter denominator: ", (num2) => {
    if (num2 == 0) {
      divide_event.emit("zero_divide", `${num1}`);
    } else {
      divide_event.emit("can_divide", [num1, num2]);
    }
    readline.close();
  });
});
