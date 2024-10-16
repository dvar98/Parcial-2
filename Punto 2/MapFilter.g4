grammar MapFilter;

// Parser rules
prog: expr+ EOF;

expr: mapExpr | filterExpr;

mapExpr: 'MAP' '(' function ',' iterable ')';
filterExpr: 'FILTER' '(' function ',' iterable ')';

function: NAME;

iterable: list | tuple | NAME;

list: '[' elements? ']';
tuple: '(' elements? ')';

elements: element (',' element)*;
element: NUMBER | NAME;

NAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;