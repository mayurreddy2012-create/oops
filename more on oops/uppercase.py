class IOSstring():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("enter String: ")
    def print_String(self):
        print("Result is: ", self.str1.upper())

str1 = IOSstring()

str1.get_String()
str1.print_String()