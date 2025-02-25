#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct Stack
{
  int arr[MAX_SIZE];
  int top;
};

void initialize(struct Stack *stack)
{
  stack->top = -1;
}
int isEmpty(struct Stack *stack)
{
  if (stack->top == -1)
  {
    return 1;
  }
  return 0;
}

void push(struct Stack *stack, int data)
{
  stack->arr[++stack->top] = data;
}

void peek(struct Stack *stack)
{
  if (isEmpty(stack))
  {
    printf("Stack is Empty\n");
    return;
  }
  printf("%d\n", stack->arr[stack->top]);
}

void pop(struct Stack *stack)
{
  if (isEmpty(stack))
  {
    return;
  }
  stack->top--;
}
int main()
{
  struct Stack *stack = (struct Stack *)malloc(sizeof(struct Stack));
  initialize(stack);
  push(stack, 5);
  push(stack, 6);
  push(stack, 7);
  push(stack, 8);

  while (!isEmpty(stack))
  {
    peek(stack);
    pop(stack);
  }
  // My Extra Love Free the memory xD
  free(stack);
  return 0;
}