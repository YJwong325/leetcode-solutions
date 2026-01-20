# Author: Yuan Jie Wong
# Last Updated: 2025-09-17

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = ListNode()
        self.__cur = self.head

    def append(self, data_array):
        for data in data_array:
            self.__cur.next = ListNode(data)
            self.__cur = self.__cur.next
    
    def getList(self):
        return self.head.next
    
    def setEmpty(self):
        self.head = ListNode()
        self.__cur = self.head

class Solution(object):
    def mergeKLists(self, lists):
        # divide and conquer: divide the problem into 2 lists from many lists to make it more manageable
        def merge(list1, list2):
            empty = ListNode()
            new_list = empty

            while list1 and list2:
                if list1.val < list2.val:
                    new_list.next = list1
                    list1 = list1.next
                else:
                    new_list.next = list2
                    list2 = list2.next
                new_list = new_list.next
            
            if list1:
                new_list.next = list1
            else:
                new_list.next = list2
            
            return empty.next

        if not lists:
            return None
        
        while len(lists) > 1:
            new_merged = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                # also can be:
                # if i + 1 < len(lists):
                #     list2 = lists[i + 1]
                # else:
                #     list2 = None

                new_merged.append(merge(list1, list2))
            lists = new_merged
        
        return lists[0]

def display(list, new_line=True):
        temp = list
        print("[", end="")
        while temp:
            if temp.next:
                print(f'{temp.val}, ', end="")
            else:
                print(f'{temp.val}', end="")
            temp = temp.next
        print("]") if new_line else print("]", end="")

print("\nExample 1:")
array_1 = []

list = LinkedList()
# list.append(7)
# list.append(13)
# list.append(42)

list.append([7, 13, 42])
array_1.append(list.getList())

list.setEmpty()
list.append([99])
array_1.append(list.getList())

list.setEmpty()
list.append([2, 5, 5, 8])
array_1.append(list.getList())

list.setEmpty()
list.append([])
array_1.append(list.getList())

list.setEmpty()
list.append([3, 12, 65, 77, 91])
array_1.append(list.getList())

list.setEmpty()
list.append([8, 14])
array_1.append(list.getList())

print("Initial array of linked lists:")
print("[", end="")
for l in array_1:
    display(l, False)
    if l != array_1[-1]:
        print(", ", end="")
    else:
        print("]")

example_1 = Solution()
display(example_1.mergeKLists(array_1))

print("\nExample 2:")
array_2 = []

list.setEmpty()
list.append([5, 8, 12, 19])
array_2.append(list.getList())

list.setEmpty()
list.append([3, 7, 14])
array_2.append(list.getList())

list.setEmpty()
list.append([2, 6, 9, 11, 21])
array_2.append(list.getList())

list.setEmpty()
list.append([4, 18])
array_2.append(list.getList())

list.setEmpty()
list.append([1, 10, 13, 15, 17, 20])
array_2.append(list.getList())

print("Initial array of linked lists:")
print("[", end="")
for l in array_2:
    display(l, False)
    if l != array_2[-1]:
        print(", ", end="")
    else:
        print("]")

example_2 = Solution()
display(example_2.mergeKLists(array_2))
print("")