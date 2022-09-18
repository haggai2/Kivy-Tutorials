import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import csv
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.effects.kinetic import KineticEffect
from kivy.base import runTouchApp

class ProfileWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass



Build_LearnAB = Builder.load_file('learnscrollview.kv')

class LearnScrollViewApp(App):
    def build(self):
        return Build_LearnAB

if __name__ == "__main__":
    LearnScrollViewApp().run()


###################
currencies = []
A1 = str(input("a1: "))
A2 = str(input("a2: "))
A3 = str(input("a3: "))
A4 = str(input("a4: "))

if A1.upper() == A3.upper():
    print("Base")

elif (A1.upper() == A4.upper() or A2.upper() == A3.upper()):
    print("Opposite")

elif A2.upper() == A4.upper():
    print("Quote")

elif (A1.upper() != A3.upper() or A1.upper() != A4.upper()) or (A2.upper() != A3.upper() or A2.upper() != A4.upper()):
    print("No")
else:
    pass

###############
B1 = str(input("B1: "))
B2 = str(input("B2: "))
B3 = str(input("B3: "))
B4 = str(input("B4: "))
B5 = str(input("B5: "))
B6 = str(input("B6: "))

C1 = str(input("C1: "))
C2 = str(input("C2: "))
C3 = str(input("C3: "))
C4 = str(input("C4: "))
C5 = str(input("C5: "))
C6 = str(input("C6: "))

counter1 = 0

if B1.upper() != C1.upper():
    counter1 = counter1+1
else:
    pass

if B2.upper() != C2.upper():
    counter1 = counter1+1
else:
    pass

if B3.upper() != C3.upper():
    counter1 = counter1+1
else:
    pass

if B4.upper() != C4.upper():
    counter1 = counter1+1
else:
    pass

if B5.upper() != B5.upper():
    counter1 = counter1+1
else:
    pass
print(counter1)
counter1 = counter1 % 2

if counter1 == 0:
    print("Even")
else:
    print("Odd")

print(type(counter1))

B7 = int(input("B7: "))
C7 = int(input("C7: "))

if B7 - C7 < 0:
    print("Ahead")
else:
    print("Behind")

print(B7-C7)

#########
D1 = ""
D2 = ""
D1 == A3
D2 == A4
D3 = str(input("D3: "))
D4 = str(input("D4: "))

if D1.upper() == D3.upper():
    print("Base")

elif (D1.upper() == D4.upper() or D2.upper() == D3.upper()):
    print("Opposite")

elif D2.upper() == D4.upper():
    print("Quote")

elif (D1.upper() != D3.upper() or D1.upper() != D4.upper()) or (D2.upper() != D3.upper() or D2.upper() != D4.upper()):
    print("No")
else:
    pass

