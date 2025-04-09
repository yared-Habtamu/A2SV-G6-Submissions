# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class ListNode():
    def __init__(self, tokenId='', expiryTime=0):
        self.tokenId, self.expiryTime = tokenId, expiryTime
        self.next = self.prev = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.authManager = dict()  
        self.start, self.end = ListNode(), ListNode()
        self.start.next, self.end.prev = self.end, self.start 
        self.size = 0
        self.ttl = timeToLive

    def insert(self, node):
        prev, end = self.end.prev, self.end
        prev.next, end.prev = node, node
        node.prev, node.next = prev, end
        self.size += 1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        expiry = currentTime + self.ttl
        self.authManager[tokenId] = ListNode(tokenId, expiry)
        self.insert(self.authManager[tokenId])

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authManager:
            node = self.authManager[tokenId]
            if node.expiryTime > currentTime:
                self.remove(node)
                node.expiryTime = currentTime + self.ttl
                self.insert(node)
            else:
                self.remove(node)
                del self.authManager[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        start = self.start.next

        while start != self.end and start.expiryTime <= currentTime:
            self.remove(start)
            del self.authManager[start.tokenId] 
            start = start.next  
        return self.size