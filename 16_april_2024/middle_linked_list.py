class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class Solution:
    def middle(self, head):
        slow = head
        fast = head

        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

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
    linked_list.append(6)

    print("Original Linked List:")
    linked_list.print_list()

    solution = Solution()
    middle_node = solution.middle(linked_list.head)

    print("\nMiddle Element of Linked List:")
    print(middle_node.value)
