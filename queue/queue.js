class Queue {
  constructor() {
    this.items = [];
  }

  enqueue(element) {
    this.items.push(element);
  }

  dequeue() {
    if (this.isEmpty()) return 'Empty Queue';

    return this.items.shift();
  }

  isEmpty() {
    return (this.items.length === 0);
  }

  size() {
    return this.items.length;
  }
}

const queue = new Queue();

// queue.enqueue(1)
// queue.enqueue(2)
// queue.enqueue(3)
// queue.enqueue(4)
// queue.enqueue(5)

// console.log(queue.dequeue())
// console.log(queue.dequeue())
// console.log(queue.dequeue())
// console.log(queue.dequeue())
// console.log(queue.dequeue())
