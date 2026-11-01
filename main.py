from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.clock import Clock

KV = '''
#:import FitImage kivymd.uix.fitimage.FitImage

MDNavigationLayout:
    ScreenManager:
        id: sm
        SplashScreen:
        MainScreen:

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y: None
                height: "190dp"
                orientation: "vertical"
                md_bg_color: 0.06,0.4,0.7,1
                padding: "16dp"
                spacing: "8dp"
                Image:
                    source: "icon.png"
                    size_hint: None, None
                    size: "72dp","72dp"
                    pos_hint: {"center_x": 0.5}
                MDLabel:
                    text: "AT World Matter"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    halign: "center"
                    font_style: "H6"
                    adaptive_height: True
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "AT BRAIN AI"
                        on_release: app.open_at_function("brain")
                        IconLeftWidget:
                            icon: "brain"
                    OneLineIconListItem:
                        text: "Photo Poster"
                        on_release: app.open_at_function("poster")
                        IconLeftWidget:
                            icon: "image"
                    OneLineIconListItem:
                        text: "AT CROWN Secure"
                        on_release: app.open_at_function("crown")
                        IconLeftWidget:
                            icon: "shield-check"

<SplashScreen>:
    name: "splash"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1
        FitImage:
            source: "login_banner.png"
            size_hint_y: 0.85
        MDBoxLayout:
            size_hint_y: 0.15
            padding: "16dp"
            MDRaisedButton:
                text: "Continue to AT World Matter"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                on_release: app.go_home()

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "AT World Matter"
            left_action_items: [["menu", lambda x: app.open_drawer()]]
            md_bg_color: 0.06,0.4,0.7,1
        MDLabel:
            text: "Welcome to AT World Matter - WASM + RAKSHAK"
            halign: "center"
'''

class SplashScreen(Screen): pass
class MainScreen(Screen): pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)
    
    def on_start(self):
        Clock.schedule_once(lambda x: self.go_home(), 0.5)

    def go_home(self):
        self.root.ids.sm.current = "main"

    def open_drawer(self):
        self.root.ids.nav_drawer.set_state("open")
    
    def open_at_function(self, name):
        self.root.ids.nav_drawer.set_state("close")
        print(f"Open {name}")

ATWorldMatterApp().run()
