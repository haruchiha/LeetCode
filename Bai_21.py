#Merger Two Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # kiểm tra list rỗng
        if not list1 or not list2:
            return list1 if not list2 else list2

        # so sánh 2 phần tử đầu của danh sách
        if list1.val > list2.val:
            list1, list2 = list2, list1

        # đệ quy để hợp nhất phần còn lại của danh sách:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
