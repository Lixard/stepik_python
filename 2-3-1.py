class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterator = iter(iterable)
        self.funcs = funcs
        self.judge_func = judge

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator)
        pos = 0
        neg = 0

        for func in self.funcs:
            result = func(value)
            if result:
                pos += 1
            else:
                neg += 1

        if self.judge_func(pos, neg):
            return value
        else:
            return next(self)
