console.log('Hello world!');

let x = 1;

console.log(`x = ${x + 1}`);
const readline = require('readline').createInterface({
    input: process.stdin, 
    output: process.stdout
});

readline.question('Who are you? ', name => {
    console.log(`hello ${name}`)
    readline.close();
});
