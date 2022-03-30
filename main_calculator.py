import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi
import speech_recognition as sr
from help import Ui_MainWindow


class Myapp(QMainWindow):
    def __init__(self):
        super(Myapp,self).__init__()
        loadUi('qt_gui/main_calculator.ui',self)

        self.check = True              # this variable checks if user press some operation then equation will continue from its current otherwise equation will start from whatever user enter
        self.equation_string = "0"     #  this variable stores the equation step by step enter by user .... initially set to "0"
        self.answer = "0"               #  this variable stores the answer in string form which is initially "0"
        self.text_equ.setText(self.equation_string)   # it is box/line_edit in our window to store equation.....initially set to "0"
        self.text_ans.setText(self.answer)            # this box/line_edit in our window is used to store answer of given equation....initially set to "0"
        self.for_ans_button = ""       # this variable is just used in a comparison
        self.audio_string = ""        # this variable stores the input equation enter by microphone in text converted form
        
        
                                # Point and One to Nine buttons when pressed ..related function is called
        self.point.clicked.connect(self.Point_to_Nine_Button)
        self.b0.clicked.connect(self.Point_to_Nine_Button)
        self.b1.clicked.connect(self.Point_to_Nine_Button)
        self.b2.clicked.connect(self.Point_to_Nine_Button)
        self.b3.clicked.connect(self.Point_to_Nine_Button)
        self.b4.clicked.connect(self.Point_to_Nine_Button)
        self.b5.clicked.connect(self.Point_to_Nine_Button)
        self.b6.clicked.connect(self.Point_to_Nine_Button)
        self.b7.clicked.connect(self.Point_to_Nine_Button)
        self.b8.clicked.connect(self.Point_to_Nine_Button)
        self.b9.clicked.connect(self.Point_to_Nine_Button)
        

                                # addition,subtraction,multiplication,division buttons when pressed ..related function is called
        self.pushButton_add.clicked.connect(self.Operations)
        self.pushButton_minus.clicked.connect(self.Operations)
        self.pushButton_multiply.clicked.connect(self.Operations)
        self.pushButton_divide.clicked.connect(self.Operations)
        
        
                                 # equal ,remove,and clear buttons when pressed ..related function is called
        self.pushButton_equal.clicked.connect(self.Equal_button)
        self.pushButton_del.clicked.connect(self.Remove_button)
        self.pushButton_clear.clicked.connect(self.Clear_button)
        self.pushButton_ans.clicked.connect(self.Ans_button)
        

                        # percent  when pressed ..related function is called
        self.pushButton_percent.clicked.connect(self.Percent_button)

                        # microphoneX and help button when pressed ..related function is called
        self.pushButton_microphone.clicked.connect(self.Microphone_button)
        self.pushButton_help.clicked.connect(self.help)


        # function executed when , point and zero to nine button pressed
    def Point_to_Nine_Button(self):
        if self.equation_string == "0":
            self.equation_string = ""
        self.sending_button = self.sender()
        self.sending_button = self.sending_button.objectName()
        
        if self.sending_button == 'point':
            self.sending_button = '.'
        elif self.sending_button == 'b0':
            self.sending_button = '0'
        else:
            self.sending_button = self.sending_button[1]    # because names are b1,b1,b2 etc, it will store 0,1,2,3,4,etc
        
        if self.check:
            self.equation_string = ('%s%s'%(self.equation_string,self.sending_button))
        if not self.check:
            self.equation_string = ('%s'%(self.sending_button))

        self.text_equ.setText('%s'%(self.equation_string))
        self.check = True
        

        # function executed when any operational button is pressed
    def Operations(self):
        self.sending_button = self.sender()
        self.sending_button = self.sending_button.objectName()
        
        
        if self.sending_button == 'pushButton_divide':
            self.sending_button = '/'
        elif self.sending_button == 'pushButton_multiply':
            self.sending_button = '*'
        elif self.sending_button == 'pushButton_add':
            self.sending_button = "+"
        else:
            self.sending_button = '-'

        if  self.equation_string[-1] == "*" or self.equation_string[-1] == "/" or self.equation_string[-1] == "+" or self.equation_string[-1] == "-" and self.equation_string != '':
            list_of_string = list(self.equation_string) # this list is used to replace an operation if again an operation is typed
            list_of_string[-1] = ""               #it will remove last operation and place new pressed operation
            list_of_string.append(self.sending_button)
            self.equation_string = "".join(list_of_string)
            self.equation_string = ('%s'%(self.equation_string))
            self.text_equ.setText('%s'%(self.equation_string))
        else:
            self.equation_string = ('%s%s'%(self.equation_string,self.sending_button))
            self.text_equ.setText('%s'%(self.equation_string))
        
        self.check = True
        
        
            # function executed when percent butten is pressed
    def Percent_button(self):
        if self.equation_string !='' and (self.equation_string[-1] == "*" or self.equation_string[-1] == "/" or self.equation_string[-1] == "+" or self.equation_string[-1] == "-"):
            list_string = list(self.equation_string)
            list_string[-1] = ""
            list_string.append("%")
            self.equation_string = "".join(list_string)
            self.text_equ.setText(self.equation_string)
        else:
            self.symbol = '%'
            self.equation_string = ('%s%s'%(self.equation_string,self.symbol))
            self.text_equ.setText(self.equation_string)
        self.check = True


        # function executed when clear_screen butten is pressed to clear both equation and answer screen
    def Clear_button(self):
        self.equation_string = "0"
        self.answer = "0"
        self.audio_string = ""
        self.text_equ.setText(self.equation_string)
        self.text_ans.setText(self.answer)


        # function executed when del butten is pressed to delete last entry currently pressed
    def Remove_button(self):
        self.equation_string = self.equation_string[:-1]
        if self.equation_string == "":
            self.equation_string = "0"
        self.text_equ.setText(self.equation_string)


        # function executed when Ans butten is pressed to add the current answer in equation
    def Ans_button(self):
        if self.equation_string == "0" or self.equation_string == self.for_ans_button or self.equation_string[-1] in "0123456789.":
            self.equation_string = str(self.answer)
            self.text_equ.setText(self.equation_string)
        else:
            self.equation_string = ('%s%s'%(self.equation_string,str(self.answer)))
            self.text_equ.setText(self.equation_string)


            # function executed when equal butten is pressed to solve the equation and place answer in answer box of window
    def Equal_button(self):
        if self.equation_string == '':
            self.text_ans.setText(str(self.answer))
        else:
            try: 
                self.new_equation_string = self.equation_string + " "   # self.new_equation_string is a copy of equation_string so that when we work on symbols in it our original equation remain same
                list_str = []                                          # this list will contain solvable string......like % is not directly solvabe by python it must be converted into 1/100
                            # this loop will convert equation with operational symbols into solvable equation e.g(1% into 1*1/100)
                for i in range(len(self.new_equation_string)-1):
                    if self.new_equation_string[i] == "%" and self.new_equation_string[i+1] in "0123456789.":
                        i="*1/100*"
                        list_str.append(i)
                    elif self.new_equation_string[i] == "%":
                        i = "*1/100"
                        list_str.append(i)
                    else:
                        i = self.new_equation_string[i]
                        list_str.append(i)
                self.new_equation_string = "".join(list_str)

                            # here octal removal function is called to remove octal values from given equation
                self.new_equation_string = self.octal_removal(self.new_equation_string)
                self.answer = eval(self.new_equation_string)
                self.text_ans.setText(str(round(self.answer,10)))
            except ZeroDivisionError:
                self.text_ans.setText("Zero Division Error")     # if zero division error occur
            except:
                self.text_ans.setText("Wrong Expression")     # if wrong expresion is given
            self.for_ans_button = self.equation_string
            self.check = False
    
    
            # this function is converting octal values to numerical values because octal values can't be evaluated directly with numerical values
    def octal_removal(self,equation_string):
        self.string = equation_string         # original expression
        self.string_without_octal = ""        # expression without octal values
        self.num = []                         # this list will contain string elements which are non_octal_values  and opeartions
        
        # loop through every single element
        for i in range(len(self.string)):
            while True:
                if self.string_without_octal.startswith('0'):          # this function  is checking if a certain operand starts with "0"...mean octal value
                    self.string_without_octal = self.string_without_octal.replace("0","")        # it will replace starting zero with "" and store that single complete value in it
                else:
                    break
            if self.string[i] == "+" or self.string[i] == "-" or self.string[i] == "/" or self.string[i] == "*" or self.string[i] == "%":
                if self.string_without_octal == "" and self.string[i-1] != "/" and self.string[i-1] != "*":
                    self.string_without_octal = "0"
                self.string_without_octal+=self.string[i]          # it will store operation in non_octal string if any found
                self.num.append(self.string_without_octal)          # it is storing every single complete value and every single operation
                self.string_without_octal=""                     #at this point string have nothing to make sure that next value or operation to be store is without any garbage value
            else:
                self.string_without_octal+=self.string[i]          # this line is storing every single character from or expression to string without octals
        self.num.append(self.string_without_octal)
        self.string_without_octal = "".join(self.num)         # it will convert num_list which is without octal values to a string(expression) that we want to solve
        return self.string_without_octal                 # finally returning it in equal_button function to evaluate it


        # function executed when microphone button is pressed to get audio input and convert it in required equation
    def Microphone_button(self):
        ans=""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            self.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
            audio = r.listen(source)
            said = ''
            try: 
                said = r.recognize_google(audio,language="en")
            except:
                self.text_equ.setText("Voice Error Speak Again")
            self.audio_string = said
            self.audio_string = self.audio_string.replace('percent', "%")
            self.audio_string = self.audio_string.replace('x', "*")
            self.audio_string = self.audio_string.replace('divided', "")
            self.audio_string = self.audio_string.replace('plus', "+")
            self.audio_string = self.audio_string.replace('add', "+")
            self.audio_string = self.audio_string.replace('minus', "-")
            self.audio_string = self.audio_string.replace('by', "over")
            self.audio_string = self.audio_string.replace('over', "/")
            self.audio_string = self.audio_string.replace('is', "")
            self.audio_string = self.audio_string.replace('what', "")
            self.audio_string = self.audio_string.replace('What', "")
            self.audio_string = self.audio_string.replace('answer',self.answer)
            self.audio_string = self.audio_string.replace('Answer', self.answer)
            self.audio_string = self.audio_string.replace('ans', self.answer)

            self.new_audio_string = self.audio_string + " "
            list_string = []  # this list will contain solvable string......like % is not directly solvabe by python it must be converted into 1/100
                     # this loop will convert equation with operational symbols into solvable equation e.g(1% into 1*1/100)
            for i in range(len(self.new_audio_string) - 1):
                if self.new_audio_string[i] == "%" and self.new_audio_string[i + 1] in "0123456789.":
                    i = "*1/100*"
                    list_string.append(i)
                elif self.new_audio_string[i] == "%":
                    i = "*1/100"
                    list_string.append(i)
                else:
                    i = self.new_audio_string[i]
                    list_string.append(i)
            self.new_audio_string = "".join(list_string)
            self.audio_string = self.audio_string.replace('one', "1")
            self.new_audio_string = self.new_audio_string.replace('one', "1")
            self.text_equ.setText(self.audio_string)
            try:
                ans = str(eval(self.new_audio_string))
                self.text_ans.setText(ans)
            except:
                if self.audio_string == "" or self.audio_string == "Voice Error Speak Again":
                    self.text_ans.setText("")
                else:
                    self.text_ans.setText("Wrong Expression")
            self.equation_string = self.audio_string
            self.answer = ans


    def help(self):
        self.help = QMainWindow()
        self.help_ui = Ui_MainWindow()
        self.help_ui.setupUi(self.help)
        self.help.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())