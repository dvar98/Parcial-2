import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

class MapFilterListener(ParseTreeListener):
    def enterMapExpr(self, ctx:MapFilterParser.MapExprContext):
        function = ctx.function().getText()
        iterable = self.getIterable(ctx.iterable())
        print(f"Applying MAP function '{function}' to iterable '{iterable}'")
        result = list(map(self.getFunction(function), iterable))
        print(f"Result: {result}")

    def enterFilterExpr(self, ctx:MapFilterParser.FilterExprContext):
        function = ctx.function().getText()
        iterable = self.getIterable(ctx.iterable())
        print(f"Applying FILTER function '{function}' to iterable '{iterable}'")
        result = list(filter(self.getFunction(function), iterable))
        print(f"Result: {result}")

    def getIterable(self, ctx):
        if ctx.NAME():
            return ctx.NAME().getText()
        elif ctx.list_():
            return [int(e.getText()) for e in ctx.list_().elements().element()]
        elif ctx.tuple_():
            return [int(e.getText()) for e in ctx.tuple_().elements().element()]
        return []

    def getFunction(self, name):
        if name == "square":
            return lambda x: x ** 2
        elif name == "double":
            return lambda x: x * 2
        elif name == "even":
            return lambda x: x % 2 == 0
        elif name == "odd":
            return lambda x: x % 2 != 0
        elif name == "multiple":
            return lambda x: x % 3 == 0
        return lambda x: x

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MapFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.prog()

    listener = MapFilterListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)