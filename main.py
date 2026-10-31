from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from datetime import datetime

class SecurityGuard:
    def check_all(self, uid, msg):
        bad = ["abuse","bomb","gaali","hack","crack","sarkar virodhi","terror"]
        for w in bad:
            if w in msg.lower(): return False, f"🚫 {w} blocked"
        return True, ""

class UserMainAI:
    def get_reply(self, txt): 
        return "JARVIS_MODE" if "email" in txt.lower() else "OK"
    def make_email(self, dept, prob):
        return f"To: {dept}@gov.in\nSubject: {prob}\n\nRespected Sir,\n{prob} at Gomti Nagar Lucknow (226010).\nConsumer: AT-4521\nResolve in 48hrs.\n\nThanks\n{datetime.now().strftime('%d-%m-%Y')}"

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
        # --- BINA BANNER KE - TEXT LOGO ---
        MDIcon:
            icon: "earth"
            font_size: "110sp"
            text_color: 0.06,0.45,0.73,1
            pos_hint: {'center_x':.5,'center_y':.72}
            halign: "center"
        MDLabel:
            text: "AT World Matter"
            halign: "center"
            bold: True
            font_size: "32sp"
            text_color: 0.06,0.45,0.73,1
            pos_hint: {'center_x':.5,'center_y':.56}
        MDLabel:
            text: "Matter"
            halign: "center"
            font_size: "28sp"
            text_color: 0.6,0.75,0.9,1
            pos_hint: {'center_x':.5,'center_y':.50}
        
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: .82,.34
            pos_hint: {'center_x':.5,'center_y':.26}
            spacing: "12dp"
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
                md_bg_color: 0.06,0.45,0.73,1
                size_hint_x: 1
                on_press: app.skip_login()
            MDLabel:
                text: "Forgot password?"
                halign: "center"
                font_size: "11sp"
                text_color: 0.06,0.45,0.73,1
            MDLabel:
                text: "Version 1.0 • AT World Matter © 2024"
                halign: "center"
                font_size: "9sp"
                text_color: 0.5,0.5,0.5,1

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDBoxLayout:
            size_hint_y: None
            height: "58dp"
            md_bg_color: 0.06,0.45,0.73,1
            padding: [8,0]
            MDIcon:
                icon: "earth"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "28sp"
                pos_hint: {'center_y':.5}
            MDLabel:
                text: "AT World Matter"
                bold: True
                font_size: "18sp"
                text_color: 1,1,1,1
                padding: [8,0]
            MDIconButton:
                icon: "magnify"
                icon_color: 1,1,1,1
            MDIconButton:
                icon: "dots-vertical"
                icon_color: 1,1,1,1
                on_press: app.open_at_world_menu()
        MDCard:
            size_hint_y: None
            height: "44dp"
            md_bg_color: 0.96,0.96,0.96,1
            radius: [0,0,12,12]
            padding: [12,0]
            MDTextField:
                id: main_search
                hint_text: "Search chats, status, ads..."
                mode: "fill"
                fill_color: 0,0,0,0
                line_color_normal: 0,0,0,0
                on_text: app.filter_chats(self.text)
        ScrollView:
            MDList:
                id: dynamic_list
                padding: "6dp"
        MDCard:
            size_hint_y: None
            height: "62dp"
            md_bg_color: 1,1,1,1
            radius: [14,14,0,0]
            MDBoxLayout:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "chat"
                        text_color: 0.06,0.45,0.73,1
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('chats')
                    MDLabel:
                        text: "Chats"
                        halign: "center"
                        font_size: "10sp"
                        bold: True
                        text_color: 0.06,0.45,0.73,1
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "update"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('updates')
                    MDLabel:
                        text: "Updates"
                        halign: "center"
                        font_size: "10sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "bullhorn"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('ads')
                    MDLabel:
                        text: "Ads"
                        halign: "center"
                        font_size: "10sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: "phone"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('calls')
                    MDLabel:
                        text: "Calls"
                        halign: "center"
                        font_size: "10sp"

<ATWorldMenuScreen>:
    name: 'at_menu'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.92,0.97,1,1
        MDBoxLayout:
            size_hint_y: None
            height: "58dp"
            md_bg_color: 0.06,0.45,0.73,1
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

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: chat_bar
            title: "Contact"
            type: "small"
            md_bg_color: 0.06,0.45,0.73,1
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
            md_bg_color: 1,1,1,1
            padding: "6dp"
            MDTextField:
                id: msg_input
                hint_text: "Message"
                mode: "round"
            MDIconButton:
                icon: "send"
                text_color: 0.06,0.45,0.73,1
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
                text: "Pipeline tooti hai, 3 din se paani nahi"
            MDRaisedButton:
                text: "Email Banwao"
                md_bg_color: 0.06,0.45,0.73,1
                size_hint_x: 1
                on_press: app.generate_jarvis_email()
            MDScrollView:
                MDLabel:
                    id: jarvis_output
                    text: "Email yaha banega..."
                    adaptive_height: True
'''

class LoginScreen(Screen): pass
class MainScreen(Screen): pass
class ATWorldMenuScreen(Screen): pass
class ChatScreen(Screen): pass
class JarvisScreen(Screen): pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.security = SecurityGuard()
        self.brain = UserMainAI()
        self.all_chats = [("AJ", "Alice Johnson", "Sounds good!", "10:32", "2"), ("M", "Mom", "Don't forget to call", "09:15", "")]
        return Builder.load_string(KV)
    def on_start(self): Clock.schedule_once(lambda dt: self.show_tab('chats'), 0.3)
    def show_tab(self, tab):
        from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingAvatar
        main = self.root.get_screen('main')
        lst = main.ids.dynamic_list
        lst.clear_widgets()
        if tab == 'chats':
            for av, name, msg, time, unread in self.all_chats:
                item = MDListItem(MDListItemLeadingAvatar(text=av), MDListItemHeadlineText(text=name, bold=True), MDListItemSupportingText(text=f"{msg} • {time}"))
                item.bind(on_release=lambda x, n=name: self.open_chat(n))
                lst.add_widget(item)
    def filter_chats(self, text): pass
    def focus_search(self): self.root.get_screen('main').ids.main_search.focus = True
    def skip_login(self): self.root.current = 'main'
    def open_at_world_menu(self): self.root.current = 'at_menu'
    def open_chat(self, name):
        self.root.get_screen('chat').ids.chat_bar.title = name
        self.root.current = 'chat'
    def send_message(self):
        txt = self.root.get_screen('chat').ids.msg_input.text.strip()
        if not txt: return
        self.root.get_screen('chat').ids.msg_input.text = ""
    def generate_jarvis_email(self):
        d = self.root.get_screen('jarvis').ids.jarvis_dept.text
        p = self.root.get_screen('jarvis').ids.jarvis_problem.text
        self.root.get_screen('jarvis').ids.jarvis_output.text = self.brain.make_email(d, p)

ATWorldMatterApp().run()
