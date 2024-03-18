#ifndef QUEUE
#define QUEUE
// please ignore the #ifndef and #define for today
// they are just some ugly hack promoted to a C idiom

#include <iostream>

template <class T> class Queue {

// internal attributes and operations, not visible by other programs
private:

  // node declaration
  struct queue_node {
    T info;
    queue_node* next;
  }; 

  // attributes of the queue proper: front and back nodes and an equiv to len
  queue_node* front_node;
  queue_node* back_node;
  int queue_length;

  // still private: internal operation that will
  //   return to the OS the memory used by the queue
  // consider declaring it static when you learn what that means
  void free_the_memory(queue_node* a_queue) {  
    if (a_queue != NULL) {
      free_the_memory(a_queue->next);
      delete a_queue;
    }
  }


// identifiers that the class offers to other programs
public:

  // object "this" (similar to Python's "self") is an 
  // implicit parameter in all the methods of the class
  
  Queue() {
  // Standard name for creation methods
  // Simplest queue creation: initialize to be empty
    front_node = NULL;
    back_node = NULL;
    queue_length = 0;
  }
  // Other creation operations possible with same name if different args
  
  ~Queue() {
  // Standard name for operation to destroy unneeded queues automatically
    back_node = NULL; // o/w that pointer might point to free memory
    free_the_memory(front_node);
  }

  void push_back_wrong(const T& x) {
  // Implicit parameter earns x as a new last item after whatever it had
  // Wrong program
    back_node->next = new queue_node; 
    back_node = back_node->next;
    back_node->info = x;
    back_node->next = NULL; 
    ++queue_length;
  }

  void push_back(const T& x) {
  // Implicit parameter earns x as a new last item after whatever it had
  // FILL IT IN CORRECTLY!
  }

// Often, there is a single operation that returns the front and
// pops it off at the same time. Here we separate both actions.

  void pop_front() {
  // Removes the front
  // Only valid for a nonempty implicit parameter, o/w Exception
    queue_node* aux = front_node; // needed in order to free memory
    front_node = front_node->next;
    if (front_node == NULL) back_node = NULL;
    delete aux;
    --queue_length;
  }

  T front() const {
  // Only valid for a nonempty implicit parameter, o/w Exception
  // FILL IT IN CORRECTLY!
  }

  bool is_empty() const {
  // FILL IT IN CORRECTLY!
  }

  void empty() {
  // make the implicit parameter an empty queue
  // FILL IT IN CORRECTLY!
  }

  int length() const {
  }

};


#endif
// matches the #ifndef, ignore for today
