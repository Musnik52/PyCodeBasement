const amqp = require("amqplib");

async function connect(queue = "queue_name") {
  try {
    const connection = await amqp.connect("amqp://localhost:5672");
    const channel = await connection.createChannel();
    await channel.assertQueue(queue);
    channel.consume(queue, (message) => {
      const input = JSON.parse(message.content.toString());
      console.log(`Received from ${queue}: ${input.queue}`);
      channel.ack(message);
    });
    console.log(`Waiting for messages...`);
  } catch (ex) {
    console.error(ex);
  }
}
connect();
