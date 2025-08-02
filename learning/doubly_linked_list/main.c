#include <stdio.h>


struct Node {
	int value;
	struct Node *prev;
	struct Node *next;
};
typedef struct Node Node;

Node *createNode(int data){
	Node *newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = NULL;
	newNode->prev = NULL;
}

void insertAtBeginning(Node **head, int data){
	Node *newNode = createNode(data);

	if (*head == NULL) {
		*head = newNode;
		return;
	}
	newNode->next = *head;
	(*head)->prev = newNode;
	*head = newNode;
}


void insertAtEnd(Node **head , int data){
	Node *newNode = createNode(data);

	if (*head == NULL){
		*head = newNode;
		return;
	}

	Node *temp  = *head;
	while(temp->next != NULL) {
		temp = temp->next;
	}
	temp->next = newNode;
	newNode->prev = temp;
}

int main(){
	Node *head = NULL;

}
