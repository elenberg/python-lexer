from lexical_analyzer import TokensList
import re


class SyntaxAnalyzer():

    assignments = ['==', '+=', '-=', '*=', '=', '/=']
    operators = ['+', '-', '*', '/']
    defs = ['class', 'def']

    def __init__(self, tokens):
        self.tokens = tokens

    def valid_literal(self, token):
        if token.startswith('\''):
            q = []
            for item in token:
                if re.search('\'', item) is not None:
                    if q == []:
                        q.append(item)
                    else:
                        q.pop()
            return len(q) == 0
        elif token.startswith('\"'):
            q = []
            for item in token:
                if re.search('\"', item) is not None:
                    if q == []:
                        q.append(item)
                    else:
                        q.pop()
                print q
            print len(q) == 0
            return len(q) == 0

        return True

    def check_valid(self):
        syntax_check = True
        for i in xrange(len(self.tokens)):
            if self.tokens[i][0] is 'LIT':
                if not self.valid_literal(self.tokens[i][1]):
                    print "ERROR INVALID LITERAL", self.tokens[i]
                    syntax_check = False
            elif self.tokens[i][0] is 'PUNCT':
                    if self.valid_punct(i) is False:
                        syntax_check = False
            elif self.tokens[i][0] is 'KEYWORD':
                    if not self.valid_keyword(i):
                        syntax_check = False
        if self.check_parens() is False:
            print "ERROR {([ must be BALANCED by an equal })]"
            return False
        return syntax_check

    def valid_keyword(self, i):
        if self.tokens[i][1] in self.defs:
            if i == len(self.tokens) - 1:
                print "ERROR DEFINITION MUST BE FOLLOWED BY AN ID", self.tokens[i]
                return False
            if self.tokens[i + 1][0] is not 'ID':
                print "ERROR DEFINITION MUST BE FOLLOWED BY AN ID", self.tokens[i]
                return False
        return True

    def valid_punct(self, i):
        if self.tokens[i][1] in self.assignments:
            checker = True
            if i == 0 or i == len(self.tokens) - 1:
                checker = False
            elif self.tokens[i - 1][0] is not 'ID':
                checker = False
            elif self.tokens[i + 1][1] is '-':
                if self.tokens[i + 2][0] is not 'LIT':
                    checker = False
            elif self.tokens[i + 1][0] not in ['LIT', 'ID']:
                    checker = False
            if checker is False:
                print "ERROR ASSIGNEMT MUST BE IN FORMAT ID ASSIGNMENT ID/LIT", self.tokens[i]
        if self.tokens[i][1] in self.operators:
            checker = True
            if i == 0 or i == len(self.tokens) - 1:
                checker = False
            elif self.tokens[i - 1][0] not in ['ID', 'LIT']:
                checker = False
            elif self.tokens[i + 1][1] is '-':
                if self.tokens[i + 2][0] is not 'LIT':
                    checker = False
            elif self.tokens[i + 1][0] not in ['LIT', 'ID']:
                    print self.tokens[i + 1]
                    checker = False
            if checker is False:
                print "ERROR OPERATORS MUST BE IN FORMAT ID/LIT ASSIGNMENT ID/LIT", self.tokens[i]
        return True

    def check_parens(self):
        counter = []
        for item in self.tokens:
            if item[1] is '(':
                counter.append('(')
            if item[1] is ')':
                if '(' in counter:
                    counter.remove('(')
                else:
                    return False
            if item[1] is '{':
                counter.append('{')
            if item[1] is '}':
                if '{' in counter:
                    counter.remove('{')
                else:
                    return False
            if item[1] is '[':
                counter.append('[')
            if item[1] is ']':
                if '[' in counter:
                    counter.remove('[')
                else:
                    return False
        return counter == []

t = TokensList('input.py')
s = SyntaxAnalyzer(t.get_tokens())
s.check_valid()
