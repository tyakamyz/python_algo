# https://leetcode.com/problems/design-browser-history/

class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, hompage):
        self.head = self.current = ListNode(val=hompage)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next

    def forward(self, index):
        for _ in range(index):
            if self.current.next == None:
                return self.current.val;    
        
            self.current = self.current.next
        
        return self.current.val

    def back(self, index):
        for _ in range(index):
            if self.current.prev == None:
                return self.current.val;    
        
            self.current = self.current.prev
        
        return self.current.val

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)