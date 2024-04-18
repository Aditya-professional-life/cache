class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class Solution:
    def cycle(self, head):
        if head is None or head.next is None:
            return False
        
        fast = slow = head

        while fast.next and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False

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

    def add_cycle(self, index):
        if index < 0:
            return
        current = self.head
        cycle_node = None
        i = 0
        while current.next:
            if i == index:
                cycle_node = current
            current = current.next
            i += 1
        if cycle_node:
            current.next = cycle_node

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

    # Add a cycle
    linked_list.add_cycle(2)  # Creating a cycle at the index 2

    solution = Solution()
    has_cycle = solution.cycle(linked_list.head)

    print("Linked List has a cycle:" if has_cycle else "Linked List does not have a cycle.")
