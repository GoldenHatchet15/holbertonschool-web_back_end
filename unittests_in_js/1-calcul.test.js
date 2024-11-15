const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return the sum of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should handle negative numbers', () => {
      assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5);
    });
  });

  describe('SUBTRACT', () => {
    it('should return the difference of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should handle negative numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });
  });

  describe('DIVIDE', () => {
    it('should return the division of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing by 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should handle negative numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', -1.4, -4.5), 0.25);
    });
  });

  describe('Invalid type', () => {
    it('should throw an error for invalid operation type', () => {
      assert.throws(() => calculateNumber('INVALID', 1.4, 4.5), Error);
    });
  });
});
