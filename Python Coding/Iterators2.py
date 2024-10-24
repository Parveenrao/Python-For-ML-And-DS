# built in iterators thats runs internally

# example range function ( that internally use iterators)

# in this lecture we create our own iterators

class PowerOfTwo:
    def __int__(self, max_value):
        self.limit = max_value
        self.current = 1

    def __iter__(self):
        return self


    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current = self.current * 2
            return result

        else:
            raise StopIteration


n = int(input("Enter your limit"))
iter_obj = PowerOfTwo(n)
for ele in iter_obj:
    print(ele)