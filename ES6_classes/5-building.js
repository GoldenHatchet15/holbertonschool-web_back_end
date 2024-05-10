// 5-building.js

export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error('Cannot instantiate from abstract class Building');
    }
    if (this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }
}
