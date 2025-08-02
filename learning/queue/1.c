#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct Queue
{
    char arr[MAX_SIZE];
    int top;
    int bottom;
};

void enque(struct Queue *ss, int data)
{
    ss->bottom = 1;
}

int main()
{
    struct Queue *ss = (struct Queue *)malloc(sizeof(struct Queue));
}
