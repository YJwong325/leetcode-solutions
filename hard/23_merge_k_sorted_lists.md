# LeetCode 23: Merge k Sorted Lists
[Problem statement on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

## Approach
The problem involves joining multiple linked lists into one huge linked list in ascending order. A solution we can use is a divide and conquer method to simplify the problem so that we can solve it one small part at a time. The approach involves merging 2 small linked lists at a time and joining them in ascending order. Once we are able to join 2 linked lists together, we would be able to eventually join all the linked lists given by the problem with multiple iterations.

### Part 1: Joining 2 Linked Lists

Here we have 2 linked lists as examples and we will try to merge their nodes together in ascending order.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))

    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node1 --> l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node1

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node1 --> l2_node2 --> l2_node3
    l2_ptr --> l2_node1

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_nodePtr --> nl_head
```

The circular nodes represent pointers that are pointing to specific nodes in the linked lists. These pointers can change the next pointer of the nodes they reference.

Since we want to merge the linked lists in ascending order, we will have to pick the lower value when deciding which node to add to the <u>new linked list? (change to merged linked list or what)</u>. Between the two starting nodes, we have the values:

$$
\texttt{list1.val = 1} \qquad | \qquad \texttt{list2.val = 2}
$$
 
Since list1.val is smaller, it will be added to the new linked list first.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node1 --> l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node1

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node1 --> l2_node2 --> l2_node3
    l2_ptr --> l2_node1

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1
    nl_nodePtr --> nl_head 
```

Then we update the list1 pointer to point to the next node in its own list.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node1 --> l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node1 --> l2_node2 --> l2_node3
    l2_ptr --> l2_node1

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1
    nl_nodePtr --> l1_node1
```

Now we compare the current values of list1.val and list2.val again.

$$
\texttt{list1.val = 4} \qquad | \qquad \texttt{list2.val = 2}
$$

Since list2.val is smaller, it will be pointed to next

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node1 --> l2_node2 --> l2_node3
    l2_ptr --> l2_node1

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1 --> l2_node1
    nl_nodePtr --> l1_node1
```

Then we update the pointers again.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node1 --> l2_node2 --> l2_node3
    l2_ptr --> l2_node2

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1 --> l2_node1
    nl_nodePtr --> l2_node1
```

We keep repeating this process of checking for the smaller value of the nodes currently being pointed to by the two list pointers, joining the node with the smaller value to the new list, and updating the pointers to prepare for the next node addition to the new list.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node2 --> l1_node3 --> l1_node4
    l1_ptr --> l1_node3

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1 --> l2_node1 --> l1_node2
    nl_nodePtr --> l1_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node2 --> l2_node3
    l2_ptr --> l2_node2
```

We will keep adding nodes to the new list until one of the original linked lists run out of nodes with values.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node3 --> l1_node4
    l1_ptr --> l1_node3

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1 --> l2_node1 --> l1_node2 --> l2_node2
    nl_nodePtr --> l2_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node2 --> l2_node3
    l2_ptr --> l2_node3
```

Since list2 is now empty and pointing to None, we do not have anymore nodes to compare and we can just point to whatever node is left in list1 because the original linked lists are already sorted in ascending order.

```mermaid
flowchart LR
    %% List 1 pointers
    l1_ptr((list1))
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node3 --> l1_node4
    l1_ptr --> l1_node3

    %% New list pointers
    nl_nodePtr((new_list))

    %% New list nodes
    nl_head[empty]

    nl_head --> l1_node1 --> l2_node1 --> l1_node2 --> l2_node2 --> l1_node3
    nl_nodePtr --> l2_node2

    %% List 2 pointers
    l2_ptr((list2))

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
    l2_node3[None]

    l2_node3
    l2_ptr --> l2_node3
```

The resulting linked list will be sorted in ascending order and is returned using empty.next.

```mermaid
flowchart LR
    %% List 1 pointers
    
    %% List 1 nodes
    l1_node1[1]
    l1_node2[4]
    l1_node3[7]
    l1_node4[None]

    l1_node3 --> l1_node4

    %% New list pointers

    %% New list nodes

    l1_node1 --> l2_node1 --> l1_node2 --> l2_node2 --> l1_node3

    %% List 2 pointers

    %% List 2 nodes
    l2_node1[2]
    l2_node2[5]
```

We have successfully joined the two linked lists together and sorted them in ascending order of their values.

### Part 2: Joining a List of Linked Lists

Using the method of joining 2 linked lists together in Part 1, we can iterate through an array of linked lists, joining 2 at a time until we end up with 1 large linked list.

Here we have a list of 5 linked lists:

$$
\begin{array}{ccccc}
\large \textbf{[} \space \space \normalsize l_1, & l_2, & l_3, & l_4, & l_5 \large \space \space \textbf{]} \\
\end{array}
$$

After iterating through the list once and joining 2 linked list using the method in part 1, the array of linked lists would look something like this:

$$
\begin{array}{ccc}
\large \textbf{[} \space \space \normalsize l_{1}l_{2}, & l_{3}l_{4}, & l_5 \large \space \space \textbf{]} \\
\end{array}
$$

$$
\small\text{$l_{1}l_{2}$ denotes $l_{1}$ merged with $l_{2}$}
$$

Iterating through the list for a second time will yield:

$$
\begin{array}{cc}
\large \textbf{[} \space \space \normalsize l_{1}l_{2}l_{3}l_{4}, & l_{5} \large \space \space \textbf{]} \\
\end{array}
$$

A third and final iteration through the entire array produces the final linked list, with its nodes sorted in ascending order by using the method in part 1.

$$
\begin{array}{c}
\large \textbf{[} \space \space \normalsize l_{1}l_{2}l_{3}l_{4}l_{5} \large \space \space \textbf{]}
\end{array}
$$

## Example 1:

Initial array of linked list:

$$
\begin{bmatrix}
\begin{bmatrix} 7, & 13, & 42 \end{bmatrix}, &
\begin{bmatrix} 99 \end{bmatrix}, &
\begin{bmatrix} 2, & 5, & 5, & 8 \end{bmatrix}, &
[], &
\begin{bmatrix} 3, & 12, & 65, & 77, & 91 \end{bmatrix}, &
\begin{bmatrix} 8, & 14 \end{bmatrix}
\end{bmatrix}
$$

$$
\left[\begin{array}{cccccc}

\left[\begin{array}{ccc} 7, & 13, & 42 \end{array}\right], &
\left[\begin{array}{c} 99 \end{array}\right], &
\left[\begin{array}{cccc} 2, & 5, & 5, & 8 \end{array}\right], &
[], &
\left[\begin{array}{ccccc} 3, & 12, & 65, & 77, & 91 \end{array}\right], &
\left[\begin{array}{cc} 8, & 14 \end{array}\right]

\end{array}\right]
$$

After the first iteration and using the merge() function that was defined to merge 2 lists at a time, the initial array will be transformed into the following array: 

$$
\begin{array}{ccc}
\Large \textbf{[} \space

\normalsize
\begin{array}{cccc}
\large \textbf{[} \space \normalsize 7, & 13, & 42, & 99 \large \space \textbf{]}
\end{array},
&
\begin{array}{cccc}
\large \textbf{[} \space \normalsize 2, & 5, & 5, & 8 \large \space \textbf{]}
\end{array},
&
\begin{array}{ccccccc}
\large \textbf{[} \space \normalsize 3, & 8, & 12, & 14, & 65, & 77, & 91 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

After the second iteration: 

$$
\begin{array}{cc}
\Large \textbf{[} \space

\normalsize
\begin{array}{cccccccc}
\large \textbf{[} \space \normalsize 2, & 5, & 5, & 7, & 8, & 13, & 42, & 99 \large \space \textbf{]}
\end{array},
&
\begin{array}{ccccccc}
\large \textbf{[} \space \normalsize 3, & 8, & 12, & 14, & 65, & 77, & 91 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

The final iteration will yield the complete merged linked list with all values sorted in ascending order. 

$$
\begin{array}{c}
\Large \textbf{[} \space

\normalsize
\begin{array}{ccccccccccccccc}
\large \textbf{[} \space \normalsize 2, & 3, & 5, & 5, & 7, & 8, & 8, & 12, & 13, & 14, & 42, & 65, & 77, & 91, & 99 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

## Example 2:

Initial array of linked list:

$$
\begin{array}{ccccc}
\Large \textbf{[} \space

\normalsize
\begin{array}{cccc}
\large \textbf{[} \space \normalsize 5, & 8, & 12, & 19 \large \space \textbf{]}
\end{array},
&
\begin{array}{ccc}
\large \textbf{[} \space \normalsize 3, & 7, & 14 \large \space \textbf{]}
\end{array},
&
\begin{array}{ccccc}
\large \textbf{[} \space \normalsize 2, & 6, & 9, & 11, & 21 \large \space \textbf{]}
\end{array},
&
\begin{array}{cc}
\large \textbf{[} \space \normalsize 4, & 18 \large \space \textbf{]}
\end{array},
&
\begin{array}{cccccc}
\large \textbf{[} \space \normalsize 1, & 10, & 13, & 15, & 17, & 20 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

After the first iteration using the merge() function:

$$
\begin{array}{ccc}
\Large \textbf{[} \space

\normalsize
\begin{array}{ccccccc}
\large \textbf{[} \space \normalsize 3, & 5, & 7, & 8, & 12, & 14, & 19 \large \space \textbf{]}
\end{array},
&
\begin{array}{ccccccc}
\large \textbf{[} \space \normalsize 2, & 4, & 6, & 9, & 11, & 18, & 21 \large \space \textbf{]}
\end{array},
&
\begin{array}{cccccc}
\large \textbf{[} \space \normalsize 1, & 10, & 13, & 15, & 17, & 20 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

After the second iteration we get:

$$
\begin{array}{cc}
\Large \textbf{[} \space

\normalsize
\begin{array}{cccccccccccccc}
\large \textbf{[} \space \normalsize 2, & 3, & 4, & 5, & 6, & 7, & 8, & 9, & 11, & 12, & 14, & 18, & 19, & 21 \large \space \textbf{]}
\end{array},
&
\begin{array}{cccccc}
\large \textbf{[} \space \normalsize 1, & 10, & 13, & 15, & 17, & 20 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$

Notice how the last linked list in the array remains unchanged. In the first and second iteration, the index of the last linked list was odd. 

Considering the fact that the index of the first linked list in a pair will always be odd, if an odd index is found at the last element of the array, there will not be a second linked list to complete the merging pair. Thus, the last linked list in the array of this particular example was unchanged for 2 iterations before merging into the final linked list.

After the third iteration, we will get the final linked list sorted in ascending order for example number 2.

$$
\begin{array}{c}
\Large \textbf{[} \space

\normalsize
\begin{array}{cccccccccccccccccccc}
\large \textbf{[} \space \normalsize 1, & 2, & 3, & 4, & 5, & 6, & 7, & 8, & 9, & 10, & 11, & 12, & 13, & 14, & 15, & 17, & 18, & 19, & 20, & 21 \large \space \textbf{]}
\end{array}

\Large \space \textbf{]}
\end{array}
$$


## Code
```python
def mergeKLists(self, lists):
    # divide and conquer: divide the problem into 2 lists from many 
    #                     lists to make it more manageable
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

            # the above can also be written as:
            # if i + 1 < len(lists):
            #     list2 = lists[i + 1]
            # else:
            #     list2 = None

            new_merged.append(merge(list1, list2))

        lists = new_merged
        
    return lists[0]
```


