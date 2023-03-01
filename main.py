import kivy 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import textInput
from kivy.uix.boxlayout import BoxLayoutfrom kivy,import App

class Appcoverso(App):
    def build(self):
        self.bl = BoxLauyout (orientacion='horizontal')
        self.lbltitulo =Label()
        self.lbltitulo.text = "conversor de dolares a pesos"
        self.ti = textInput 
        self.ti.text = "ingrese el valor a convertir"
        self.btn1 = Button()
        self.btn1.text = "presioname"
        self.btn1.font_size = 18
        self.lblfinal = Label()
        self.bl.add_widget(self.lbltitulo)
        self.bl.add_wigdet-_(self.ti)
        self.bl.add_wigdet-(self.btn1)
        self.bl.add-wigdet(self.lblfinal)
        return self.bl
if __name__ =="__main__" :
    appConversor().run()
    


