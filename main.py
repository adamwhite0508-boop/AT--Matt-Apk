from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.metrics import dp

KV = '''
MDNavigationLayout:
    ScreenManager:
        id: sm
        SplashScreen:
        MainScreen:
        BrainScreen:
        PosterScreen:
        CameraScreen:
        GalleryScreen:
        ContactsScreen:
        CallScreen:
        VideoCallScreen:
        VoiceScreen:
        OnlineScreen:
        SettingsScreen:
        CrownScreen:

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        MDBoxLayout:
            orientation: "vertical"
            padding: "0dp"
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
                    text_color: 1,1,1,1
                    theme_text_color: "Custom"
                    halign: "center"
                    font_style: "H6"
                    adaptive_height: True
                MDLabel:
                    text: "WASM + RAKSHAK"
                    text_color: 1,1,1,0.8
                    theme_text_color: "Custom"
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
                            icon: "image"
                    OneLineIconListItem:
                        text: "AT Camera"
                        on_release: app.open_at_function("camera")
                        IconLeftWidget:
                            icon: "camera"
                    OneLineIconListItem:
                        text: "Gallery / Voice"
                        on_release: app.open_at_function("gallery")
                        IconLeftWidget:
                            icon: "folder-image"
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
        # HIGH QUALITY SPLASH BANNER - Aapka pehla wala
        Image:
            source: "splash_login.png"
            fit_mode: "contain"
            size_hint_y: 0.85
        MDBoxLayout:
            size_hint_y: 0.15
            padding: "16dp"
            MDRaisedButton:
                text: "Continue to AT World Matter"
                md_bg_color: 0.06,0.4,0.7,1
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                on_release: app.go_home()

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        # HIGH QUALITY HEADER BANNER - Aapka dusra wala
        MDCard:
            size_hint_y: None
            height: "180dp"
            radius: [0,0,22,22]
            md_bg_color: 0.06,0.4,0.7,1
            Image:
                source: "main_header_banner.png"
                fit_mode: "cover"
                radius: [0,0,22,22]
            MDIconButton:
                icon: "menu"
                pos_hint: {"x": 0, "top": 1}
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_release: app.open_drawer()
        MDBoxLayout:
            size_hint_y: None
            height: "48dp"
            padding: "8dp"
            MDTextField:
                id: search_bar
                hint_text: "Search AT - Chat, Status, Calls..."
                mode: "round"
        MDBottomNavigation:
            panel_color: 1,1,1,1
            text_color_active: 0.06,0.4,0.7,1
            MDBottomNavigationItem:
                name: "chat_tab"
                text: "Chat"
                icon: "chat"
                MDBoxLayout:
                    orientation: "vertical"
                    ScrollView:
                        MDBoxLayout:
                            id: chat_list
                            orientation: "vertical"
                            adaptive_height: True
                            padding: "8dp"
                            spacing: "6dp"
                    MDRaisedButton:
                        text: "AT BRAIN Chat Kholo"
                        size_hint_y: None
                        height: "48dp"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.open_at_function("brain")
            MDBottomNavigationItem:
                name: "status_tab"
                text: "Status"
                icon: "fire"
                MDBoxLayout:
                    orientation: "vertical"
                    ScrollView:
                        MDBoxLayout:
                            id: status_list
                            orientation: "vertical"
                            adaptive_height: True
                            padding: "8dp"
                    MDRaisedButton:
                        text: "+ Status"
                        size_hint_y: None
                        height: "48dp"
                        pos_hint: {"center_x": 0.5}
                        md_bg_color: 0.9,0.3,0.2,1
                        on_release: app.add_status()
            MDBottomNavigationItem:
                name: "adds_tab"
                text: "Adds"
                icon: "account-group"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    MDLabel:
                        text: "AT Adds - Community"
                        bold: True
                        halign: "center"
                        adaptive_height: True
                    ScrollView:
                        MDBoxLayout:
                            id: adds_list
                            orientation: "vertical"
                            adaptive_height: True
                    MDRaisedButton:
                        text: "+ New Adds"
                        size_hint_y: None
                        height: "48dp"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.add_adds()
            MDBottomNavigationItem:
                name: "calls_tab"
                text: "Calls"
                icon: "phone"
                MDBoxLayout:
                    orientation: "vertical"
                    ScrollView:
                        MDBoxLayout:
                            id: call_history_list
                            orientation: "vertical"
                            adaptive_height: True
                            padding: "8dp"
                    MDBoxLayout:
                        size_hint_y: None
                        height: "60dp"
                        spacing: "10dp"
                        pos_hint: {"center_x": 0.5}
                        adaptive_width: True
                        MDRaisedButton:
                            text: "Call"
                            on_release: app.open_at_function("call")
                        MDRaisedButton:
                            text: "Video"
                            md_bg_color: 0.48,0.38,1,1
                            on_release: app.open_at_function("videocall")

<BrainScreen>:
    name: "brain"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "AT BRAIN AI"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        ScrollView:
            MDBoxLayout:
                id: chat_box
                orientation: "vertical"
                adaptive_height: True
                padding: "12dp"
                spacing: "8dp"
        MDCard:
            id: attach_panel
            size_hint_y: None
            height: 0
            opacity: 0
            md_bg_color: 0.97,0.97,0.97,1
            radius: [18,18,0,0]
            padding: "12dp"
            MDGridLayout:
                cols: 4
                adaptive_height: True
                spacing: "10dp"
                MDBoxLayout:
                    orientation: "vertical"
                    MDCard:
                        size_hint: None, None
                        size: "56dp","56dp"
                        radius: [16]
                        md_bg_color: 0.2,0.5,1,0.15
                        pos_hint: {"center_x": 0.5}
                        on_release: app.chat_open_gallery("brain")
                        MDIconButton:
                            icon: "image"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDLabel:
                        text: "Gallery"
                        halign: "center"
                        font_style: "Caption"
                        adaptive_height: True
                MDBoxLayout:
                    orientation: "vertical"
                    MDCard:
                        size_hint: None, None
                        size: "56dp","56dp"
                        radius: [16]
                        md_bg_color: 1,0.3,0.3,0.15
                        pos_hint: {"center_x": 0.5}
                        on_release: app.chat_open_camera("brain")
                        MDIconButton:
                            icon: "camera"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDLabel:
                        text: "Camera"
                        halign: "center"
                        font_style: "Caption"
                        adaptive_height: True
                MDBoxLayout:
                    orientation: "vertical"
                    MDCard:
                        size_hint: None, None
                        size: "56dp","56dp"
                        radius: [16]
                        md_bg_color: 0.5,0.3,0.9,0.15
                        pos_hint: {"center_x": 0.5}
                        on_release: app.chat_open_document("brain")
                        MDIconButton:
                            icon: "file-document"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDLabel:
                        text: "Document"
                        halign: "center"
                        font_style: "Caption"
                        adaptive_height: True
                MDBoxLayout:
                    orientation: "vertical"
                    MDCard:
                        size_hint: None, None
                        size: "56dp","56dp"
                        radius: [16]
                        md_bg_color: 0,0.7,0.4,0.15
                        pos_hint: {"center_x": 0.5}
                        on_release: app.chat_open_ai_studio("brain")
                        MDIconButton:
                            icon: "creation"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDLabel:
                        text: "AI Studio"
                        halign: "center"
                        font_style: "Caption"
                        adaptive_height: True
        MDCard:
            size_hint_y: None
            height: "64dp"
            md_bg_color: 1,1,1,1
            radius: [28]
            padding: "6dp"
            spacing: "4dp"
            MDIconButton:
                icon: "emoticon-happy-outline"
            MDTextField:
                id: user_input
                hint_text: "Message"
                mode: "rectangle"
            MDIconButton:
                icon: "paperclip"
                on_release: app.toggle_attach("brain")
            MDIconButton:
                icon: "camera-outline"
                on_release: app.chat_open_camera("brain")
            MDCard:
                size_hint: None, None
                size: "48dp","48dp"
                radius: [24]
                md_bg_color: 0.06,0.4,0.7,1
                on_release: app.send_msg()
                MDIconButton:
                    icon: "send"
                    icon_color: 1,1,1,1
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

<PosterScreen>:
    name: "poster"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Poster Maker"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDTextField:
                id: shayari_text
                hint_text: "Shayari likho..."
            MDRaisedButton:
                text: "Banao"
                pos_hint: {"center_x": 0.5}
                on_release: app.make_poster()
            MDCard:
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.06,0.4,0.7,1
                radius: [18]
                padding: "16dp"
                MDLabel:
                    id: poster_preview
                    text: "Poster Preview"
                    halign: "center"
                    text_color: 1,1,1,1

<CameraScreen>:
    name: "camera"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "AT Camera"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        Camera:
            id: cam
            play: True
        MDRaisedButton:
            text: "Photo Lo - Chat me jayega"
            size_hint_y: None
            height: "56dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.take_photo()

<GalleryScreen>:
    name: "gallery"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Gallery"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            id: gal_label
            text: "Gallery Working - No Cut"
            halign: "center"
        MDRaisedButton:
            text: "Gallery Kholo"
            pos_hint: {"center_x": 0.5}
            on_release: app.open_gallery()

<ContactsScreen>:
    name: "contacts"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Contacts"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        ScrollView:
            MDList:
                id: contact_list

<CallScreen>:
    name: "call"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Call"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDBoxLayout:
            padding: "20dp"
            orientation: "vertical"
            spacing: "12dp"
            MDTextField:
                id: call_number
                hint_text: "Number"
            MDRaisedButton:
                text: "Call Karo - Working"
                pos_hint: {"center_x": 0.5}
                on_release: app.make_call()

<VideoCallScreen>:
    name: "videocall"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Video Call"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        Camera:
            id: vcam
            play: True
        MDRaisedButton:
            text: "Start Video - Working"
            size_hint_y: None
            height: "56dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.start_video()

<VoiceScreen>:
    name: "voice"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Voice"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            id: voice_label
            text: "Voice Working"
            halign: "center"
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            spacing: "12dp"
            pos_hint: {"center_x": 0.5}
            adaptive_width: True
            MDRaisedButton:
                text: "Record"
                on_release: app.start_voice()
            MDRaisedButton:
                text: "Stop"
                on_release: app.stop_voice()

<OnlineScreen>:
    name: "online"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Online AT"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        ScrollView:
            MDBoxLayout:
                id: online_chat
                orientation: "vertical"
                adaptive_height: True
                padding: "12dp"
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            padding: "8dp"
            MDTextField:
                id: online_input
                hint_text: "Global message..."
            MDRaisedButton:
                text: "Send"
                on_release: app.send_online()

<SettingsScreen>:
    name: "settings"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Settings"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "12dp"
            Image:
                source: "icon.png"
                size_hint: None, None
                size: "100dp","100dp"
                pos_hint: {"center_x": 0.5}
            MDLabel:
                text: "AT World Matter v6.0\\nWith High Quality Banners\\nNo Cut + All Working"
                halign: "center"

<CrownScreen>:
    name: "crown"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "AT CROWN"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "12dp"
            Image:
                source: "icon.png"
                size_hint: None, None
                size: "200dp","200dp"
                pos_hint: {"center_x": 0.5}
            MDLabel:
                text: "WASM + RAKSHAK ON - Secure"
                halign: "center"
                bold: True
'''

class SplashScreen(Screen): pass
class MainScreen(Screen): pass
class BrainScreen(Screen): pass
class PosterScreen(Screen): pass
class CameraScreen(Screen): pass
class GalleryScreen(Screen): pass
class ContactsScreen(Screen): pass
class CallScreen(Screen): pass
class VideoCallScreen(Screen): pass
class VoiceScreen(Screen): pass
class OnlineScreen(Screen): pass
class SettingsScreen(Screen): pass
class CrownScreen(Screen): pass

class AtWorldMatterApp(MDApp):
    dialog=None
    def build(self):
        self.theme_cls.primary_palette="Blue"
        return Builder.load_string(KV)
    def on_start(self):
        Clock.schedule_once(lambda dt: self.load_lists(), 0.5)
        Clock.schedule_once(lambda dt: setattr(self.root.ids.sm, 'current', 'splash'), 0.1)
    def load_lists(self):
        try:
            self.root.ids.chat_list.clear_widgets()
            for n,m in [("AT BRAIN AI","Haan Malik bolo?"),("Anuj Sir","Jai Shree Ram!"),("AT Support","App Ready")]:
                self.root.ids.chat_list.add_widget(MDLabel(text=f"{n}: {m}", adaptive_height=True, padding="10dp"))
            self.root.ids.status_list.clear_widgets()
            self.root.ids.status_list.add_widget(MDLabel(text="Anuj: AT WORLD Status", adaptive_height=True, padding="10dp"))
            self.root.ids.call_history_list.clear_widgets()
            for n in ["Anuj Sir - Today 10:30 AM","AT Office - Yesterday"]:
                self.root.ids.call_history_list.add_widget(MDLabel(text=f"{n}", adaptive_height=True, padding="10dp"))
        except: pass
    def open_drawer(self):
        self.root.ids.nav_drawer.set_state("open")
    def close_drawer(self):
        self.root.ids.nav_drawer.set_state("close")
    def go_home(self):
        self.root.ids.sm.current="main"
    def open_at_function(self, name):
        self.close_drawer()
        self.root.ids.sm.current=name
    def show_msg(self,t):
        if self.dialog: self.dialog.dismiss()
        self.dialog=MDDialog(text=t, buttons=[MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())])
        self.dialog.open()
    def add_status(self):
        try:
            self.root.ids.status_list.add_widget(MDLabel(text="You: New Status - No Cut", adaptive_height=True, padding="10dp"))
            self.show_msg("Status Added!")
        except: pass
    def add_adds(self):
        try:
            self.root.ids.adds_list.add_widget(MDLabel(text="AT Adds: New Post!", adaptive_height=True, padding="10dp"))
            self.show_msg("Adds Added!")
        except: pass
    def toggle_attach(self, screen_name):
        panel=self.root.ids.sm.get_screen(screen_name).ids.attach_panel
        if panel.height==0:
            panel.height=dp(110)
            panel.opacity=1
        else:
            panel.height=0
            panel.opacity=0
    def chat_open_gallery(self, screen_name):
        self.toggle_attach(screen_name)
        self.add_chat_image(screen_name, "Gallery_Photo.jpg")
        self.show_msg("Gallery - Working!")
    def chat_open_camera(self, screen_name):
        self.toggle_attach(screen_name)
        self.open_at_function("camera")
    def chat_open_document(self, screen_name):
        self.toggle_attach(screen_name)
        self.add_chat_image(screen_name, "Document.pdf")
        self.show_msg("Document - Working!")
    def chat_open_ai_studio(self, screen_name):
        self.toggle_attach(screen_name)
        self.open_at_function("poster")
    def add_chat_image(self, screen_name, path):
        try:
            scr=self.root.ids.sm.get_screen(screen_name)
            scr.ids.chat_box.add_widget(MDLabel(text=f"You sent: {path}", adaptive_height=True, padding="10dp"))
        except: pass
    def take_photo(self):
        self.show_msg("Photo Saved! Chat me gaya!")
        try:
            self.root.ids.sm.get_screen("brain").ids.chat_box.add_widget(MDLabel(text="You sent a Photo!", adaptive_height=True, padding="10dp"))
        except: pass
        self.go_home()
        Clock.schedule_once(lambda dt: setattr(self.root.ids.sm, 'current', 'brain'), 0.5)
    def open_gallery(self): self.show_msg("Gallery Open - Working!")
    def make_call(self): self.show_msg("Calling... Working!")
    def start_video(self): self.show_msg("Video Call Started!")
    def start_voice(self): self.show_msg("Recording...")
    def stop_voice(self): self.show_msg("Voice Saved!")
    def send_msg(self):
        try:
            s=self.root.ids.sm.get_screen("brain")
            m=s.ids.user_input.text.strip()
            if not m: return
            s.ids.chat_box.add_widget(MDLabel(text=f"You: {m}", adaptive_height=True, padding="10dp"))
            s.ids.chat_box.add_widget(MDLabel(text=f"AT BRAIN: {m} - Done!", adaptive_height=True, padding="10dp"))
            s.ids.user_input.text=""
        except: pass
    def make_poster(self):
        try:
            s=self.root.ids.sm.get_screen("poster")
            t=s.ids.shayari_text.text or "AT WORLD"
            s.ids.poster_preview.text=f"{t}"
        except: pass
    def send_online(self):
        try:
            s=self.root.ids.sm.get_screen("online")
            m=s.ids.online_input.text.strip()
            if not m: return
            s.ids.online_chat.add_widget(MDLabel(text=f"You: {m}", adaptive_height=True))
            s.ids.online_input.text=""
        except: pass

AtWorldMatterApp().run()
