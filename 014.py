class Collatz():
    _instance = None
    results = {1: 1}
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    @classmethod
    def solve(cls, num):
        if cls.results.get(num):
            return cls.results[num]
        else:
            if num % 2 == 0:
                result = cls.solve(num / 2)+1
                cls.results[num] = result
                return result
            else:
                result = cls.solve(3*num+1)+1
                cls.results[num] = result
                return result

c = Collatz()
max = 1
max_index = 1
for i in range(1, 1000*1000+1):
    v = c.solve(i)
    if max < v:
        max = v
        max_index = i

print(max_index, max)
