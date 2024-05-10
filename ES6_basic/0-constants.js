export function taskFirst() {
    const task = 'I prefer const when I can.';  // Use `const` because `task` is not reassigned
    return task;
  }
  
  export function getLast() {
    return ' is okay';
  }
  
  export function taskNext() {
    let combination = 'But sometimes let';     // Use `let` because `combination` is reassigned
    combination += getLast();
  
    return combination;
  }
  