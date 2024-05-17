// 0-promise.js

/**
 * Simulates an API call and returns a promise that resolves after a short delay.
 * @return {Promise<string>} A promise that resolves with a message.
 */
export default function getResponseFromAPI() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("Success: API response received");
      }, 1000); // Simulates a delay of 1000 milliseconds (1 second)
    });
  }
  