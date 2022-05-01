
const logger = require('./logger')
logger.log('what did we import?')
console.log(logger);
const fs = require('fs')
const files = fs.readdirSync('./')
console.log(files);

fs.readdir(__dirname + '____________', (err, files) => {
    if (err)
        logger.log(`[async] Error ${err}`);
    else {
        console.log(`[async] Files: `);
        console.log(files);
    }
})

//console.log(module);