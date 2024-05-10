// 5-main.js
import Building from './5-building.js';

const b = new Building(100); // This will fail since Building should be abstract
console.log(b);

class TestBuilding extends Building {}

try {
    new TestBuilding(200); // This will also fail
}
catch(err) {
    console.log(err.message);
}
