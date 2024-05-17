// 0-promise.js

/**
 * This function returns a promise that resolves immediately.
 * @return {Promise<void>} A promise that resolves without returning any value.
 */
export default function getResponseFromAPI () {
  return new Promise((resolve) => {
    resolve();
  });
}
