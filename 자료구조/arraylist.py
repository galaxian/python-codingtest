class ArrayList:
    def __init__(self):
        self.list = []
        self.cnt = 0

    def append(self, data):
        self.list.append(data)
        self.cnt += 1

    def get(self, idx):
        if idx < 0 or idx >= self.cnt:
            print("유효한 인덱스가 아닙니다.")
        print(self.list[idx])

    def print_all(self):
        idx = 0
        while idx < self.cnt:
            print(self.list[idx])
            idx += 1
