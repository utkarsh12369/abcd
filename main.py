from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Creating a button instance
        button = Button(text='Click me!')
        return button
if __name__ == '__main__':
    MyApp().run()
