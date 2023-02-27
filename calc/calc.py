from functools import reduce

class Calc:
    # Python provides support to generic number of arguments 
    # (variadic functions)
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        return reduce(lambda x, y: x * y, args)
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"