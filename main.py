from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
import os

Window.softinput_mode = "below_target"

KV = '''
ScreenManager:
    HomeScreen:
    BrainScreen:
    PosterScreen:
    OnlineScreen:
    SettingsScreen:
    CrownScreen:

<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        spacing: "10dp"
        md_bg_color: app.theme_cls.bg_normal

        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "weather-night"
                on_release: app.toggle_dark()
            MDLabel:
                text: "AT WORLD MATTER"
                halign: "center"
                bold: True
            MDIconButton:
                icon: "bell-outline"
                on_release: app.show_msg("AT WORLD MATTER Notification")
            MDIconButton:
                icon: "cog-outline"
                on_release: root.manager.current = "settings"

        MDCard:
            size_hint_y: None
            height: "110dp"
            md_bg_color: 0.11,0.42,1,1
            radius: [22,22,22,22]
            padding: "15dp"
            on_release: root.manager.current = "crown"
            MDBoxLayout:
                orientation: "vertical"
                MDLabel:
                    text: "🌍 AT WORLD MATTER"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_style: "H6"
                    halign: "center"
                MDLabel:
                    text: "WASM + RAKSHAK + SECURE - AT CROWN Tap"
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    halign: "center"
                    font_style: "Caption"

        MDGridLayout:
            cols: 2
            spacing: "10dp"
            size_hint_y: None
            height: "160dp"
            MDCard:
                md_bg_color: 0.11,0.42,1,1
                radius: [18]
                on_release: root.manager.current = "brain"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    MDLabel:
                        text: "🧠 AT BRAIN"
                        bold: True
                        text_color: 1,1,1,1
                    MDLabel:
                        text: "AI Hindi/Bhojpuri"
                        font_style: "Caption"
                        text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.48,0.38,1,1
                radius: [18]
                on_release: root.manager.current = "poster"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    MDLabel:
                        text: "🖼️ Photo Shayari"
                        bold: True
                        text_color: 1,1,1,1
                    MDLabel:
                        text: "Poster Maker"
                        font_style: "Caption"
                        text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0,0.78,1,1
                radius: [18]
                on_release: root.manager.current = "online"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    MDLabel:
                        text: "💬 Online AT"
                        bold: True
                        text_color: 1,1,1,1
                    MDLabel:
                        text: "Global Chat"
                        font_style: "Caption"
                        text_color: 1,1,1,1

        MDGridLayout:
            cols: 4
            spacing: "8dp"
            size_hint_y: None
            height: "140dp"
            MDCard:
                radius: [14]
                on_release: app.open_camera()
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "camera"
                        halign: "center"
                    MDLabel:
                        text: "Camera"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.open_gallery()
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "image"
                        halign: "center"
                    MDLabel:
                        text: "Gallery"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: root.manager.current = "poster"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "draw"
                        halign: "center"
                    MDLabel:
                        text: "Poster"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.show_msg("Contacts - AT")
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "account"
                        halign: "center"
                    MDLabel:
                        text: "Contacts"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.show_msg("Calling AT WORLD MATTER...")
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "phone"
                        halign: "center"
                    MDLabel:
                        text: "Call"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.show_msg("🎙️ Voice Recording Saved!")
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "microphone"
                        halign: "center"
                    MDLabel:
                        text: "Voice"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.show_msg("💾 Poster Downloaded in Gallery!")
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "download"
                        halign: "center"
                    MDLabel:
                        text: "Download"
                        halign: "center"
                        font_style: "Caption"
            MDCard:
                radius: [14]
                on_release: app.show_msg("🔗 Share - AT WORLD MATTER")
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "5dp"
                    MDIcon:
                        icon: "share-variant"
                        halign: "center"
                    MDLabel:
                        text: "Share"
                        halign: "center"
                        font_style: "Caption"

<BrainScreen>:
    name: "brain"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        spacing: "10dp"
        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = "home"
            MDLabel:
                text: "🧠 AT BRAIN"
                bold: True
        ScrollView:
            id: chat_scroll
            MDBoxLayout:
                id: chat_box
                orientation: "vertical"
                adaptive_height: True
                spacing: "8dp"
                MDLabel:
                    text: "AT BRAIN: AT WORLD MATTER ready! Bolo ka haal ba?"
                    adaptive_height: True
                    padding: "10dp"
        MDBoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: "8dp"
            MDTextField:
                id: user_input
                hint_text: "Yaha likho..."
            MDRaisedButton:
                text: "Send"
                on_release: app.send_msg()

<PosterScreen>:
    name: "poster"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        spacing: "10dp"
        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = "home"
            MDLabel:
                text: "🖼️ Photo Shayari Poster"
                bold: True
        MDTextField:
            id: shayari_text
            hint_text: "Shayari likho..."
            size_hint_y: None
            height: "50dp"
        MDBoxLayout:
            size_hint_y: None
            height: "45dp"
            spacing: "10dp"
            MDRaisedButton:
                text: "✨ Banao"
                on_release: app.make_poster()
            MDRaisedButton:
                text: "💾 Download"
                md_bg_color: 0.06,0.54,0.37,1
                on_release: app.show_msg("Poster Saved!")
        MDLabel:
            id: poster_preview
            text: "Poster Preview Yaha Ayega\\n[Camera/Gallery se photo + Shayari]\\nAT WORLD MATTER"
            halign: "center"
            md_bg_color: 0.48,0.38,1,0.2
            radius: [14]

<OnlineScreen>:
    name: "online"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = "home"
            MDLabel:
                text: "💬 Online AT"
                bold: True
        MDCard:
            padding: "20dp"
            MDLabel:
                text: "Global Chat - AT WORLD MATTER\\nSabhi AT Members yaha chat kar sakte hai\\nComing Soon - Full Chat Feature"
                halign: "center"

<SettingsScreen>:
    name: "settings"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = "home"
            MDLabel:
                text: "⚙️ Settings"
                bold: True
        MDCard:
            padding: "15dp"
            orientation: "vertical"
            MDLabel:
                text: "🌙 Dark Mode: ON/OFF Button se badlo"
            MDRaisedButton:
                text: "Toggle Dark Mode"
                on_release: app.toggle_dark()
            MDLabel:
                text: "\\n🛡️ WASM + Rakshak ON\\nAT WORLD MATTER v2.0 - Final"
                adaptive_height: True

<CrownScreen>:
    name: "crown"
    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        MDBoxLayout:
            size_hint_y: None
            height: "40dp"
            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = "home"
            MDLabel:
                text: "🛡️ AT CROWN"
                bold: True
        MDCard:
            padding: "20dp"
            MDLabel:
                text: "Secure + WASM + Rakshak ON\\nAT WORLD MATTER Protected\\nAT CROWN - Tap to Secure Your World"
                halign: "center"
'''

class HomeScreen(Screen): pass
class BrainScreen(Screen): pass
class PosterScreen(Screen): pass
class OnlineScreen(Screen): pass
class SettingsScreen(Screen): pass
class CrownScreen(Screen): pass

class AtWorldMatterApp(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def toggle_dark(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    def show_msg(self, text):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(text=text, buttons=[])
        self.dialog.open()

    def send_msg(self):
        try:
            screen = self.root.get_screen("brain")
            inp = screen.ids.user_input
            chat = screen.ids.chat_box
            msg = inp.text.strip()
            if not msg: return
            from kivymd.uix.label import MDLabel
            from kivy.metrics import dp
            chat.add_widget(MDLabel(text=f"You: {msg}", adaptive_height=True, padding=[10,10]))
            reply = f"{msg} - Done!"
            low = msg.lower()
            if "ka haal" in low: reply = "Haan Malik! Ka haal ba? Sab first class ba!"
            elif "kaise" in low: reply = "Ekdam mast! AT WORLD MATTER ready ba!"
            chat.add_widget(MDLabel(text=f"AT BRAIN: {reply}", adaptive_height=True, padding=[10,10], theme_text_color="Custom", text_color=(0.11,0.42,1,1)))
