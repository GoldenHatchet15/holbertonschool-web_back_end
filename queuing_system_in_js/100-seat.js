import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

// Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize available seats and reservation status
const initialAvailableSeats = 50;
let reservationEnabled = true;

// Kue queue
const queue = kue.createQueue();

// Function to set available seats in Redis
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get the current available seats from Redis
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats !== null ? parseInt(seats, 10) : null;
}

// Set initial available seats
reserveSeat(initialAvailableSeats);

// Express App
const app = express();
const port = 1245;

// Route: GET /available_seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

// Route: GET /reserve_seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route: GET /process
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();

    if (seats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    await reserveSeat(seats - 1);

    if (seats - 1 === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
