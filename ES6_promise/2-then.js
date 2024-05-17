// 0-promise.js

/**
 * This function returns a new Promise that resolves immediately.
 * @returns {Promise<void>} A promise that resolves with no value.
 */
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        // This promise resolves immediately. You can modify the behavior as needed.
        resolve();
    });
}

export default getResponseFromAPI;
