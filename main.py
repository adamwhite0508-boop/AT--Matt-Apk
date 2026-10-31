from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog

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
                icon: "cog-outline"
                on_release: root.manager.current = "settings"
        MDCard:
            size_hint_y: None
            height: "110dp"
            md_bg_color: 0.11,0.42,1,1
            radius: [22,22,22,22]
            padding: "15dp"
            on_release: root.manager.current = "crown"
            MDLabel:
                text: "🌍 AT WORLD MATTER\\nWASM + RAKSHAK + SECURE"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
        MDGridLayout:
            cols: 2
            spacing: "10dp"
            size_hint_y: None
            height: "160dp"
            MDCard:
                md_bg_color: 0.11,0.42,1,1
                radius: [18]
                padding: "12dp"
                on_release: root.manager.current = "brain"
                MDLabel:
                    text: "🧠 AT BRAIN\\nAI Hindi/Bhojpuri"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.48,0.38,1,1
                radius: [18]
                padding: "12dp"
                on_release: root.manager.current = "poster"
                MDLabel:
                    text: "🖼️ Photo Shayari\\nPoster Maker"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0,0.78,1,1
                radius: [18]
                padding: "12dp"
                on_release: root.manager.current = "online"
                MDLabel:
                    text: "💬 Online AT\\nGlobal Chat"
                    text_color: 1,1,1,1
        MDGridLayout:
            cols: 4
            spacing: "8dp"
            size_hint_y: None
            height: "140dp"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("📷 Camera")
                MDLabel:
                    text: "📷\\nCamera"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("🖼️ Gallery")
                MDLabel:
                    text: "🖼️\\nGallery"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: root.manager.current = "poster"
                MDLabel:
                    text: "🖌️\\nPoster"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("👤 Contacts")
                MDLabel:
                    text: "👤\\nContacts"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("📞 Calling AT...")
                MDLabel:
                    text: "📞\\nCall"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("🎙️ Voice Saved!")
                MDLabel:
                    text: "🎙️\\nVoice"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("💾 Download")
                MDLabel:
                    text: "💾\\nDownload"
                    halign: "center"
                    font_style: "Caption"
            MDCard:
                radius: [14]
                padding: "5dp"
                on_release: app.show_msg("🔗 Share AT WORLD MATTER")
                MDLabel:
                    text: "🔗\\nShare"
                    halign: "center"
                    font_style: "Caption"

<BrainScreen>:
    name: "brain"
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
                text: "🧠 AT BRAIN"
                bold: True
        ScrollView:
            MDBoxLayout:
                id: chat_box
                orientation: "vertical"
                adaptive_height: True
                spacing: "8dp"
                MDLabel:
                    text: "AT BRAIN: Bolo ka haal ba?"
                    adaptive_height: True
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
                on_release: app.show_msg("Poster Saved!")
        MDLabel:
            id: poster_preview
            text: "Poster Preview\\nAT WORLD MATTER"
            halign: "center"

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
        MDLabel:
            text: "Global Chat - AT WORLD MATTER\\nComing Soon"
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
        MDRaisedButton:
            text: "Toggle Dark Mode"
            on_release: app.toggle_dark()
        MDLabel:
            text: "🛡️ WASM + Rakshak ON\\nAT WORLD MATTER v2.0"
            halign: "center"

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
        MDLabel:
            text: "Secure + WASM + Rakshak ON\\nAT WORLD MATTER Protected"
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
        if self.dialog: self.dialog.dismiss()
        self.dialog = MDDialog(text=text, buttons=[])
        self.dialog.open()
    def send_msg(self):
        try:
            s = self.root.get_screen("brain")
            msg = s.ids.user_input.text.strip()
            if not msg: return
            from kivymd.uix.label import MDLabel
            s.ids.chat_box.add_widget(MDLabel(text=f"You: {msg}", adaptive_height=True))
            reply = "Haan Malik! Ka haal ba? Sab first class ba!" if "ka haal" in msg.lower() else f"{msg} - Done!"
            s.ids.chat_box.add_widget(MDLabel(text=f"AT BRAIN: {reply}", adaptive_height=True))
            s.ids.user_input.text = ""
        except Exception as e: print(e)
    def make_poster(self):
        try:
            s = self.root.get_screen("poster")
            txt = s.ids.shayari_text.text or "AT WORLD MATTER"
            s.ids.poster_preview.text = f"✨ Poster Ready ✨\\n{txt}\\nMade by AT WORLD MATTER"
        except: pass

AtWorldMatterApp().run()
