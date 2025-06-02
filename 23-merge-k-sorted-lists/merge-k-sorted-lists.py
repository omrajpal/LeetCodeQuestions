# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy

        while True:
            minVal = float('inf')
            minIndex = -1

            for i in range(len(lists)):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    minIndex = i

            if minIndex == -1:
                break

            # Append the smallest node
            curr.next = lists[minIndex]
            curr = curr.next

            # Advance in that list
            lists[minIndex] = lists[minIndex].next

        return dummy.next