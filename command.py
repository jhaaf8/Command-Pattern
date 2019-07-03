#code and annotations by Jacob Haaf-Murphy

#lists to use as stacks to implement undo/redo
undoStack = []
redoStack = []

class Command: 

    #append char to a string + put appropriate strings on stacks
    def append(self, char, string):
        undoStack.append(string)
        string += char
        redoStack.append(string)
        print(string)
        #strings are immutable in python so have to print results within methods

    #delete first char of a string + put appropriate strings on stacks
    def deleteStart(self, string):
        undoStack.append(string)
        string = string[1:]
        redoStack.append(string)
        print(string)
        
    #delete last char of a string + put appropriate strings on stacks
    def deleteEnd(self, string):
        undoStack.append(string)
        string = string[:-1]
        redoStack.append(string)
        print(string)
    
    #capitalize letter of string at index + put appropriate strings on stacks
    def capitalizeIndex(self, string, index):
        undoStack.append(string)
        string = string[:index] + string[index].upper() + string[index + 1:]
        redoStack.append(string)
        print(string)

    #lowercase letter of string at index + put appropriate strings on stacks
    def lowercaseIndex(self, string, index):
        undoStack.append(string)
        string = string[:index] + string[index].lower() + string[index + 1:]
        redoStack.append(string)
        print(string)

    #make entire string title case + put appropriate strings on stacks
    def titleCase(self, string):
        undoStack.append(string)
        string = string.title()
        redoStack.append(string)
        print(string)

    #undo last action made in command class using lists
    def undo(self):
        data = undoStack.pop()
        print(data)
        redoStack.append(data)

    #redo last undone action in command class using lists
    def redo(self):
        data = redoStack.pop()
        print(data)
        undoStack.append(data)