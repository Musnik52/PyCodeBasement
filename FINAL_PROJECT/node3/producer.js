const amqp = require("amqplib");

async function connect(queue = "queue_name", msg = "message_to_be_sent") {
  const msgBuffer = Buffer.from(JSON.stringify({ queue: msg }));
  try {
    const connection = await amqp.connect("amqp://localhost:5672");
    const channel = await connection.createChannel();
    await channel.assertQueue(queue);
    await channel.sendToQueue(queue, msgBuffer);
    console.log(`Sending message to queue: ${queue}`);
    await channel.close();
    await connection.close();
  } catch (ex) {
    console.error(ex);
  }
}
connect();
