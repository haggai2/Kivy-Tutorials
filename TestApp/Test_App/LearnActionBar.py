import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import csv
import os.path
from kivymd.theming import ThemeManager
from kivy.uix.slider import Slider
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionBarException
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionItem
from kivy.uix.actionbar import ActionButton
from kivy.utils import get_color_from_hex
        


class LoginWindow(Screen):
    
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginbtn(self):
        destination = "/Users/foxcoding/Desktop/TestApp/CSV/"
        
        with open (destination + 'VALIDATE.csv', 'w')as userinfo:
            writer = csv.writer(userinfo, dialect = 'excel')
            writer.writerow(['EMAIL', 'PASSWORD'])
            writer.writerow(['Fox', 'Coding'])

            
        with open(destination + 'VALIDATE.csv', 'r') as userlog:
            Lgin = False
            em = self.email.text
            pw = self.password.text
            reader = csv.reader(userlog, dialect = 'excel')
            for row in reader:
                if (row[0] != em) or (row[1] != pw):
                    Lgin = False
                else:
                    print('email:', row[0], 'password:', row[1])
                    Lgin = True
                    break
                
            if Lgin == True:
                return True
            if Lgin == False:
                return False

class ProfileWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

Build_LearnAB = Builder.load_file('learnactionbar.kv')

class LearnActionBarApp(App):
    def build(self):
        return Build_LearnAB

if __name__ == "__main__":
    LearnActionBarApp().run()



