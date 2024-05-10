export default function appendToEachArrayValue(array, appendString) {
    let newArray = []; // Use let to declare a new array to store modified values
    for (const value of array) { // Using for...of for iterating through array values directly
      newArray.push(appendString + value); // Append the string and push to the new array
    }
  
    return newArray; // Return the new array to avoid mutating the original array
  }
  