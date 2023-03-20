# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(); 

        dummy.next = head; 

        fp = sp = dummy;   

        for i in range(n):
            fp = fp.next;   

        while fp.next != None:
            fp = fp.next; 
            sp = sp.next;  

        deletingItem = sp.next;   
        sp.next = sp.next.next;   

        del(deletingItem);   

        return dummy.next;    



