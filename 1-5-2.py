class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer += a
        while len(self.buffer) >= 5:
            total = 0
            for i in self.buffer[:5]:
                total += i
            del self.buffer[:5]
            print(total)

    def get_current_part(self):
        return self.buffer


buf = Buffer()
buf.add(1, 2, 3)
print("get 1 ", buf.get_current_part())
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print("get 2", buf.get_current_part())
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print("get 3", buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print("get 4", buf.get_current_part())
