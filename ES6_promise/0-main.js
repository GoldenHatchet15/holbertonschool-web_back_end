#!/usr/bin/node
// This is the main file that will be used to test 
// the function getResponseFromAPI from 0-promise.js
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);  // This should log `true` to the console.
