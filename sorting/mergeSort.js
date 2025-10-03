// O(N*logN) time complexity / O(n) space complexity search
//
// This algorithm follows the divide to conquer pattern.
function mergeSort(array) {
  if (array.length <= 1) return array;

  const midArray = Math.floor(array.length / 2);
  const leftMerge = mergeSort(array.slice(0, midArray));
  const rightMerge = mergeSort(array.slice(midArray));
  return merge(leftMerge, rightMerge);
}

function merge(left, right) {
  let result = [];
  let leftIndexer = 0;
  let rightIndexer = 0;

  while ((leftIndexer < left.length) && (rightIndexer < right.length)) {
    if (left[leftIndexer] < right[rightIndexer]) {
      result.push(left[leftIndexer]);
      leftIndexer++;
    } else {
      result.push(right[rightIndexer]);
      rightIndexer++;
    }
  }

  return result.concat(left.slice(leftIndexer), right.slice(rightIndexer));
}

const sortedArray = mergeSort([0, 2, -4, 6, 1, -9]);
