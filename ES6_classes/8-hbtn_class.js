// 8-hbtn_class.js

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Getter for size
  get size() {
    return this._size;
  }

  // Getter for location
  get location() {
    return this._location;
  }

  // Method to cast class to a Number
  valueOf() {
    return this._size;
  }

  // Method to cast class to a String
  toString() {
    return this._location;
  }
}
