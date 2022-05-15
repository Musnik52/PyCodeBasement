
const { logger } = require('./logger')
const sqlite3 = require('sqlite3').verbose()

logger.debug('====== System startup ========')

const db = new sqlite3.Database('db1.db', err => {
    if (err) {
        logger.error(`cannot connect to db. Error: ${err}`)
        return;
    }
    console.log('Connected ....')
    db.serialize( () => {
        db.each(`SELECT * FROM PRODUCTS`, (_err, row) => {
            if (_err) {
                logger.error(`cannot connect to db. Error: ${err}`)
                return;
            }            
            console.table(row)
        })
    })
})
db.close((err) => {
    if (err) {
        logger.error(`cannot close db. Error: ${err}`)
        return;
    }
    console.log('DB closed ....')
})





