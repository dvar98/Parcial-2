import sys
from antlr4 import *
from ComplexNumbersLexer import ComplexNumbersLexer
from ComplexNumbersParser import ComplexNumbersParser

class ComplexNumbersListener(ParseTreeListener):
    def enterExpr(self, ctx:ComplexNumbersParser.ExprContext):
        result = None
        for i in range(0, len(ctx.children), 2):
            complex_num = self.getComplexNumber(ctx.getChild(i))
            if result is None:
                result = complex_num
            else:
                operator = ctx.getChild(i-1).getText()
                if operator == '+':
                    result = (result[0] + complex_num[0], result[1] + complex_num[1])
                elif operator == '-':
                    result = (result[0] - complex_num[0], result[1] - complex_num[1])
                elif operator == '*':
                    result = (
                        result[0] * complex_num[0] - result[1] * complex_num[1],
                        result[0] * complex_num[1] + result[1] * complex_num[0]
                    )
                elif operator == '/':
                    denom = complex_num[0] ** 2 + complex_num[1] ** 2
                    result = (
                        (result[0] * complex_num[0] + result[1] * complex_num[1]) / denom,
                        (result[1] * complex_num[0] - result[0] * complex_num[1]) / denom
                    )
        print(f"Result: {result[0]} + {result[1]}i")
    
    def getComplexNumber(self, ctx):
        real = int(ctx.realPart().getText())
        imag = int(ctx.imaginaryPart().getText())
        sign = ctx.sign().getText()
        if sign == '-':
            imag = -imag
        return (real, imag)

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ComplexNumbersLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexNumbersParser(stream)
    tree = parser.prog()

    listener = ComplexNumbersListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)