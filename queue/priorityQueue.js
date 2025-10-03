class PriorityNode {
  constructor(value, priority) {
    this.value = value;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.items = [];
  }

  enqueue(node) {
    let isQueued = false;

    for (let index = 0; index < this.items.length; index++) {
      if (this.items[index].priority < node.priority) {
        this.items.splice(index, 0, node);

        isQueued = true;
        break;
      }
    }

    if (!isQueued) this.items.push(node);
  }

  dequeue() {
    if (this.isEmpty()) return 'Empty Queue.';

    return this.items.shift();
  }

  front() {
    if (this.isEmpty()) return 'Empty Queue.';

    return this.items[0];
  }

  rear() {
    if (this.isEmpty()) return 'Empty Queue.';

    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return (this.items.length === 0);
  }
}

// Creating queue.
const priorityQueue = new PriorityQueue();

// Creating nodes.
// const node1 = new PriorityNode('A', 1);
// const node2 = new PriorityNode('A', 1);
// const node3 = new PriorityNode('B', 5);
// const node4 = new PriorityNode('C', 2);
// const node5 = new PriorityNode('T', 10);
// const node6 = new PriorityNode('X', 88);
// const node7 = new PriorityNode('Z', 3);
// const node8 = new PriorityNode('A', 1);

// Empty.
// console.log(priorityQueue.front());

// Adding nodes to queue.
// priorityQueue.enqueue(node1);
// priorityQueue.enqueue(node2);
// priorityQueue.enqueue(node3);
// priorityQueue.enqueue(node4);
// priorityQueue.enqueue(node5);

// console.log(priorityQueue.front());
// console.log(priorityQueue.rear());

// Adding nodes to queue.
// priorityQueue.enqueue(node6);
// priorityQueue.enqueue(node7);

// console.log(priorityQueue.front());
// console.log(priorityQueue.rear());

// Adding nodes to queue.
// priorityQueue.enqueue(node8);

// console.log(priorityQueue.items);

// Removing nodes from the queue.
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())

// Empty
// console.log(priorityQueue.dequeue())
