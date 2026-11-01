from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar
from kivy.clock import Clock
from kivy.metrics import dp

KV = '''
#:import FitImage kivymd.uix.fitimage.FitImage

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
        FitImage:
            source: "login_banner.png"
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
        MDCard:
            size_hint_y: None
            height: "180dp"
            radius: [0,0,22,22]
            md_bg_color: 0.06,0.4,0.7,1
            FitImage:
                source: "main__header.png"
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
            text_color_active: 0.06,
