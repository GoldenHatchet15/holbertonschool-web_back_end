// 4-main.js
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const currency = new Currency("EUR", "Euro");
const pricing = new Pricing(100, currency);

console.log(pricing);
console.log(pricing.displayFullPrice());
