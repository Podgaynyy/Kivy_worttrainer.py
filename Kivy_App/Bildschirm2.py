from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 500)
 # размеры экрана надо прописывать до того,
# как импортируешь другие виджеты. Иначе ничего не изменится

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import *

class WortTrainer(App):
    def build2(self):  # erschaffe zweite Bildschirm, wo die Woerter geprueft werden
        bl = BoxLayout(orientation='vertical', spacing=10, padding = 25)
        bl.add_widget(Label(text="Wörte lernen", padding=25, font_size=40, height=50, size_hint=(1, 0.15)))
    # um in eine Zeile verschiedene Anzahl von Spalten zu haben
    # nehme ich BoxLayout als Grundwerkstoff
        gl = GridLayout(cols = 1, spacing = 5, size_hint=(1, 0.05))
        gl.add_widget(TextInput())  # Feld fuer Antworteingabe

        gl2 = GridLayout(cols=1, spacing=5, size_hint = (1, 0.3))
        gl2.add_widget(Label(text="Was bedeutet?", font_size=20))  # Wird Woerte abgefragt
        gl2.add_widget(Label(text="Richtig", font_size=25))  # Richtig oder falsch nach Antwort
        gl2.add_widget(Label(text="Abgeschlossen!\n   Alles gelernt!", font_size=30))  # zeigt nach Abschluss

        gl3 = GridLayout(cols=1, spacing=5, size_hint=(1, 0.5))
        gl3.add_widget(Button(text="Prüfen"))
        gl3.add_widget(Button(text="Zur Worteingabe"))
        gl3.add_widget(Button(text="Programm schliessen"))
        bl.add_widget(gl)
        bl.add_widget(gl2)
        bl.add_widget(gl3)
        return bl

if __name__ == "__main__":
    WortTrainer().run()