// 0-promise.js

/**
 * Returns a promise that either resolves or rejects based on a condition.
 * @return {Promise<string>} A promise that might resolve with a success message or reject with an error.
 */
export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      const success = true; // Simulate success or failure
      if (success) {
        resolve("Success: Data fetched successfully");
      } else {
        reject(new Error("Failure: Unable to fetch data"));
      }
    });
  }
  