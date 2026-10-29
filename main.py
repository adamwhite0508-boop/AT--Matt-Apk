from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
Window.softinput_mode = "below_target"

KV = '''
<SplashScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        Widget:
        MDLabel:
            text: "AT WORLD"
            halign: "center"
            font_style: "H4"
            bold: True
        MDLabel:
            text: "AT World Matter"
            halign: "center"
        Widget:
        MDLabel:
            text: "Loading..."
            halign: "center"
            theme_text_color: "Hint"
        Widget:

<MainScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 0.02, 0.45, 0.80, 1
            padding: "10dp"
            MDLabel:
                text: "AT World Matter"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                bold: True
            MDIconButton:
                icon: "dots-vertical"
                theme_text_color: "Custom"
                text_color: 1,1,1,1

        ScrollView:
            MDList:
                TwoLineAvatarIconListItem:
                    text: "Anuj Tripathi"
                    secondary_text: "Sir AT World Ready Hai!"
                    on_release: app.show_chat("Anuj Tripathi")
                    IconLeftWidget:
                        icon: "account-circle"
                TwoLineAvatarIconListItem:
                    text: "AT Group"
                    secondary_text: "Welcome to AT World"
                    on_release: app.show_chat("AT Group")
                    IconLeftWidget:
                        icon: "account-group"
                TwoLineAvatarIconListItem:
                    text: "AT Support"
                    secondary_text: "How can I help you?"
                    on_release: app.show_chat("AT Support")
                    IconLeftWidget:
                        icon: "headset"

        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 0.95,0.95,0.95,1
            MDIconButton:
                icon: "message-text"
            Widget:
            MDIconButton:
                icon: "phone"
            Widget:
            MDIconButton:
                icon: "account-group"
'''

class SplashScreen(MDScreen): pass
class MainScreen(MDScreen): pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

    def on_start(self):
        Clock.schedule_once(self.go_main, 2)

    def go_main(self, *args):
        self.root.current = 'main'

    def show_chat(self, name):
        print(f"Open chat: {name}")

ATWorldMatterApp().run()
