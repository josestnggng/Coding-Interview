from dspy.LinkedList import LinkedList


def kth_to_last(head, k):
    p1, p2 = head, head

    # move p1 k node
    for i in range(k):
        if p1 is None:
            return
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(10)
    l.print_all()
    l2 = kth_to_last(l.head, 10)
    if l2:
        l2.print_all()
