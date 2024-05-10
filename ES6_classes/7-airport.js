// 7-airport.js

export default class Airport {
    constructor(name, code) {
      this._name = name;
      this._code = code;
    }
  
    // Getter for name
    get name() {
      return this._name;
    }
  
    // Getter for code
    get code() {
      return this._code;
    }
  
    // Customize the default string representation
    toString() {
      return `[object ${this.code}]`;
    }
  }
  