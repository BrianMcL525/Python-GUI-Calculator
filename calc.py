"""
Program: calc.py
Author: Brian McLaughlin

Gui operatered calcuator that adds

1. CE : clears all stored and displayed numbers
2. C : clears the current display of numbers
3. Back : clears the last number entered
4. 0-9 : adds that value to the string
5. + : stores current display and clears the input field
6. = : stores the current string into a variable and adds the num2 string and the previous stored string together

"""
#importing class EasyFrame from the breezypythongui file
from breezypythongui import EasyFrame

#constructiong the calc class
class Calc(EasyFrame):
    """Does additon"""
    
    def __init__(self):
        #variables to be used in multiple functions
        self.display = ""
        self.num1 = 0

        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Text Field Demo")
        #input field that will display the result, also styling the field
        self.sumField = self.addTextField(text = "", row =0, column = 0, width = 21, columnspan = 3)
        self.sumField["background"] = "black"
        self.sumField["foreground"] = "white"

        #First column/ buttons for clear line, Clear entire and back, also styling for the buttons 
        self.buttonC = self.addButton(text = "C", row = 1, column = 0, command  = self.pressC)
        self.buttonC["width"] = 4
        self.buttonC["height"] = 1
        
        self.buttonCE = self.addButton(text = "CE", row =1, column = 1, command = self.pressCE)
        self.buttonCE["width"] = 4
        self.buttonCE["height"] = 1
        
        self.buttonBack = self.addButton(text = "BACK", row =1, column =2, command = self.pressBack)
        self.buttonBack["width"] = 4
        self.buttonBack["height"] = 1
        #Second column/ buttons for 7 8 9, also styling each button
        self.button7 = self.addButton(text = "7", row = 2, column = 0, command = self.press7)
        self.button7["width"] = 4
        self.button7["height"] = 1

        self.button8 = self.addButton(text = "8", row = 2, column = 1, command = self.press8)
        self.button8["width"] = 4
        self.button8["height"] = 1
        
        self.button9 = self.addButton(text = "9", row = 2, column = 2, command = self.press9)
        self.button9["width"] = 4
        self.button9["height"] = 1
        #Third column/ buttons for 4 5 6, also styling each button
        self.button4 = self.addButton(text = "4", row = 3, column = 0, command = self.press4)
        self.button4["width"] = 4
        self.button4["height"] = 1

        self.button5 = self.addButton(text = "5", row = 3, column = 1, command = self.press5)
        self.button5["width"] = 4
        self.button5["height"] = 1

        self.button6 = self.addButton(text = "6", row = 3, column = 2, command = self.press6)
        self.button6["width"] = 4
        self.button6["height"] = 1

        #Fourth column/ buttons for 1 2 3 also styling each button
        self.button1 = self.addButton(text = "1", row = 4, column = 0, command = self.press1)
        self.button1["width"] = 4
        self.button1["height"] = 1

        self.button2 = self.addButton(text = "2", row = 4, column = 1, command = self.press2)
        self.button2["width"] = 4
        self.button2["height"] = 1

        self.button3 = self.addButton(text = "3", row = 4, column = 2, command = self.press3)
        self.button3["width"] = 4
        self.button3["height"] = 1
        
        #Fifth column/ buttons +, 0 , =, also styling each button
        self.buttonPlus = self.addButton(text = "+", row = 5, column = 0, command = self.pressPlus)
        self.buttonPlus["width"] = 4
        self.buttonPlus["height"] = 1
   
        self.button0 = self.addButton(text = "0", row = 5, column = 1, command = self.press0)
        self.button0["width"] = 4
        self.button0["height"] = 1

        self.buttonEqual = self.addButton(text = "=", row = 5, column = 2, command = self.pressEqual)
        self.buttonEqual["width"] = 4
        self.buttonEqual["height"] = 1

    #functions that add the value pressed to the display string, and outputs the string
    def press0(self):
        self.display += "0"
        self.sumField.setText(self.display)
        
    def press1(self):
        self.display += "1"
        self.sumField.setText(self.display)

    def press2(self):
        self.display += "2"
        self.sumField.setText(self.display)

    def press3(self):
        self.display += "3"
        self.sumField.setText(self.display)

    def press4(self):
        self.display += "4"
        self.sumField.setText(self.display)

    def press5(self):
        self.display += "5"
        self.sumField.setText(self.display)

    def press6(self):
        self.display += "6"
        self.sumField.setText(self.display)

    def press7(self):
        self.display += "7"
        self.sumField.setText(self.display)

    def press8(self):
        self.display += "8"
        self.sumField.setText(self.display)

    def press9(self):
        self.display += "9"
        self.sumField.setText(self.display)
    #end of functions that add to the string 

    #function that turns the display string into an int and stores it in the num1 varaible, then resets display to an empty string and outputs display
    def pressPlus(self):
        self.num1 = int(self.display)
        self.display = ""
        self.sumField.setText(self.display)
    
    #function that runs when equal is clicked and turns display into an int and adds together the new int and the variable from "pressPlus", then out puts the result after turning it into a string
    def pressEqual(self):
        num2 = int(self.display)
        total = self.num1 + num2
        self.result = str(total)
        self.sumField.setText(self.result)
    
    #Restores all variables to have no value, and clears the "sumField"
    def pressCE(self):
        self.num1 = 0
        self.display = ""
        self.result = ""
        self.sumField.setText(self.display)
    
    #turns "display" into a list then takes the last character out of the list and rebuilds the string with concatination
    def pressBack(self):
        charList = list(self.display)
        del(charList[-1])
        self.display = ""
        for char in range(len(charList)):
            self.display = self.display + charList[char]
        self.sumField.setText(self.display)
    
    #clears the current display string
    def pressC(self):
        self.display = ""
        self.sumField.setText(self.display)

#function to call the class
def main():
    Calc().mainloop()

#call to main and executes the program
main()