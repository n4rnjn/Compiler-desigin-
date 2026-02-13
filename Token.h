// Token.h

#ifndef TOKEN_H
#define TOKEN_H

#include <string>

enum class TokenType {
    IDENTIFIER,
    KEYWORD,
    LITERAL,
    OPERATOR,
    PUNCTUATION,
    END_OF_FILE
};

struct Token {
    TokenType type;
    std::string lexeme;
    int line;
};

#endif // TOKEN_H
