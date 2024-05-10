// Importing the ClassRoom class
import ClassRoom from './0-classroom';

function initializeRooms() {
  // Create an array of ClassRoom instances with specified sizes
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}

// Exporting the initializeRooms function
export default initializeRooms;
