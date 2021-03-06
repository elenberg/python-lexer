# Everett Lenberg
# A02044266

import re


class Token():

    keywords = ['and', 'del', 'from', 'not', 'while',
                'as', 'elif', 'global', 'or', 'with',
                'assert', 'else', 'if', 'pass', 'yield',
                'break', 'except', 'import', 'print',
                'class', 'exec', 'in', 'raise',
                'continue', 'finally', 'is', 'return',
                'def', 'for', 'lambda', 'try']
    id_lex = '[A-Za-z_][A-Za-z_0-9]*'

    delim = ['\(', '\)', '\[', '\]', '\{', '\}',
             '\=\=', '\+\=', '\-\=', '\*\=', '\-',
             '\*', '\+', '\/', ':', ',']

    combined_keywords = "(" + "|".join(keywords) + ")"
    combined_delim = "(" + "|".join(delim) + " )"

    def __init__(self, token):
        self.tokens = self.find_tokens(token)
        self.tokens = self.get_token_types()

    def find_tokens(self, token):
        general = re.split(self.combined_delim, token)
        results = []
        # ID Split rules.
        for item in general:
            if re.search('[A-Za-z]+[\dA-Za-z]*\.', item) is not None:
                item = re.split('(\.)', item)
                results.extend(item)
            elif re.search('\.[A-Za-z]+[\dA-Za-z]*', item) is not None:
                item = re.split('(\.)', item)
                results.extend(item)
            elif re.search('[A-Za-z]+[\dA-Za-z]*,', item):
                item = re.split('(,)', item)
                results.extend(item)
            else:
                results.append(item)
        return results

    def get_tokens(self):
        return self.tokens

    def get_token_types(self):
        results = []
        for token in self.tokens:
            if self.is_keyword(token):
                results.append(('KEYWORD', token))
            elif self.is_lit(token):
                results.append(('LIT', token))
            elif self.is_punct(token):
                results.append(('PUNCT', token))
            elif self.is_id(token):
                results.append(('ID', token))
            else:
                if len(token) > 0:
                    results.append(('ERROR', token))
        return results

    def print_tokens(self):
        for item in self.tokens:
            print '{} {}'.format(item[0], item[1])

    def is_keyword(self, token):
        if token in self.keywords:
            return True
        return False

    def is_punct(self, token):
        if re.search('^\W', token) is not None:
            return True
        return False

    def is_id(self, token):
        if re.search(self.id_lex, token) is not None:
            return True
        return False

    def is_lit(self, token):
        if re.search('^[\'\"\d]', token) is not None:
            return True
        return False


class TokensList():

    def __init__(self, filename):
        self.filename = filename
        self.tokens = self.readfile()

    def readfile(self):
        f = open(self.filename, 'r')
        results = []
        for line in f.readlines():
            individuals = line.split()
            if '#' in individuals:
                del individuals[individuals.index('#'):]
            for i in individuals:
                results.append(Token(i))
        return results

    def print_tokens(self):
        for token in self.tokens:
            token.print_tokens()
        print "{}".format('ENDMARKER')

    def get_tokens(self):
        results = []
        for token in self.tokens:
            results.extend(token.get_tokens())
        return results

t = TokensList('input.py')
print t.print_tokens()


# Everett Lenberg
# A02044266
