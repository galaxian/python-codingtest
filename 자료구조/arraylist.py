class ArrayList:
    def __init__(self):
        self.list = []
        self.cnt = 0

    def append(self, data):
        self.list.append(data)
        self.cnt += 1
