grammar ComplexNumbers;

// Parser rules
prog: expr+ EOF;

expr: term (op term)*;

term: complexNumber | realNumber;

complexNumber: '(' realPart? (sign? imaginaryPart 'i')? ')';

realNumber: NUMBER;

realPart: NUMBER;
imaginaryPart: NUMBER;
sign: '+' | '-';
op: '+' | '-' | '*' | '/';

// Lexer rules
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;