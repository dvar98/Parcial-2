grammar FourierTransform;

// Parser rules
prog: stmt+ EOF;

stmt: fourierTransformStmt | pairTransformStmt;

fourierTransformStmt: 'FOURIER' '(' iterable ')';
pairTransformStmt: 'PAIRTRANSFORM' '(' iterable ')';

iterable: list | tuple | NAME;

list: '[' elements? ']';
tuple: '(' elements? ')';

elements: element (',' element)*;
element: NUMBER | variable;

variable: NAME;

NUMBER: [0-9]+ ('.' [0-9]+)?;
NAME: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t\r\n]+ -> skip;