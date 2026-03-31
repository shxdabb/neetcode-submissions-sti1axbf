
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        dummy = ListNode()
        s,f = head,head.next
        
        while f and f.next:
            s = s.next
            f = f.next.next


        # now s.next is where the new list will start
        #write a reversal

        prev = None
        curr = s.next
        s.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #now prev is at last/ or rather the first node of the reversed list

        
        first = head
        second = prev


        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

