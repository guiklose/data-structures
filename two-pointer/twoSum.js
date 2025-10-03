// We need to check whether the sum of two numbers within
// an array is equal to some target.

// O(n^2) time / O(1) space complexity
function twoSum(array, targetNumber) {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < (array.length - 1); j++) {
      if (array[i] + array[j] === targetNumber) {
        return true;
      }
    }
  }

  return false;
}

// Test case:
// twoSum([1, 2, 3, 4, 5], 3);

// O(n) time / O(1) space complexity (two pointers method).
function twoSumOptimized(array, targetNumber) {
  let leftSearch = 0;
  let rightSearch = array.length - 1;

  while (leftSearch < rightSearch) {

    let sum = array[leftSearch] + array[rightSearch];

    if (sum === targetNumber) {
      return true;
    }

    if (sum < targetNumber) {
      leftSearch += 1;
    }

    if (sum > targetNumber) {
      rightSearch -= 1;
    }
  }

  return false;
}

// Test case:
// twoSumOptimized([1, 2, 3, 4, 5], 10);
