from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 500)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

# from kivy.animation import Animation
# from kivy.clock import Clock
# from kivy.config import Config
# from kivy.uix.image import Image
# from kivy.core import audio
# from kivy.core.audio import SoundLoader

# import socket
# sock = socket.socket()
# sock.bind(('', 9090))
# sock.listen(1)


# I set the color constants to then color the text on the buttons (this is optional)
red = (255 / 255, 67 / 255, 67 / 255)
green = (0 / 255, 158 / 255, 60 / 255)


class MainApp(App):
    def build(self):
        # here I add the main and second screens to the manager, this class does nothing else
        sm.add_widget(MainScreen())
        sm.add_widget(SecondScreen())
        return sm  # I return the manager to work with him later




class MainScreen(Screen):
    def __init__(self):
        super().__init__()

        self.name = 'Main'  # setting the screen name value for the screen manager
        # (it's more convenient to call by name rather than by class)

        main_layout = BoxLayout(orientation = 'vertical', spacing=10, padding = 25)
        main_layout.add_widget(Label(text="Bibliothek erstellen", font_size=40, height=50, size_hint = (1, .2)))
        # creating an empty layout that's not bound to the screen

        gl = GridLayout(cols=2, spacing=5, height=20, size_hint=(1, .2))
        # erste Gridlayout wird aus zwei spalten in 2te Zeile bl passen 30% gesamtlayout
        gl.add_widget(Label(text="Wort"))
        gl.add_widget(TextInput())
        gl.add_widget(Label(text="Bedeutung"))
        gl.add_widget(TextInput())

        gl2 = GridLayout(cols=1, rows=3, spacing=5, height=300, size_hint=(1, 0.6))
        # rest 50% uebernimmt Layout mit 3 Buttons Speichern, Prueffen und Abbrechen
        gl2.add_widget(Button(text="Speichern"))
        gl2.add_widget(Button(text="Prüfen", on_press=self.to_second_scrn))
        gl2.add_widget(Button(text="Abbrechen"))
        self.add_widget(main_layout)  # adding main_layout on screen
        main_layout.add_widget(gl)
        main_layout.add_widget(gl2)

        # Button
        """Go_Screen2 = Button(text='Go to Screen2',
                            size_hint=(.5, .5),
                            pos_hint={'center_x': .5, 'center_y': .5},
                            color=red)

        Go_Screen2.bind(on_press=self.to_second_scrn)  # setting up a button to perform an action when clicked

        main_layout.add_widget(Go_Screen2)  # adding button on layout"""

    def to_second_scrn(self, *args):
        self.manager.current = 'Second'  # selecting the screen by name (in this case by name "Second")
        return 0  # this line is optional


class SecondScreen(Screen):
    def __init__(self):
        super().__init__()
    # on this screen, I do everything the same as on the main screen to be able to switch back and forth
        self.name = 'Second'
        second_layout = BoxLayout(orientation='vertical', spacing=10, padding = 25)
        self.add_widget(second_layout)
        second_layout.add_widget(Label(text="Wörte lernen", padding=25, font_size=40, height=50, size_hint=(1, 0.15)))
        # um in eine Zeile verschiedene Anzahl von Spalten zu haben
        # nehme ich BoxLayout als Grundwerkstoff
        gl = GridLayout(cols=1, spacing=5, size_hint=(1, 0.05))
        gl.add_widget(TextInput())  # Feld fuer Antworteingabe

        gl2 = GridLayout(cols=1, spacing=5, size_hint=(1, 0.3))
        gl2.add_widget(Label(text="Was bedeutet?", font_size=20))  # Wird Woerte abgefragt
        gl2.add_widget(Label(text="Richtig", font_size=25))  # Richtig oder falsch nach Antwort
        gl2.add_widget(Label(text="Abgeschlossen!\n   Alles gelernt!", font_size=30))  # zeigt nach Abschluss

        gl3 = GridLayout(cols=1, spacing=5, size_hint=(1, 0.5))
        gl3.add_widget(Button(text="Prüfen"))
        gl3.add_widget(Button(text="Zur Worteingabe", on_press=self.to_main_scrn))
        gl3.add_widget(Button(text="Programm schliessen"))


        second_layout.add_widget(gl)
        second_layout.add_widget(gl2)
        second_layout.add_widget(gl3)


    def to_main_scrn(self, *args):  # together with the click of the button, it transmits info about itself.
        # In order not to pop up an error, I add *args to the function
        self.manager.current = 'Main'
        return 0


sm = ScreenManager()  # it's necessary to create a manager variable that will collect screens and manage them

if __name__ == '__main__':
    MainApp().run()