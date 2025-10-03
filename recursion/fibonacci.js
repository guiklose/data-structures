function fibonacci(number) {
  if (number === 0 || number === 1) {
    return number;
  }

  return fibonacci(number - 1) + fibonacci(number - 2);
}

// Call some number to get the nth fibonacci number.
// const result = fibonacci(X);
