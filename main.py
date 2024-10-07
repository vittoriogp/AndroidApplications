# Kivy app
from kivy.app import App
# Kivy Layout
from kivy.uix.floatlayout import FloatLayout
# Widgets
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class Interface(FloatLayout): 
    
    
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)

        # Creazione di un widget button
        self.button = Button(
            # Testo del button (formato Markup)
            markup = True, 
            text = "[color=#FFBF00][b]Hello[/b][/color] [i]World[/i] Button", 
            # Colore del testo
            color = (0.5, 0.5, 0.5), # Formato RGB
            # Background colorato 
            background_color = (0.5, 0.5, 1, 1), # Formato RGBA
            background_normal = '', # Eliminazione del background color standard 

            # Immagine come background
            # background_normal = '../Immagini/Bocconi.png' # Immagine mostrata quando il button non è premuto
            # background_down = '../Immagini/Bocconi.png' # Immagine mostrata quando il button è premuto

            # Disabilitazione del pulsante
            # disabled: True
            # background_disabled_normal = "../Immagini/Bocconi.png" # Background quando il pulsante è disabilitato e non premuto
            # background_disabled_down = "../Immagini/Bocconi.png" # Background quando il pulsante è disabilitato e premuto

            # Dimensione del font
            font_size = '32sp',
            # Dimensioni del pulsante
            size_hint = (0.5, 0.2), 
            # Posizione del pulsante
            pos_hint = {"center_x": 0.5, "top": 0.2},
        )
        self.button.bind(
            # Evento e callback function quando si preme il pulsante
            on_press = self.callback_button_onPress, 
            # Evento e callback function quando si rilascia il pulsante
            on_release = self.callback_button_onRelease, 
        )
        self.add_widget(self.button)

        # Creazione di un widget label
        self.label = Label(
            # Testo (formato markuup)
            markup = True,
            text = "[color=#FFBF00][b]Hello[/b][/color] [i]World[/i]", 
            # Colore del font
            color = (0.5, 0.5, 0.5), 
            # Dimensione del font
            font_size = '32sp',
            # Dimensioni del font
            size_hint = (0.5, 0.4), 
            # Posizione del label
            pos_hint = {"center_x": 0.5, "top": 0.6},
        )
        self.add_widget(self.label)

        # Creazione di un widget text input
        self.textinput = TextInput(
            # Dimensioni del text input
            size_hint = (0.5, 0.4), 
            # Posizione del text input
            pos_hint = {"center_x": 0.5, "top": 1},
            # Multilinea 
            multiline = False, 
        )
        self.textinput.bind(
            on_text_validate = self.callback_button_onRelease
        )
        self.add_widget(self.textinput)

    
    def callback_button_onPress(self, obj): 
        print("button premuto")
    def callback_button_onRelease(self, obj): 
        testo_utente = self.textinput.text
        self.label.text = testo_utente
        print(testo_utente)

class Applicazione(App): 
    def build(self): 
        return Interface()

Applicazione().run()

