# Trabalho feito por: Leonardo Silva Vieira
#                     Marco Antonio de Abreu Barbosa
#                     Renan Aguiar Chagas

# Parte 1 -- Analisador lexico
import re
from sys import argv


token_start = 0
token_flag = 0

ws = re.compile(r"[ \n\t]*")
def ignore_space(string: str, inicial: int):
    foo = ws.match(string, inicial)
    if "\n" in foo[0]:
        global token_flag
        token_flag = 0 + len(foo[0]) - 1
    return len(foo[0]) 

tokens = {"ReservedWords"   : re.compile(r"fn|main|let|int|float|char|if|else|while|print|println|return",), 
          "Identifier"      : re.compile(r"[a-zA-Z][a-zA-Z0-9_]*"),
          "Punctuation"     : re.compile(r"\(|\)|->|:|,|\{|\}|\.|;"),
          "Operators"       : re.compile(r"=|==|!=|>|>=|<|<=|\+|\-|\*|\/"),
          "CharConst"       : re.compile(r"'[^']'"),
          "IntConst"        : re.compile(r"[0-9]([0-9])*"),
          "FloatConst"      : re.compile(r"[0-9]([0-9])*.[0-9]([0-9])*"),
          "FormattedString" : re.compile(r"\"\{\}\""),
          "Errors"          : re.compile(r"[^a-zA-Z0-9_]"),
          }

punctuation = {
        "("     : "LParen",
        ")"     : "RParen",
        "->"    : "Arrow",
        ":"     : "Colon",
        ","     : "Comma",
        "{"     : "LBrace",
        "}"     : "RBrace",
        "."     : "Period",
        ";"     : "Semicolon"
        }
operators = {
        "="     : "Assign",
        "=="    : "Equal",
        "!="    : "NotEqual",
        ">"     : "GreaterThan",
        ">="    : "GreaterThanEqual",
        "<"     : "LessThan",
        "<="    : "LessThanEqual",
        "+"     : "Plus",
        "-"     : "Minus",
        "*"     : "Multiplication",
        "/"     : "Division",
        }
reserved = {
        "fn"        : "Function",
        "main"      : "Main",
        "let"       : "Let",
        "int"       : "Int",
        "float"     : "Float",
        "char"      : "Char",
        "if"        : "If",
        "else"      : "Else",
        "while"     : "While",
        "print"     : "Print",
        "println"   : "Println",
        "return"    : "Return",
        }

token_list = []
with open(argv[1], "r") as f:
    string_source = f.read()

while True:
    for name, token in tokens.items():
        token_flag = token_flag + ignore_space(string_source, token_start)
        token_start += ignore_space(string_source, token_start)
        match = token.match(string_source, token_start)
        if not match:
            continue

        token_start = token_start + len(match[0])
        token_flag = token_flag + len(match[0])
        aux = match[0]
        if name == "Punctuation":
            aux = punctuation[match[0]]
        if name == "Operators":
            aux = operators[match[0]]
        if name == "ReservedWords":
            aux = reserved[match[0]]
        token_list.append([{name: aux}, token_flag, token_flag + len(match[0])])
        break

    if token_start >= len(string_source) - 1:
        break

print(f"{token_list}")

# Parte 2 -- Analisador sintatico

