class ArticleStack:
    def __init__(self):
        self.stack = []

    def push(self, article):
        self.stack.append(article)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
