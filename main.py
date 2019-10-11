from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
import kivy
# import loginScreen.LoginScreen

kivy.require("1.11.1")


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.goLoginScreen=Button(text="button1")
        self.goLoginScreen.bind(on_press=self.pressLoginScreen)
        self.add_widget(self.goLoginScreen)

    def pressLoginScreen(self, instance):
        print("hello")

class MyApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MyApp().run()
