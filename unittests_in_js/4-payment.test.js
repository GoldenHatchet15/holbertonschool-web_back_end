const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('should stub Utils.calculateNumber and spy on console.log', () => {
    // Stub Utils.calculateNumber to always return 10
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy on console.log
    const consoleLogSpy = sinon.spy(console, 'log');

    try {
      // Call the function
      sendPaymentRequestToApi(100, 20);

      // Verify the stub was called with the correct arguments
      expect(calculateNumberStub.calledOnce).to.be.true;
      expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;

      // Verify console.log was called with the correct message
      expect(consoleLogSpy.calledOnce).to.be.true;
      expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
    } finally {
      // Restore the stub and the spy
      calculateNumberStub.restore();
      consoleLogSpy.restore();
    }
  });
});
