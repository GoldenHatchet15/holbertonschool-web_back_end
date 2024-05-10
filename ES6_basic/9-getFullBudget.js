import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {  // Simplified method syntax
      return `$${income}`;
    },
    getIncomeInEuros(income) {   // Simplified method syntax
      return `${income} euros`;
    },
  };

  return fullBudget;
}
