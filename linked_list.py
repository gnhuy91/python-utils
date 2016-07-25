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

    # if next_node is a Node instance, keep moving
    if isinstance(head.next, Node):
        Insert(head.next, data)
    # reached end of the linked-list,
    # insert data as next_node of this last node
    else:
        head.next = Node(data=data)


def InsertNth(head, data, position):
    if not head:
        head = Node(data)

    if position == 0:
        head = Node(data, head)
    else:
        # start from 1
        i = 1
        current_node = head

        while True:
            if i == position:
                # Insert new node between current node and its next node.
                new_node = Node(data, current_node.next)
                current_node.next = new_node
                break
            else:
                # keep moving to next node until meet position
                current_node = current_node.next
                i += 1

    return head


def main():
    n = Node(1, Node(2))
    Insert(n, 3)
    Insert(n, 4)
    Insert(n, 5)
    print_list(n)

if __name__ == '__main__':
    main()
