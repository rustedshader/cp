#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

void print(struct Node *head){
    struct Node *n = head;
    while(n != NULL){
        printf("%d\n",n->data);
        n = n->next;
    }
}

void peek(struct Node *head){
    printf("%d\n",head->data);
}

void node_to_add(struct Node *head, struct Node *to_add){
    to_add->next = head;
}


int main(){
    struct Node *head = NULL;
    struct Node *Two = NULL;
    struct Node *Three = NULL;
    struct Node *Four = NULL;

    head = (struct Node*)malloc(sizeof(struct Node));
    Two = (struct Node*)malloc(sizeof(struct Node));
    Three = (struct Node*)malloc(sizeof(struct Node));
    Four = (struct Node*)malloc(sizeof(struct Node));

    head->data = 9;
    head->next = Two;

    Two->data = 1;
    Two->next = Three;

    Three->data = 7;
    Three->next = NULL;

    Four->data = 4;
    Four->next = NULL;
    node_to_add(head,Four);

    print(Four);
    // peek(head);

    free(head);
    free(Two);
    free(Three);

}   