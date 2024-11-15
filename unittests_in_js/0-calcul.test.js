const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round and add two numbers correctly', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round both numbers and add them', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should handle rounding up for both numbers', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.4, -3.7), -5);
  });

  it('should handle a mix of positive and negative numbers', () => {
    assert.strictEqual(calculateNumber(1.4, -3.7), -3);
  });
});
