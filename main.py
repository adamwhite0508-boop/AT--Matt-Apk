from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from datetime import datetime

class UserMainAI:
    def make_email(self, dept, prob):
        return f"To: {dept}@gov.in\nSubject: {prob}\n\nRespected Sir,\n{prob} at Gomti Nagar, Lucknow.\nResolve in 48hrs.\nThanks"

KV = '''
MDScreenManager:
    LoginScreen:
    MainScreen:
    ATWorldMenuScreen:
    ChatScreen:
    JarvisScreen:

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: "banner.png"
            size_hint: .78, .52
            pos_hint: {'center_x':.5,'center_y':.68}
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: .82,.32
            pos_hint: {'center_x':.5,'center_y':.25}
            spacing: "10dp"
            MDTextField:
                hint_text: "Email"
                icon_left: "email"
                mode: "round"
            MDTextField:
                hint_text: "Password"
                icon_left: "lock"
                password: True
                mode: "round"
            MDRaisedButton:
                text: "Log In"
                md_bg_color: 0.11,0.44,0.71,1
                size_hint_x: 1
                on_press: app.skip_login()

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: "64dp"
            md_bg_color: 0.11,0.44,0.71,1
            padding: [10,0]
            Image:
                source: "banner.png"
                size_hint: None, None
                size: "40dp","40dp"
                pos_hint: {'center_y':.5}
            MDLabel:
                text: "AT World Matter"
                bold: True
                text_color: 1,1,1,1
                padding: [8,0]
            MDIconButton:
                icon: "magnify"
                icon_color: 1,1,1,1
                pos_hint: {'center_y':.5}
                on_press: app.focus_search()
            MDIconButton:
                icon: "bell-outline"
                icon_color: 1,1,1,1
                pos_hint: {'center_y':.5}
            MDIconButton:
                id: three_dot_btn
                icon: "dots-vertical"
                icon_color: 1,1,1,1
                pos_hint: {'center_y':.5}
                on_release: app.open_three_dot_menu(self)
        MDCard:
            size_hint_y: None
            height: "48dp"
            md_bg_color: 0.96,0.96,0.96,1
            radius: [0,0,12,12]
            padding: [12,0]
            MDTextField:
                id: main_search
                hint_text: "Search chats, status, ads..."
                mode: "fill"
                fill_color: 0,0,0,0
                line_color_normal: 0,0,0,0
        ScrollView:
            MDList:
                id: dynamic_list
                padding: "6dp"
        MDCard:
            size_hint_y: None
            height: "64dp"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "chat"
                        text_color: 0.11,0.44,0.71,1
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('chats')
                    MDLabel:
                        text: "Chats"
                        halign: "center"
                        font_size: "10sp"
                        bold: True
                        text_color: 0.11,0.44,0.71,1
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "update"
                        pos_hint: {'center_x':.5}
                    MDLabel:
                        text: "Updates"
                        halign: "center"
                        font_size: "10sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "bullhorn"
                        pos_hint: {'center_x':.5}
                    MDLabel:
                        text: "Ads"
                        halign: "center"
                        font_size: "10sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "phone"
                        pos_hint: {'center_x':.5}
                    MDLabel:
                        text: "Calls"
                        halign: "center"
                        font_size: "10sp"

<ATWorldMenuScreen>:
    name: 'at_menu'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: "58dp"
            md_bg_color: 0.11,0.44,0.71,1
            MDIconButton:
                icon: "arrow-left"
                icon_color: 1,1,1,1
                on_press: app.root.current = 'main'
            MDLabel:
                text: "AT World - 7 Tools"
                bold: True
                text_color: 1,1,1,1
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "14dp"
                spacing: "10dp"
                adaptive_height: True
                MDCard:
                    size_hint_y: None
                    height: "68dp"
                    md_bg_color: 0.65,0.85,0.98,1
                    radius: [14]
                    padding: "12dp"
                    on_release: app.root.current = 'jarvis'
                    MDLabel:
                        text: "AT Brain - AI Chat & Jarvis Email"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Matter - Scenes"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.9,0.9,1,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Tools 3"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.9,0.9,1,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Tools 4"
                        bold: True

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: chat_bar
            title: "Contact"
            type: "small"
            md_bg_color: 0.11,0.44,0.71,1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        ScrollView:
            MDBoxLayout:
                id: msg_list
                orientation: 'vertical'
                padding: "10dp"
                spacing: "8dp"
                adaptive_height: True
        MDCard:
            size_hint_y: None
            height: "58dp"
            padding: "6dp"
            MDTextField:
                id: msg_input
                hint_text: "Message"
                mode: "round"
            MDIconButton:
                icon: "send"
                on_press: app.send_message()

<JarvisScreen>:
    name: 'jarvis'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Brain - Jarvis Email"
            type: "small"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'at_menu')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: "16dp"
            spacing: "12dp"
            MDTextField:
                id: jarvis_dept
                hint_text: "Department"
                text: "Jal Vibhag Lucknow"
            MDTextField:
                id: jarvis_problem
                hint_text: "Problem"
            MDRaisedButton:
                text: "Email Banwao"
                md_bg_color: 0.11,0.44,0.71,1
                size_hint_x: 1
                on_press: app.generate_jarvis_email()
            MDScrollView:
                MDLabel:
                    id: jarvis_output
                    adaptive_height: True
'''

class LoginScreen(Screen): pass
class MainScreen(Screen): pass
class ATWorldMenuScreen(Screen): pass
class ChatScreen(Screen): pass
class JarvisScreen(Screen): pass

class ATWorldMatterApp(MDApp):
    three_dot_menu = None
    def build(self):
        self.all_chats = [("AJ", "Alice Johnson", "Sounds good!", "10:32", "2")]
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(lambda dt: self.show_tab('chats'), 0.3)
        # 3 DOT MENU ITEMS - YEHI AAPKA FEATURE HAI
        menu_items = [
            {"text": "AT World - 7 Tools", "viewclass": "OneLineListItem", "on_release": lambda x="AT World - 7 Tools": self.menu_callback(x)},
            {"text": "AT Brain - Jarvis Email", "viewclass": "OneLineListItem", "on_release": lambda x="AT Brain": self.menu_callback(x)},
            {"text": "Profile", "viewclass": "OneLineListItem", "on_release": lambda x="Profile": self.menu_callback(x)},
            {"text": "Settings", "viewclass": "OneLineListItem", "on_release": lambda x="Settings": self.menu_callback(x)},
            {"text": "About", "viewclass": "OneLineListItem", "on_release": lambda x="About": self.menu_callback(x)},
            {"text": "Logout", "viewclass": "OneLineListItem", "on_release": lambda x="Logout": self.menu_callback(x)},
        ]
        # menu ko baad me banayenge jab screen ready hogi

    def open_three_dot_menu(self, button):
        menu_items = [
            {"text": "AT World - 7 Tools", "viewclass": "OneLineListItem", "on_release": lambda x="at_menu": self.menu_callback(x)},
            {"text": "AT Brain - Jarvis", "viewclass": "OneLineListItem", "on_release": lambda x="jarvis": self.menu_callback(x)},
            {"text": "Profile", "viewclass": "OneLineListItem", "on_release": lambda x="profile": self.menu_callback(x)},
            {"text": "Settings", "viewclass": "OneLineListItem", "on_release": lambda x="settings": self.menu_callback(x)},
        ]
        self.three_dot_menu = MDDropdownMenu(caller=button, items=menu_items, width_mult=4)
        self.three_dot_menu.open()

    def menu_callback(self, screen_name):
        self.three_dot_menu.dismiss()
        if screen_name in ['at_menu','jarvis']:
            self.root.current = screen_name
        else:
            print(f"{screen_name} clicked")

    def show_tab(self, tab):
        from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingAvatar
        lst = self.root.get_screen('main').ids.dynamic_list
        lst.clear_widgets()
        if tab == 'chats':
            for av, name, msg, time, unread in self.all_chats:
                item = MDListItem(MDListItemLeadingAvatar(text=av), MDListItemHeadlineText(text=name, bold=True), MDListItemSupportingText(text=f"{msg} • {time}"))
                item.bind(on_release=lambda x, n=name: self.open_chat(n))
                lst.add_widget(item)
    def focus_search(self): self.root.get_screen('main').ids.main_search.focus = True
    def skip_login(self): self.root.current = 'main'
    def open_at_world_menu(self): self.root.current = 'at_menu'
    def open_chat(self, name):
        self.root.get_screen('chat').ids.chat_bar.title = name
        self.root.current = 'chat'
    def send_message(self): self.root.get_screen('chat').ids.msg_input.text = ""
    def generate_jarvis_email(self):
        d = self.root.get_screen('jarvis').ids.jarvis_dept.text
        p = self.root.get_screen('jarvis').ids.jarvis_problem.text
        self.root.get_screen('jarvis').ids.jarvis_output.text = UserMainAI().make_email(d, p)

ATWorldMatterApp().run()
