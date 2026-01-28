from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# شاشة قفل الخزنة
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        layout.add_widget(Label(text="🔒 Gaming Vault", font_size=30))
        
        self.password = TextInput(multiline=False, password=True, hint_text="كلمة المرور")
        layout.add_widget(self.password)
        
        btn = Button(text="فتح الخزنة", background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.check_password)
        layout.add_widget(btn)
        
        self.add_widget(layout)

    def check_password(self, instance):
        if self.password.text == "1234":
            self.manager.current = 'hub'

# شاشة مكتبة الألعاب
class HubScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="🎮 مكتبة ألعابي", font_size=30))
        layout.add_widget(Button(text="لعبة 1 (قريباً)"))
        layout.add_widget(Button(text="لعبة 2 (قريباً)"))
        self.add_widget(layout)

class GamingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HubScreen(name='hub'))
        return sm

if __name__ == '__main__':
    GamingApp().run()