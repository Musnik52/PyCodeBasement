const EventEmitter = require('events')
const event_new_customer = new EventEmitter();

event_new_customer.on('new_customer', cust_name => {
    console.log(`New customer ${cust_name} has arrived. write to db`);
})

event_new_customer.on('new_customer', cust_name => {
    console.log(`New customer ${cust_name} has arrived. write to Logger`);
})

event_new_customer.on('new_order', cust_name => {
    console.log(`New order for ${cust_name} has arrived. write to Logger`);
})

event_new_customer.emit('new_customer', 'moshe');
event_new_customer.emit('new_order', 'moshe');
