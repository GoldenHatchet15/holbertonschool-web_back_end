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

describe('Cart page', () => {
  const BASE_URL = 'http://localhost:7865';

  it('should return the correct status code and message for a valid cart ID', (done) => {
    request.get(`${BASE_URL}/cart/12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return a 404 status code for an invalid cart ID', (done) => {
    request.get(`${BASE_URL}/cart/hello`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should return a 404 status code for missing cart ID', (done) => {
    request.get(`${BASE_URL}/cart/`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
