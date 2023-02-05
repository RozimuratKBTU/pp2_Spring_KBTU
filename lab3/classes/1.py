class String():
    def __init__(self):
        self.str = ''

    def get_String(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())
    pass

str = String()

str.get_String()
str.print_string()