const express = require('express')
const router = express.Router();
const path = require('path')
const url = require('url')
const cors = require('cors')
const port = 8088

const app = express();

app.use(express.static(path.join(__dirname, 'static')))

app.get('/', (req, resp) => {
    resp.writeHead(200);
    resp.end('This will be sent to the deafult url');
})
app.post('/banana', (req, resp) => {
    resp.writeHead(201);
    resp.end('new banana');
})
app.get('/page1', (req, resp) => {
    resp.sendFile(path.join(__dirname, 'page1.html'))
})
app.get('/add', (req, resp) => {
    // http://localhost:8088/add?x=4&y=3
    // http://localhost:8088/flights?origin=israel
    console.log(req.url)
    console.log(req.query)
    if (isNaN(Number(req.query.x))) {
        resp.writeHead(400);
        resp.end(`${req.query.x} is not a number`)
        return;
    }
    if (isNaN(Number(req.query.y))) {
        resp.writeHead(400);
        resp.end(`${req.query.y} is not a number`)
        return;
    }    
    const x = Number(req.query.x)
    const y = Number(req.query.y) 
    const sum = x + y
    resp.writeHead(200);
    resp.end(`${x} + ${y} = ${sum}`)
})

app.listen(port, () => console.log(`Listening to port ${port}`))
