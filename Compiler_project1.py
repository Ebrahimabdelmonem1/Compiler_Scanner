import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class LexicalAnalyzer:
    def __init__(self, input):
        self.input = input
        self.current_char = input[0]
        self.position = 0

    def advance(self):
        self.position += 1
        if self.position < len(self.input):
            self.current_char = self.input[self.position]
        else:
            self.current_char = None

    def is_whitespace(self, char):
        return re.match(r'\s', char)

    def is_letter(self, char):
        return re.match(r'[a-zA-Z]', char)

    def is_digit(self, char):
        return re.match(r'\d', char)

    def is_operator(self, char):
        operators = ['+', '-', '=', '<', '>', '==', '!=', '<=', '>=']
        if char in operators:
            return True
        else:
            return False

    def get_next_token(self):
        while self.current_char is not None:
            if self.is_whitespace(self.current_char):
                self.advance()
                continue

            elif self.is_letter(self.current_char):
                keywords = [
                    'int','False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
                    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally',
                    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'None',
                    'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield','long']
                letter = ''
                while self.is_letter(self.current_char) or self.is_digit(self.current_char):
                    letter += self.current_char
                    self.advance()

                if letter in keywords:
                    return Token('KEYWORD', letter)
                else:
                    return Token('IDENTIFIER', letter)

            elif self.is_digit(self.current_char):
                number = ''
                while self.is_digit(self.current_char):
                    number += self.current_char
                    self.advance()
                return Token('NUMBER', number)

            elif self.is_operator(self.current_char):
                operator = ''
                while self.is_operator(self.current_char):
                    operator += self.current_char
                    self.advance()
                return Token('OPERATOR', operator)

            else:
                special_char = self.current_char
                self.advance()
                return Token('SPECIAL_CHAR', special_char)

        return Token('EOF', None)


input_code = input('Please enter the statement\n')
lexer = LexicalAnalyzer(input_code)
print('*' * 50)

t_name, t_type = [], []
token = lexer.get_next_token()
while token.type != 'EOF':
    t_name.append(token.value)
    t_type.append(token.type)
    print(f'<Token Type: {token.type} , Value: {token.value}>')
    token = lexer.get_next_token()

print('*' * 50)
print(t_name, '\n', t_type)
print('*' * 50)


input("\nPress Enter to exit...")
