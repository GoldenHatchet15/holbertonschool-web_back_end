const cleanSet = (set, startString) => {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const filtered = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return filtered.join('-');
};

export default cleanSet;
