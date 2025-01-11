class Node:
    def __init__(self, content):
        self.content = content
        self.next = None


def view(head: Node):
    current = head
    while current is not None:
        print(current.content)
        current = current.next
