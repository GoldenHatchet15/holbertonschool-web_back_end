// 10-car.js

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Method to clone the car
  cloneCar() {
    // Create a new instance of the same class without calling constructor
    const newCar = Object.create(this.constructor.prototype);

    // Optionally initialize any properties you want or leave it to the user to set them
    return newCar;
  }
}
