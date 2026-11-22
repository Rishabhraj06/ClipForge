"""Lexical tokenizer and syntax colorizer for code rendering."""

import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Token:
    text: str
    color: Tuple[int, int, int]


class SyntaxStyler:
    """Tokenizes code into styled colored spans."""

    THEME = {
        "bg": (15, 17, 26),
        "card_bg": (22, 27, 34),
        "text": (203, 213, 225),
        "keyword": (192, 132, 252),      # Purple
        "string": (134, 239, 172),       # Emerald
        "number": (251, 146, 60),        # Orange
        "comment": (100, 116, 139),      # Slate Gray
        "func": (56, 189, 248),          # Cyan
        "accent": (244, 63, 94),         # Rose
    }

    KEYWORDS = {
        "def", "class", "return", "if", "else", "elif", "for", "while",
        "in", "import", "from", "as", "try", "except", "finally",
        "with", "async", "await", "lambda", "yield", "raise", "pass"
    }

    @classmethod
    def tokenize_line(cls, line: str) -> List[Token]:
        tokens: List[Token] = []
        if not line:
            return [Token("", cls.THEME["text"])]

        # Check comment
        if "#" in line:
            idx = line.find("#")
            pre_code = line[:idx]
            comment_part = line[idx:]
            if pre_code:
                tokens.extend(cls._tokenize_code_segment(pre_code))
            tokens.append(Token(comment_part, cls.THEME["comment"]))
            return tokens

        return cls._tokenize_code_segment(line)

    @classmethod
    def _tokenize_code_segment(cls, segment: str) -> List[Token]:
        parts = re.split(r"(\"\"\"|\'\'\'|\"[^\"]*\"|\'[^\']*\'|\b\d+\b|\b\w+\b|[^\w\s])", segment)
        tokens: List[Token] = []

        for p in parts:
            if not p:
                continue

            if p in cls.KEYWORDS:
                tokens.append(Token(p, cls.THEME["keyword"]))
            elif (p.startswith('"') and p.endswith('"')) or (p.startswith("'") and p.endswith("'")):
                tokens.append(Token(p, cls.THEME["string"]))
            elif p.isdigit():
                tokens.append(Token(p, cls.THEME["number"]))
            elif p.isidentifier():
                tokens.append(Token(p, cls.THEME["text"]))
            else:
                tokens.append(Token(p, cls.THEME["text"]))

        return tokens
