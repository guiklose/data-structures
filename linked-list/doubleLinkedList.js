import { DoubleWayNode } from "./nodeClass.js";

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(node) {
    if (!this.head) {
      this.head = node;
      this.tail = node;

      return;
    }

    let currentNode = this.tail;

    // Update next and previous of the node.
    node.previous = currentNode;
    currentNode.next = node;

    // Save the last appended node as the tail.
    node.next = this.head;
    this.head.previous = node;
    this.tail = node;
  }

  remove(index) {
    let currentNode = this.head;
    let lastNode = null;

    let listIndex = 0;

    // Loop through the list until we get to the end.
    while (currentNode) {
      if (index === 0) {
        this.head = this.head.next;
        if (this.head) this.head.previous = this.tail;

        return;
      }

      if (listIndex === index) {
        if (currentNode === this.tail) {
          this.tail = lastNode;
        }

        lastNode.next = currentNode.next;
        currentNode.next.previous = lastNode;
        return;
      }

      // Update the node's reference.
      lastNode = currentNode;
      currentNode = currentNode.next;

      // Update the index.
      listIndex += 1;
    }

    console.log('Invalid index.');
  }

  log() {
    let currentNode = this.head;
    let log = '';

    // Loop through the list until we get to the end.
    while (currentNode) {
      log += currentNode.value;
      log += ' ';

      if (currentNode === this.tail) break;

      currentNode = currentNode.next;
    }

    console.log(log);
  }
}

// Instanciate the class
const list = new LinkedList();

// Uncomment to test.
// list.append(new DoubleWayNode(0));

// list.log();

// list.remove(0);
// list.remove(0);

// list.log();

// list.append(new DoubleWayNode(1));
// list.append(new DoubleWayNode(2));
// list.append(new DoubleWayNode(3));

// list.log();
// list.remove(0);
// list.remove(0);

// list.log();

// list.append(new DoubleWayNode(4));

// list.append(new DoubleWayNode(5));

// list.remove(2);
// list.log();