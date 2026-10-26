from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ATMatt(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.add_widget(Label(text='AT - MATT AI', font_size='24sp', bold=True, size_hint_y=0.15))
        
        self.chat = Label(text='Namaste Sir! Mai AT Matt hu.\nApna sawal likhiye...', text_size=(None, None), halign='left', valign='top', size_hint_y=0.7)
        scroll = ScrollView()
        scroll.add_widget(self.chat)
        self.add_widget(scroll)
        
        self.input = TextInput(hint_text='Yaha likhiye...', size_hint_y=0.15, multiline=False)
        self.add_widget(self.input)
        
        btn = Button(text='BHEJO', size_hint_y=0.15, background_color=(0, 0.6, 0.8, 1))
        btn.bind(on_press=self.reply)
        self.add_widget(btn)

    def reply(self, instance):
        q = self.input.text
        if q.strip() == "":
            return
        self.chat.text += f"\n\nAap: {q}\nMatt: Ye sawal ka jawab mai jald dunga! (APK version)"
        self.input.text = ""

class ATMattApp(App):
    def build(self):
        return ATMatt()

ATMattApp().run()
