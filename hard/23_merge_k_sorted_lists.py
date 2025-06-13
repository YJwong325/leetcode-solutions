class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        # divide and conquer: divide the problem into 2 lists from many lists to make it more manageable
        def merge(list1, list2):
            empty = ListNode()
            newList = empty

            while list1 and list2:
                if list1.val < list2.val:
                    newList.next = list1
                    list1 = list1.next
                else:
                    newList.next = list2
                    list2 = list2.next
                newList = newList.next
            
            if list1:
                newList.next = list1
            else:
                newList.next = list2
            
            return empty.next

        if not lists:
            return None
        
        while len(lists) > 1:
            newMerged = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                # also can be:
                # if i + 1 < len(lists):
                #     list2 = lists[i + 1]
                # else:
                #     list2 = None

                newMerged.append(merge(list1, list2))
            lists = newMerged
        
        return lists[0]

