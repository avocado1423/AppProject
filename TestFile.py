import kivy

from kivy.app import App
from kivy.uix.label import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name:", self.name.text, "Email:", self.email.text)
        self.name.text = ""
        self.email.text = ""

class TestFile(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    TestFile().run()