const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const BASE_URL = 'http://localhost:7865';

  it('should return the correct status code', (done) => {
    request.get(`${BASE_URL}/`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', (done) => {
    request.get(`${BASE_URL}/`, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should handle unknown routes with a 404 status code', (done) => {
    request.get(`${BASE_URL}/unknown`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
