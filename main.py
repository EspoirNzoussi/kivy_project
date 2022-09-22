import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random



class Mygame(BoxLayout):
    def __init__(self):
        super(Mygame, self).__init__()
        self.valeur_random=random.randint(0, 5)
    def verification(self):
            if int(self.entrer_reponse.text)== self.valeur_random :
                self.mon_label.text= "Correct\n🏆🏆🏆🏆🏆🎉✨🎉✨😇😇"
                self.mon_label.color="#13FF20"
                self.valeur_random = random.randint(0, 5)
            elif int(self.entrer_reponse.text)> self.valeur_random :
                self.mon_label.text= "votre nombre est trop\ngrand 😥😥😥"
                self.mon_label.color="#FF231C"
            elif int(self.entrer_reponse.text)< self.valeur_random :
                self.mon_label.text= "votre nombre est trop\npetit😓😓😓"
                self.mon_label.color="#FC216C"

class EspoirApp(App):
    def build(self):
        return Mygame()

espoirApp=EspoirApp()
espoirApp.run()