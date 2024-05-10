// 7-main.js
import Airport from "./7-airport.js";

const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);        // Should use the custom toString implicitly
console.log(airportSF.toString()); // Explicit call to toString method
