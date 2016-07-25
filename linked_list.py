class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    print head.data
    if head.next:
        print_list(head.next)


def Insert(head, data):
    if not isinstance(head, Node):
        head = Node(data=data)
    else:
        if head.next:
            Insert(head.next, data)
        else:
            head.next = Node(data=data)


def main():
    n = Node(1, Node(2))
    Insert(n, 3)
    Insert(n, 4)
    Insert(n, 5)
    print_list(n)

if __name__ == '__main__':
    main()
