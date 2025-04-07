#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct Queue
{
    int arr[MAX_SIZE];
    int front;
    int back;
};

void enqueue(struct Queue *qq, int data)
{

    if (qq->back == -1)
    {
        qq->front++;
        qq->back++;
        qq->arr[qq->front] = data;
    }
    else
    {
        qq->front++;
        qq->arr[qq->front] = data;
    }
}

void dequeue(struct Queue *qq)
{
    if (qq->back == -1)
    {
        printf("Error Not Initialized");
    }
    else
    {
        qq->back++;
    }
}

void print_queue(struct Queue *qq)
{
    int t = qq->front;
    int b = qq->back;

    for (int i = b; i <= t; i++)
    {
        printf("%d\n", qq->arr[i]);
    }
}

int main()
{
    struct Queue *qq = (struct Queue *)malloc(sizeof(struct Queue));
    qq->front = -1;
    qq->back = -1;
    enqueue(qq, 5);
    enqueue(qq, 6);
    enqueue(qq, 7);
    print_queue(qq);
    dequeue(qq);
    printf("\n");
    print_queue(qq);
}