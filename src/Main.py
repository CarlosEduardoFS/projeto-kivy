from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button

Builder.load_file('view/cadastro.kv') 

class Main(Widget):
    pass
class MainApp(App):
    def build(self):
        return Main()  

MainApp().run()