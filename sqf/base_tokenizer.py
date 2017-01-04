from sqf.tokenizer_source.tokenize import tokenize as raw_tokenize


def tokenize(statement):
    tokens = raw_tokenize(statement, ('"', ' ', '<=', '>=', '=', '==', '{', '}',
                                      '(', ')', '[', ']', ';', ',', '!', '!=', '/*', '*/', '//', '\n'))

    return [token for token in tokens if token]