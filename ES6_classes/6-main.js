// 6-main.js
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);                     // Outputs: 140
console.log(building.floors);                   // Outputs: 60
console.log(building.evacuationWarningMessage()); // Outputs: Evacuate slowly the 60 floors
