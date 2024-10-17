import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser

class FourierTransformListener(ParseTreeListener):
    def enterFourierTransformStmt(self, ctx:FourierTransformParser.FourierTransformStmtContext):
        iterable = self.getIterable(ctx.iterable())
        print(f"Calculating Fourier Transform for iterable: {iterable}")
        result = self.calculateFourierTransform(iterable)
        print(f"Result: {result}")

    def enterPairTransformStmt(self, ctx:FourierTransformParser.PairTransformStmtContext):
        iterable = self.getIterable(ctx.iterable())
        print(f"Calculating Pair Transform for iterable: {iterable}")
        result = self.calculatePairTransform(iterable)
        print(f"Result: {result}")

    def getIterable(self, ctx):
        if ctx.NAME():
            return ctx.NAME().getText()  # Placeholder for actual data retrieval
        elif ctx.list_():
            return [float(e.getText()) for e in ctx.list_().elements().element()]
        elif ctx.tuple_():
            return [float(e.getText()) for e in ctx.tuple_().elements().element()]
        return []

    def calculateFourierTransform(self, data):
        import numpy as np
        return np.fft.fft(data)

    def calculatePairTransform(self, data):
        # Placeholder for pair transform logic
        return [(x, 2*x) for x in data]

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = FourierTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierTransformParser(stream)
    tree = parser.prog()

    listener = FourierTransformListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)