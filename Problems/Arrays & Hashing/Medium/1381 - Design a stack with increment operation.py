class CustomStack:

    def __init__(self, maxSize: int):
        self.elems = []
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if len(self.elems) < self.maxsize:
            self.elems.append(x)

    def pop(self) -> int:
        if not self.elems:
            return -1
        return self.elems.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.elems))):
            self.elems[i] += val