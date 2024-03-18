#ifndef STACK
#define STACK
// please ignore the #ifndef and #define for today
// they are just some ugly hack promoted to a C idiom

#include <iostream>

template <class T> class Stack {

// internal attributes and operations, not visible by other programs
private:

  // node declaration
  struct stack_node {
    T info;
    stack_node* next;
  }; 

  // attributes of the stack proper: top node and an equiv to len
  stack_node* top_node;
  int stack_height;

  // still private: internal operation that will
  //   return to the OS the memory used by the stack
  // consider declaring it static when you learn what that means
  void free_the_memory(stack_node* a_stack) {  
    if (a_stack != NULL) {
      free_the_memory(a_stack->next);
      delete a_stack;
    }
  }


// identifiers that the class offers to other programs
public:

  // object "this" (similar to Python's "self") is an 
  // implicit parameter in all the methods of the class
  
  Stack() {
  // Standard name for creation methods
  // Simplest stack creation: initialize to be empty
    top_node = NULL;
    stack_height = 0;
  }
  // Other creation operations possible with same name if different args
  
  ~Stack() {
  // Standard name for operation to destroy unneeded stacks automatically
    free_the_memory(top_node);
  }

  void push(const T& x) {
  // Implicit parameter earns x as a new top above whatever it had
    stack_node* aux = new stack_node; 
    aux->info = x;
    aux->next = top_node;
    top_node = aux;
    ++stack_height;
  }

  T top() const {
  // Only valid for a nonempty implicit parameter, o/w Exception
    return top_node->info;
  }

  void pop() {
  // Removes the top
  // Only valid for a nonempty implicit parameter, o/w Exception
    stack_node* aux = top_node; // needed in order to free memory
    top_node = top_node->next;
    delete aux;
    --stack_height;
  }

// Often, there is a single operation that returns the top and
// pops it off at the same time. Here we separate both actions.

  bool is_empty() const {
    return top_node == NULL;
  }

  void empty() {
  // make the implicit parameter an empty stack
    free_the_memory(top_node);
    top_node = NULL;
    stack_height = 0;
  }

  int height() const {
    return stack_height;
  }

};


#endif
// matches the #ifndef, ignore for today
