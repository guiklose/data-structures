class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) 'Stack empty.';

    return this.items.pop();
  }

  isEmpty() {
    return (this.items.length === 0);
  }

  size() {
    return this.items.length
  }

  print() {
    console.log(this.items);
  }
}


const stack = new Stack();

// stack.push(1)
// stack.push(2)
// stack.push(3)
// stack.push(4)
// stack.push(5)

// console.log(stack.pop())
// console.log(stack.pop())
// console.log(stack.pop())
// console.log(stack.pop())
// console.log(stack.pop())
