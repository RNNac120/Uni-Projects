# Trabalho feito por: Leonardo Silva Vieira
#                     Marco Antonio de Abreu Barbosa
#                     Renan Aguiar Chagas

# Parte 1 -- Analisador lexico
import re
from sys import argv

ws = re.compile(r"[ \t\n]*")
def ignore_space(string: str, inicial: int):
    foo = ws.match(string, inicial)
    return inicial + len(foo[0]) 

tokens = {"ReservedWords"   : re.compile(r"fn|main|let|int|float|char|if|else|while|print|println|return",), 
          "Identifier"      : re.compile(r"[a-zA-Z][a-zA-Z0-9_]*"),
          "Punctuation"     : re.compile(r"\(|\)|->|:|,|\{|\}|\.|;"),
          "Operators"       : re.compile(r"=|==|!=|>|>=|<|<=|\+|\-|\*|\/"),
          "CharConst"       : re.compile(r"'[^']'"),
          "IntConst"        : re.compile(r"[0-9]([0-9])*"),
          "FloatConst"      : re.compile(r"[0-9]([0-9])*.[0-9]([0-9])*"),
          "FormattedString" : re.compile(r"\"\{\}\""),
}

token_start = 0
token_list = []
with open(argv[1], "r") as f:
    string_source = f.read()

while True:
    for name, token in tokens.items():
        token_start = ignore_space(string_source, token_start)
        match = token.match(string_source, token_start)
        if not match:
            continue
        token_list.append([{name: match[0]},token_start, token_start + len(match[0])])
        token_start = token_start + len(match[0])
        break
    print(f"{token_list}")

    if token_start >= len(string_source) - 1:
        break

print(f"{token_list}")


# Parte 2 -- Analisador sintatico
