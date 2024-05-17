// 1-promise.js

/**
 * This function returns a promise that resolves or rejects based on the input boolean.
 * @param {boolean} success - Determines whether the promise should resolve or reject.
 * @returns {Promise<Object|Error>} A promise that resolves with an object if true, or rejects with an Error if false.
 */
function getFullResponseFromAPI(success) {
    return new Promise((resolve, reject) => {
        if (success) {
            resolve({
                status: 200,
                body: 'Success'
            });
        } else {
            reject(new Error('The fake API is not working currently'));
        }
    });
}

export default getFullResponseFromAPI;
