import kivy

from kivy.app import App
from kivy.uix.label import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder

class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.inside.add_widget(Label(text="Confirm Password: "))
        self.confirm_password = TextInput(multiline=False)
        self.inside.add_widget(self.confirm_password)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        email = self.email.text
        username = self.username.text
        password = self.password.text
        confirm_password = self.confirm_password.text

        print("\n\n\n", "\tName:", name, "\n", "Email:", email, "\n", "Username:", username, "\n", "Password:", password, "\n", "Confirm Password", confirm_password, "\n")
        self.name.text = ""
        self.email.text = ""
        self.username.text = ""
        self.password.text = ""
        self.confirm_password.text = ""

class MyKivyApp(App):

    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyKivyApp().run()


