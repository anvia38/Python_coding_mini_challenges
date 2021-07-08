# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr is not None:
            while curr.next is not None and curr.val == curr.next.val:
                curr.next=curr.next.next 
            curr = curr.next
    
        return head

def print_linked_list(head):
    curr = head
    out = '['
    while curr is not None:
        out = out + ' ' + str(curr.val)
        curr = curr.next
    out += ']'
    print(out)

if __name__ == "__main__":
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    listnode = ListNode(2)
    listnode = ListNode(1, listnode)
    listnode = ListNode(1, listnode)
    print_linked_list(listnode)
    sol = Solution()
    deleted_dupes = sol.deleteDuplicates(listnode)
    print_linked_list(deleted_dupes)


