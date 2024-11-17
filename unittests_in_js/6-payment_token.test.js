const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise with the correct object when success is true', (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      // Assertions
      expect(response).to.be.an('object');
      expect(response).to.have.property('data', 'Successful response from the API');
      done(); // Notify Mocha that the test is complete
    }).catch((err) => done(err)); // Ensure done is called on error
  });
});
