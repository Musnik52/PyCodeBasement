const url = 'http://mylogger.io/log';

function log(message) {
    console.log(`Logging: ${message}`)
}


module.exports.log = log
module.exports.end_point = url

console.log(module)
