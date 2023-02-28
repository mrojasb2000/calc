from functools import reduce

class Calc:
    # Python provides support to generic number of arguments 
    # (variadic functions)
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"
        
    def avg(self, args, ut=None):
        if not ut:
           ut = max(args)
        
        _args = [x for x in args if x <= ut]
        return sum(_args) / len(_args)