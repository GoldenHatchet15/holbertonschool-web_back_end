// 9-main.js
import getFullBudgetObject from './9-getFullBudget.js';

const fullBudget = getFullBudgetObject(20, 50, 10);

console.log(fullBudget.getIncomeInDollars(fullBudget.income)); // Should print "$20"
console.log(fullBudget.getIncomeInEuros(fullBudget.income));   // Should print "20 euros"
