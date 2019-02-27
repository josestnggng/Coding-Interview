
from dspy.LinkedList import LinkedList


def remove_dups(node):
    has = set()
    prev = None
    while node is not None:
        if node.data in has:
            prev.next = node.next
        else:
            has.add(node.data)
            prev = node
        node = node.next


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(3)
    l.append(3)
    l.append(4)
    l.append(3)
    l.append(3)
    l.print_all()
    remove_dups(l.head)
    l.print_all()
