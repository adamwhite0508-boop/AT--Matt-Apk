from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import os

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
            spacing: "8dp"

            MDBoxLayout:
                size_hint_y: None
                height: "200dp"
                orientation: "vertical"
                md_bg_color: 0.06, 0.4, 0.7, 1
                padding: "16dp"
                spacing: "12dp"

                Image:
                    source: "icon.png"
                    size_hint: None, None
                    size: "80dp", "80dp"
                    pos_hint: {"center_x": 0.5}
                
                MDLabel:
                    text: "AT World Matter"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    halign: "center"
                    font_style: "H6"
                    adaptive_height: True

                MDLabel:
                    text: "WASM + RAKSHAK"
                    theme_text_color: "Custom"
                    text_color: 0.9,0.9,0.9,1
                    halign: "center"
                    font_style: "Caption"
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
                            icon: "image-outline"

                    OneLineIconListItem:
                        text: "AT CROWN Secure"
                        on_release: app.open_at_function("crown")
                        IconLeftWidget:
                            icon: "shield-check-outline"
                    
                    MDSeparator:

                    OneLineIconListItem:
                        text: "About Us"
                        on_release: app.open_at_function("about")
                        IconLeftWidget:
                            icon: "information-outline"

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
            padding: "24dp"
            md_bg_color: 1,1,1,1
            
            MDRaisedButton:
                text: "Continue to AT World Matter"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                size_hint_x: 0.9
                md_bg_color: 0.06, 0.4, 0.7, 1
                on_release: app.go_home()

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "AT World Matter"
            left_action_items: [["menu", lambda x: app.open_drawer()]]
            right_action_items: [["dots-vertical"]]
            md_bg_color: 0.06, 0.4, 0.7, 1

        MDBoxLayout:
            orientation: "vertical"
            padding: "24dp"
            spacing: "16dp"
            
            MDIcon:
                icon: "check-decagram"
                halign: "center"
                font_size: "80sp"
                theme_text_color: "Custom"
                text_color: 0.06, 0.4, 0.7, 1
                size_hint_y: None
                height: "100dp"

            MDLabel:
                text: "Welcome to AT World Matter"
                halign: "center"
                font_style: "H5"
                bold: True
                adaptive_height: True

            MDLabel:
                text: "WASM + RAKSHAK Platform Ready!\\nAapka APK ab single arch (arm64-v8a) pe ban raha hai!"
                halign: "center"
                theme_text_color: "Secondary"
                adaptive_height: True
'''

class SplashScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        # Agar image nahi hai to blank na ho
        if not os.path.exists("icon.png"):
            print("Warning: icon.png not found!")
        if not os.path.exists("login_banner.png"):
            print("Warning: login_banner.png not found!")
        return Builder.load_string(KV)

    def go_home(self):
        self.root.ids.sm.current = "main"
        self.root.ids.nav_drawer.set_state("close")

    def open_drawer(self):
        self.root.ids.nav_drawer.set_state("open")

    def open_at_function(self, name):
        print(f"Opening: {name}")
        self.root.ids.nav_drawer.set_state("close")
        if name == "brain":
            self.root.ids.sm.current = "main"
        elif name == "poster":
            self.root.ids.sm.current = "main"
        elif name == "crown":
            self.root.ids.sm.current = "main"
        elif name == "about":
            self.root.ids.sm.current = "main"

if __name__ == "__main__":
    ATWorldMatterApp().run()
