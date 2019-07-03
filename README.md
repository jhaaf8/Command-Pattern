# Command-Pattern
example of the command pattern in python to implement undo and redo along with some methods to manipulate and print strings

#append char to a string + put appropriate strings on stacks
    def append(self, char, string):
    
#delete first char of a string + put appropriate strings on stacks
    def deleteStart(self, string):
    
#delete last char of a string + put appropriate strings on stacks
    def deleteEnd(self, string):    
    
#capitalize letter of string at index + put appropriate strings on stacks
    def capitalizeIndex(self, string, index):
    
#lowercase letter of string at index + put appropriate strings on stacks
    def lowercaseIndex(self, string, index):
    
#make entire string title case + put appropriate strings on stacks
    def titleCase(self, string):
    
#undo last action made in command class using lists
    def undo(self):
    
#redo last undone action in command class using lists
    def redo(self):
