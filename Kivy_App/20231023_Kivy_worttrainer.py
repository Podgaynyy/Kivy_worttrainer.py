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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout


class MainApp(App):
    def build(self):
        # here I add the main and second screens to the manager, this class does nothing else
        sm.add_widget(WortTrainer1stScreen())
        sm.add_widget(SecondScreen())
        return sm  # I return the manager to work with him later


class WortTrainer1stScreen(App):
    def __init__(self):
        super().__init__()

        self.name = 'Main'

    """def abschliessen():
        schluss()
        fenster.destroy()"""

    """def schluss():
    datei = open('woerterbuch.txt', 'w')
    datei.close()"""

    """def erschaffeWoerterbuch():
    # Aufbau eines fremdsprache-deutschen Wörterbuchs
        datei = open('woerterbuch.txt', 'a')
        if wort_eintrag.get() == '':
            datei.close()
        elif wort_eintrag.get() == ' ':
            datei.close()
        else:
            datei.write(wort_eintrag.get() + " " + bedeutung_eintrag.get() + "\n")
            wort_eintrag.delete(0, END)
            bedeutung_eintrag.delete(0, END)"""


    """def getListe():
        global liste
        datei = open('woerterbuch.txt', 'r', encoding='utf-8')
        wortschatz = datei.readlines()
        datei.close()
        for zeile in wortschatz:
            if zeile == '\n' or zeile == ' \n':
                pass
            else:
                vokabel = zeile.split()
                liste.append(vokabel)"""

    """def start():
    getListe()
    listeChoice()
    print(liste)"""


    """def listeChoice():
    global checkElement
    if len(liste) != 0:
        checkElement = random.choice(liste)
        label_wort_abfrage.config(text="Was bedeutet: " + checkElement[0])
    else:
        label_finisch = Label(recht, text="Abgeschlossen! \n Alles gelernt", fg="black",
                              font=("Tiwg Typist", 12), bg="#A9A9A9", height=2, width=30).grid(row=5, pady=5)"""

    """def pruefung():
    global liste
    if label_wort_bedeutung.get() == checkElement[1]:
        label_richtig = Label(recht, text="Richtig!", fg="black",
                                font=("Tiwg Typist", 12), bg = "#A9A9A9", height=2, width=30).grid(row=5, pady=5)
        label_wort_bedeutung.delete(0, END)
        liste.remove(checkElement)
        listeChoice()
    else:
        label_falsch = Label(recht, text="leider falsch!", fg="black",
                                 font=("Tiwg Typist", 12), bg="#A9A9A9", height=2, width=30).grid(row=5, pady=5)
        label_wort_bedeutung.delete(0, END)
        listeChoice()"""

    """#******** Linke Block ********
    #Erstellen Uebertitel fuer Dicteintrag
    label_eintrag = Label(link, text="Hier erstellen Sie Ihre Zettelbibliotek \n"
                "zum Lernen neuer Sprache:", fg="black", font=("KacstArt", 12), bg = "#FFFFFF", height=3, width=30)
    #man gibt zuerst fremdspache Wort
    wort_eintrag = Entry(link, fg="black", font=("KacstArt", 12), bg = "#FFFFFF", width=17)
    #man gibt zuerst fremdspache, dann bedeutung auf Deutsch
    bedeutung_eintrag = Entry(link, fg="black", font=("KacstArt", 12), bg = "#FFFFFF", width=17)
    #wird gewaechselt, wenn Wort eingetragen wurde
    label_links_worteintrag = Label(link, text="Wort eingeben", fg="black", font=("Tiwg Typist", 10), bg = "#D3D3D3",
                                height=1, width=10)
    label_links_bedeutungeintrag = Label(link, text="Bedeutung eingeben", fg="black", font=("Tiwg Typist", 10),
                                     bg = "#D3D3D3", height=1, width=17)
    #wird in pfad gespeichert
    button_speichern = Button(link, text="Speichern", fg="black", font=("Arial", 12), bg = "#808080",
                                height=3, width=10, command=erschaffeWoerterbuch)
    #macht Übungsfunktion aktiv
    button_zur_pruefung = Button(link, text="Zur Übung", fg="black", font=("Arial", 12), bg = "#00FF00", command=start,
                                height=3, width=10)

    #******* Rechte Block*******
    # Erstellen Uebertitel fuer Lernmodus
    label_abfrage = Label(recht, text="Hier lernen Sie die eingetragene Wörter",
                      fg="black", font=("KacstArt", 12), bg="#FFFFFF", height=3)
    label_wort_bedeutung = Entry(recht, fg="black", font=("KacstArt", 12), bg = "#FFFFFF", width=30)
    label_wort_abfrage = Label(recht, text="Was bedeutet: _________ ?", fg="black", font=("Tiwg Typist", 12), bg = "#A9A9A9",
                                height=1, width=30)
    button_pruefen = Button(recht, text="prüfen", fg="black", font=("Arial", 12), bg = "#808080", command=pruefung,
                                height=3, width=10)
    button_exit = Button(recht, text="Schliessen", fg="black", font=("Arial", 12), bg = "#B22222", command=abschliessen,
                                height=3, width=10)

    #******* Auspacken linkes Frame *******
    link.place(relx=0, rely=0, relheight=1, relwidth=0.5, )
    label_eintrag.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    wort_eintrag.grid(row=1, column=1, padx=10, pady=1)
    label_links_worteintrag.grid(row=1, column=0, padx=2, pady=2)
    bedeutung_eintrag.grid(row=2, column=1, padx=10, pady=1)
    label_links_bedeutungeintrag.grid(row=2, column=0, padx=2, pady=2)
    button_speichern.grid(row=3, columnspan=2, pady=3)
    button_zur_pruefung.grid(row=4, columnspan=2, pady=3)

    #******* Auspacken rechtes Frame *******
    recht.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
    label_abfrage.grid(row=0, padx=10, pady=10)
    label_wort_bedeutung.grid(row=1, padx=10, pady=1)
    label_wort_abfrage.grid(row=2, padx=10, pady=0)
    button_pruefen.grid(row=3, pady=3)
    button_exit.grid(row=4, pady=3)

    button_zur_pruefung.bind("<Enter>")
    button_zur_pruefung.bind("<Leave>")
    """



    def build(self):
        bl = BoxLayout(orientation = 'vertical', spacing=10, padding = 25)
        #um in eine Zeile verschiedene Anzahl von Spalten zu haben
        #nehme ich BoxLayout als Grundwerkstoff
        bl.add_widget(Label(text="Bibliothek erstellen", font_size=40, height=50, size_hint = (1, .2)))
        # erste Zeile bekommt 20% von BoxLayout
        gl = GridLayout(cols = 2, spacing = 5, height = 20, size_hint = (1, .2))
        #erste Gridlayout wird aus zwei spalten in 2te Zeile bl passen 30% gesamtlayout
        gl.add_widget(Label(text = "Wort"))
        gl.add_widget(TextInput())
        gl.add_widget(Label(text="Bedeutung"))
        gl.add_widget(TextInput())

        gl2 = GridLayout(cols = 1, rows = 3, spacing = 5, height = 300, size_hint = (1, 0.6))
        #rest 50% uebernimmt Layout mit 3 Buttons Speichern, Prueffen und Abbrechen
        gl2.add_widget(Button(text = "Speichern"))
        gl2.add_widget(Button(text="Prüfen", on_press = self.build2))
        gl2.add_widget(Button(text="Abbrechen"))
        bl.add_widget(gl) #In erste Zeile bl wird gl zugegeben. Ohne diese Kommande funktioniert es leider nicht
        bl.add_widget(gl2)
        return bl


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





"""gl.add_widget(Button(text = "Speichern",
                      background_color = [.29, .29, .30, 1],
                      background_normal = ''))
        bl.add_widget(Button(text="Zur Pruefung",
                             on_press=self.start,
                             background_color=[.29, .29, .30, 1],
                             background_normal='', cols = 2, rows = 3))
    def start(self, instance):
        instance.text = "Viel Erfolg!"
        instance.background_color= [.58, .78, .67, 1]"""

sm = ScreenManager()

if __name__ == '__main__':
    MainApp().run()