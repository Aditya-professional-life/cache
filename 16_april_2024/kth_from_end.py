class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        next_node = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def kth(self, head, k):
        reversed_head = self.reverse(head)
        current = reversed_head
        for _ in range(k - 1):
            if current is None:
                return None
            current = current.next
        return current

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Testing the solution
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print("Original Linked List:")
    linked_list.print_list()

    solution = Solution()
    k = 2  # Example: finding the 2nd node from the end
    kth_node = solution.kth(linked_list.head, k)

    if kth_node:
        print(f"\n{k}th Node from the End of Linked List:")
        print(kth_node.value)
    else:
        print(f"\n{k}th Node from the End of Linked List not found.")
