function createPushNotificationsJobs(jobs, queue) {
    // Check if jobs is an array
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    // Iterate through the jobs array
    jobs.forEach((jobData) => {
      // Create a job in the queue
      const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
          if (err) {
            console.error(`Notification job failed to create: ${err}`);
          } else {
            console.log(`Notification job created: ${job.id}`);
          }
        });
  
      // Event listeners for job progress, completion, and failure
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
  
      job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
  
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  }
  
  export default createPushNotificationsJobs;
  