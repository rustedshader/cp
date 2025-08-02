#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void add_node(struct Node *head, int data)
{
    struct Node *curr = head;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }
    struct Node *to_add;
    to_add = (struct Node *)malloc(sizeof(struct Node));
    to_add->data = data;
    to_add->next = NULL;
    curr->next = to_add;
}

void add_at_index(struct Node *head, int data, int index)
{
    struct Node *curr = head;

    int i = 1;
    while (curr != NULL)
    {
        if (i == index - 1)
        {
            break;
        }
        curr = curr->next;
        i++;
    }

    if (curr == NULL)
    {
        return;
    }

    struct Node *next = curr->next;
    struct Node *to_add;
    to_add = (struct Node *)malloc(sizeof(struct Node));
    to_add->data = data;
    to_add->next = next;
    curr->next = to_add;
}

void print_ll(struct Node *head)
{
    struct Node *curr = head;
    while (curr != NULL)
    {
        printf("%d\n", curr->data);
        curr = curr->next;
    }
}

void delete_node(struct Node **head, int data)
{
    struct Node *curr = *head;
    struct Node *prev;

    if (curr->data == data)
    {
        *head = curr->next;
        return;
    }

    while (curr->data != data)
    {
        prev = curr;
        curr = curr->next;
    }

    if (curr == NULL)
    {
        return;
    }

    struct Node *next = curr->next;
    prev->next = next;
    curr = NULL;
}

struct Node *rev_ll(struct Node *head)
{
    struct Node *curr = head;
    struct Node *prev = NULL;
    struct Node *next = NULL;

    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

int main()
{
    struct Node *head;
    head = (struct Node *)malloc(sizeof(struct Node));
    head->data = 5;
    head->next = NULL;
    add_node(head, 6);
    add_node(head, 9);
    print_ll(head);
    printf("\n");
    delete_node(&head, 5);
    printf("\n");
    print_ll(head);
    add_at_index(head, 69, 2);
    printf("\n");
    print_ll(head);
    head = rev_ll(head);
    printf("\n");
    print_ll(head);
    free(head);
}