#-----------------------------------------
#   Importações
#-----------------------------------------
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock # cria delay
from kivy.core.window import Window # janela do app
from kivy.utils import get_color_from_hex #cores hexa
from kivy.core.text import LabelBase # fonte para textos
from kivy.lang import Builder # importa telas do arquivo .kv
 
 
#-----------------------------------------
#   Configurações do Aplicativo
#-----------------------------------------
 
# Carrega o arquivo KV
Builder.load_file('telas.kv')
 
# Definir o tamanho da tela
Window.size = (338, 600)
 
# importando a nova fonte
LabelBase.register(name='MinhaFonte', fn_regular='Raleway-Light.ttf')
 
#-----------------------------------------
#   Telas da aplicação
#-----------------------------------------
 
# Tela SplashScreen
class SplashScreen(Screen):
    def on_enter(self):
        # Agendar a navegação para a tela de login após 3 segundos
        Clock.schedule_once(self.go_to_login, 10)
 
    def go_to_login(self, dt):
        # Transição para a tela de login
        self.manager.current = 'login'
 
 
# Tela de Login
class LoginScreen(Screen):
    pass

class AcessoScreen(Screen):
    pass
 
#-----------------------------------------
#   Classe principal
#-----------------------------------------
class Testes(App):
    def build(self):
       
        # cor de fundo da janela
        Window.clearcolor = get_color_from_hex('#ffffff')
       
        # Criação do ScreenManager
        sm = ScreenManager()
 
        # Adiciona as telas ao ScreenManager
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(AcessoScreen(name='acessar'))
        sm.add_widget(LoginScreen(name='login'))
 
        return sm
 
 
if __name__ == '__main__':
    Testes().run()