const request = require('request');
const { expect } = require('chai');
const app = require('./api');

describe('Index page', () => {
  let server;
  let port;

  before((done) => {
    server = app.listen(0, () => { // Use port 0 for a random available port
      port = server.address().port; // Get the assigned port
      console.log(`Server started on port ${port}`);
      done();
    });
  });

  after(() => {
    if (server) server.close();
  });

  it('should return the correct status code', (done) => {
    request.get(`http://localhost:${port}/`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', (done) => {
    request.get(`http://localhost:${port}/`, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should handle unknown routes with a 404 status code', (done) => {
    request.get(`http://localhost:${port}/unknown`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
