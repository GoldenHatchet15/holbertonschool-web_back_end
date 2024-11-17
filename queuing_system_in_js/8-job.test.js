import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Enter test mode
    queue = kue.createQueue();
    kue.Job.queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the test queue and exit test mode
    kue.Job.queue.testMode.clear();
    kue.Job.queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(42, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check that two jobs were created
    expect(kue.Job.queue.testMode.jobs.length).to.equal(2);

    // Check job data
    expect(kue.Job.queue.testMode.jobs[0].type).to.equal(
      'push_notification_code_3'
    );
    expect(kue.Job.queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(kue.Job.queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});