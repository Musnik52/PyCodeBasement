console.log(module);
console.log(__dirname);

const path = require('path')
console.log(path.join(__dirname, 'myfile.txt'));

const os = require('os');
console.log(`Free memory: ${os.freemem()}`);
console.log(`Total memory: ${os.totalmem()}`);
