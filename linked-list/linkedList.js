import { Node } from "./nodeClass.js";

class LinkedList {
  constructor() {
    this.head = null;
  }

  append(node) {
    if (!this.head) {
      this.head = node;
      return;
    }

    let currentNode = this.head;

    // Loop through the list until we get to the end.
    while (currentNode.next) {
      currentNode = currentNode.next;
    }

    // Go to the next node in the list.
    currentNode.next = node;
  }

  remove(index) {
    let currentNode = this.head;
    let lastNode = null;

    let listIndex = 0;

    // Loop through the list until we get to the end.
    while (currentNode) {
      if (index === 0) {
        this.head = this.head.next;
        return;
      }

      if (listIndex === index) {
        lastNode.next = currentNode.next;
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
      currentNode = currentNode.next;
    }

    console.log(log);
  }


}

// Instanciate the class
const list = new LinkedList();

// Uncomment to test.
// list.append(new Node(0));

// list.log();

// list.remove(0);

// list.log();

// list.append(new Node(1));
// list.append(new Node(2));
// list.append(new Node(3));

// list.log();
// list.remove(0);
// list.remove(0);

// list.log();

// list.append(new Node(5));

// list.append(new Node(5));

// list.remove(2);
// list.log();