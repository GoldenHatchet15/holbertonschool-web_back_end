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

describe('/available_payments endpoint', () => {
  const BASE_URL = 'http://localhost:7865';

  it('should return the correct payment methods', (done) => {
    request.get(`${BASE_URL}/available_payments`, { json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('/login endpoint', () => {
  const BASE_URL = 'http://localhost:7865';

  it('should return a welcome message for a valid userName', (done) => {
    request.post(
      `${BASE_URL}/login`,
      {
        json: { userName: 'Betty' },
      },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });

  it('should return a 400 status code for missing userName', (done) => {
    request.post(`${BASE_URL}/login`, { json: {} }, (err, res, body) => {
      expect(res.statusCode).to.equal(400);
      expect(body).to.equal('Missing userName');
      done();
    });
  });
});
