from kivy.app import App

#Builder allows us to call another file such as our kv file
from kivy.lang import Builder

#BoxLayout allows us to use this layout
from kivy.uix.boxlayout import BoxLayout

#Random allows us to use random choice and other random triggers
import random

#Allows us to trigger window size or make the app full screen
from kivy.core.window import Window

#Setting the size of the window that opens
Window.fullscreen = 'auto'

#Deciding if user can resize the window or not
from kivy.config import Config
Config.set('graphics', 'resizable', True)  

#Importing a CSV
import csv   

class Idiom_Generation(BoxLayout):                                     
#Male Name Generation               
    def Idiom_Gen(self, *args):
        Idiom = []
        with open(r'Idioms.csv', encoding="utf8") as f:
            reader = csv.reader(f, skipinitialspace=True)         
            for col in reader: 
                ##This verifies it doesn't get a blank or the column title and if it does it continues until it doesn't get a blank
                if not col[1] or col[1] == "Field": continue
                else:
                #This appends column 0 to First_Name
                    Idiom.append(col[1])

#Print a random first and last name for Males 
        self.ids.Char_Name.text = " ".join([random.choice(Idiom)])

#Clears what is showing on the main_label of the application   
    def clear(self, *args):
        self.ids.Char_Name.text = ''



class app1(App):

    def build(self):
        return Builder.load_file('Idiom_Generator.kv') 

if __name__=="__main__":
    app1().run()