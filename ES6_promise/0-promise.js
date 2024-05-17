// 0-promise.js

export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        // Simulating an asynchronous operation
        setTimeout(() => {
            // You can add any condition here to resolve or reject the promise
            resolve("Success");
        }, 1000);
    });
}
