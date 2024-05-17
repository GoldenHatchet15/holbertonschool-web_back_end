#!/usr/bin/node
/**
 * Returns a new Promise that resolves immediately.
 * 
 * @return {Promise<any>} A promise that resolves with no value.
 */
function getResponseFromAPI() {
    return new Promise((resolve) => {
      // You can resolve immediately since no specific asynchronous task is mentioned.
      resolve();
    });
  }
  
  export default getResponseFromAPI;
  