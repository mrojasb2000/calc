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
        
    def avg(self, args, lt=None, ut=None):
        if len(args) == 0:
            return 0
        
        if not lt:
            lt = min(args)

        if not ut:
           ut = max(args)
        
        _args = [x for x in args if x >= lt and x <= ut]
        
        if len(_args) == 0:
            return 0
        
        return sum(_args) / len(_args)