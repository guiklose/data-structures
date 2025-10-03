function factorial(number) {
  console.log(`number: `, number)
  if (number === 0 || number ===1) {
    return 1;
  }

  return number * factorial(number - 1);
}

// Call some number to get the answer.
// OBS: JS max int number is reached above 170.
// const result = factorial(170);
