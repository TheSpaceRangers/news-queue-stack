from collections import deque

class ArticleQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, article):
        self.queue.append(article)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
