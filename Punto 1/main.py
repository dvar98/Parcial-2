import sys
from antlr4 import *
from ComplexNumbersLexer import ComplexNumbersLexer
from ComplexNumbersParser import ComplexNumbersParser

class ComplexNumbersListener(ParseTreeListener):
    def enterExpr(self, ctx:ComplexNumbersParser.ExprContext):
        result = None
        for i in range(0, len(ctx.children), 2):
            term = self.getTerm(ctx.getChild(i))
            if result is None:
                result = term
            else:
                operator = ctx.getChild(i-1).getText()
                if operator == '+':
                    result = (result[0] + term[0], result[1] + term[1])
                elif operator == '-':
                    result = (result[0] - term[0], result[1] - term[1])
                elif operator == '*':
                    result = (
                        result[0] * term[0] - result[1] * term[1],
                        result[0] * term[1] + result[1] * term[0]
                    )
                elif operator == '/':
                    denom = term[0] ** 2 + term[1] ** 2
                    result = (
                        (result[0] * term[0] + result[1] * term[1]) / denom,
                        (result[1] * term[0] - result[0] * term[1]) / denom
                    )
        print(f"Result: {result[0]} + {result[1]}i")

    def getTerm(self, ctx):
        text = ctx.getText()
        if 'i' in text:
            # Handle complex number
            return self.parseComplexNumber(text)
        else:
            # Handle real number
            return (int(text), 0)

    def parseComplexNumber(self, text):
        import re
        text = text.replace(" ", "")
        if text == "i":
            return (0, 1)
        elif text == "-i":
            return (0, -1)
        match = re.match(r'\((\-?\d*)i\)', text)
        if match:
            real = 0
            imag = int(match.group(1) or "1")
            return (real, imag)
        match = re.match(r'\((\-?\d+)\s*([\+\-]\s*\d+)i\)', text)
        if match:
            real = int(match.group(1))
            imag = int(match.group(2).replace(" ", ""))
            return (real, imag)
        else:
            raise ValueError(f"Invalid complex number format: {text}")

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