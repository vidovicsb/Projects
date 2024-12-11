class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Cannot be negative capacity")
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return "🍪" * self._n

    def deposit(self, n):
        if self._n + n > self.capacity:
            raise ValueError("Too many cookies are being deposited")
        self._n += n

    def withdraw(self, n):
        if (self._n - n) < 0:
            raise ValueError("You are taking away too many cookies")
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n


def main():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(4)
    print(jar)
    print(jar.size)

main()
