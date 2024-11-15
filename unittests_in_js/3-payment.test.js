const sinon = require('sinon');
const chai = require('chai'); // Import chai
const expect = chai.expect; // Explicitly define expect
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should use Utils.calculateNumber to calculate the total', () => {
    // Create a spy on Utils.calculateNumber
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    try {
      // Call the function
      sendPaymentRequestToApi(100, 20);

      // Assert that the spy was called with the correct arguments
      expect(calculateNumberSpy.calledOnce).to.be.true;
      expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;
    } finally {
      // Restore the spy
      calculateNumberSpy.restore();
    }
  });
});
