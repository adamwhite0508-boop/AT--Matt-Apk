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
        MDLabel:
            text: "AT World Matter"
            halign: "center"
            bold: True
            font_size: "28sp"
            text_color: 0.06,0.45,0.73,1
            pos_hint: {'center_y':.78}
        MDLabel:
            text: "Ocean Blue Light • Fast Login"
            halign: "center"
            font_size: "12sp"
            text_color: 0.06,0.45,0.73,0.6
            pos_hint: {'center_y':.74}
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: .85,.26
            pos_hint: {'center_x':.5,'center_y':.48}
            spacing: "14dp"
            MDTextField:
                hint_text: "Mobile number - Fast Login"
                icon_left: "cellphone"
            MDTextField:
                hint_text: "OTP"
                icon_left: "key"
        MDRaisedButton:
            text: "Skip - Demo Login"
            md_bg_color: 0.06,0.45,0.73,1
            pos_hint: {'center_x':.5,'center_y':.28}
            size_hint_x: .7
            on_press: app.skip_login()

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.92,0.97,1,1
        MDBoxLayout:
            size_hint_y: None
            height: "68dp"
            md_bg_color: 0.06,0.45,0.73,1
            padding: [8,0,2,0]
            MDIconButton:
                icon: "earth"
                icon_color: 1,1,1,1
                icon_size: "28sp"
                md_bg_color: 0.1,0.55,0.85,1
                on_press: app.open_at_world_menu()
            MDLabel:
                text: "AT World"
                bold: True
                text_color: 1,1,1,1
                font_size: "22sp"
                padding: [8,0]
            MDIconButton:
                icon: "magnify"
                icon_color: 1,1,1,1
                on_press: app.focus_search()
            MDIconButton:
                icon: "camera-outline"
                icon_color: 1,1,1,1
            MDIconButton:
                icon: "dots-vertical"
                icon_color: 1,1,1,1
        MDCard:
            size_hint_y: None
            height: "48dp"
            md_bg_color: 1,1,1,1
            radius: [0,0,18,18]
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
            height: "68dp"
            md_bg_color: 1,1,1,1
            radius: [18,18,0,0]
            MDBoxLayout:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        id: tab_chats
                        icon: "chat"
                        theme_text_color: "Custom"
                        text_color: 0.06,0.45,0.73,1
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('chats')
                    MDLabel:
                        text: "Chats"
                        halign: "center"
                        font_size: "11sp"
                        bold: True
                        text_color: 0.06,0.45,0.73,1
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        id: tab_updates
                        icon: "update"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('updates')
                    MDLabel:
                        text: "Updates"
                        halign: "center"
                        font_size: "11sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        id: tab_ads
                        icon: "bullhorn"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('ads')
                    MDLabel:
                        text: "Ads"
                        halign: "center"
                        font_size: "11sp"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        id: tab_calls
                        icon: "phone"
                        pos_hint: {'center_x':.5}
                        on_press: app.show_tab('calls')
                    MDLabel:
                        text: "Calls"
                        halign: "center"
                        font_size: "11sp"

<ATWorldMenuScreen>:
    name: 'at_menu'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.78,0.89,0.98,1
        MDBoxLayout:
            size_hint_y: None
            height: "68dp"
            md_bg_color: 0.06,0.45,0.73,1
            padding: [8,0]
            MDIconButton:
                icon: "arrow-left"
                icon_color: 1,1,1,1
                on_press: app.root.current = 'main'
            MDLabel:
                text: "AT World - 7 Tools"
                bold: True
                font_size: "19sp"
                text_color: 1,1,1,1
                padding: [8,0]
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "14dp"
                spacing: "12dp"
                adaptive_height: True
                MDCard:
                    size_hint_y: None
                    height: "72dp"
                    md_bg_color: 0.65,0.85,0.98,1
                    radius: [16]
                    padding: "12dp"
                    on_release: app.root.current = 'jarvis'
                    MDLabel:
                        text: "AT Brain - AI Chat & Jarvis Email"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "72dp"
                    md_bg_color: 1,0.9,0.7,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Remote X - AnyDesk Killer - Small icon big work"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Matter - Scenes"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Poster Studio - Create Posters"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Avatar Studio - AI Avatars"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Security Guard - Protection"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [16]
                    padding: "12dp"
                    MDLabel:
                        text: "AT Compressor - Compress Files"
                        bold: True

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.89,0.85,0.78,1
        MDTopAppBar:
            id: chat_bar
            title: "Contact"
            type: "small"
            md_bg_color: 0.06,0.45,0.73,1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
            right_action_items: [["video", lambda x: None], ["phone", lambda x: None]]
        ScrollView:
            MDBoxLayout:
                id: msg_list
                orientation: 'vertical'
                padding: "10dp"
                spacing: "8dp"
                adaptive_height: True
        MDCard:
            size_hint_y: None
            height: "62dp"
            md_bg_color: 1,1,1,1
            radius: [18,18,0,0]
            padding: "6dp"
            MDTextField:
                id: msg_input
                hint_text: "Message"
                mode: "round"
            MDIconButton:
                icon: "send"
                theme_text_color: "Custom"
                text_color: 0.06,0.45,0.73,1
                on_press: app.send_message()

<JarvisScreen>:
    name: 'jarvis'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.95,0.98,1,1
        MDTopAppBar:
            title: "AT Brain - Jarvis Email"
            type: "small"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'at_menu')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: "16dp"
            spacing: "14dp"
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
        self.all_chats = [
            ("AJ", "Alice Johnson", "Sounds good! See you then", "10:32", "2"),
            ("M", "Mom", "Don't forget to call me", "09:15", ""),
            ("JP", "John Patel", "Sent document please review", "Yesterday", "1"),
        ]
        self.status_data = [("Alice","10:32 AM","Mom, John, You"),("Mom","09:15 AM","Alice, You")]
        self.ads_data = [("iPhone 15 - 45k","Gomti Nagar • 2h ago"),("1BHK Rent","Indira Nagar • 5h ago")]
        self.call_data = [("Alice","Outgoing • 2:34 • Today","phone",False),("Mom","Missed • Yesterday","phone-missed",True),("John","Incoming • 5:12","phone-incoming",False)]
        return Builder.load_string(KV)
    
    def on_start(self):
        Clock.schedule_once(lambda dt: self.show_tab('chats'), 0.3)
    
    def show_tab(self, tab):
        from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingAvatar, MDListItemTrailingIcon, MDListItemTrailingSupportingText
        main = self.root.get_screen('main')
        lst = main.ids.dynamic_list
        lst.clear_widgets()
        for t in ['chats','updates','ads','calls']:
            try: main.ids[f'tab_{t}'].text_color = (0.06,0.45,0.73,1) if t==tab else (0.5,0.5,0.5,1)
            except: pass
        if tab == 'chats':
            for av, name, msg, time, unread in self.all_chats:
                item = MDListItem(MDListItemLeadingAvatar(text=av), MDListItemHeadlineText(text=name, bold=True), MDListItemSupportingText(text=f"{msg}"), MDListItemTrailingSupportingText(text=f"{time} ✓✓"))
                item.bind(on_release=lambda x, n=name: self.open_chat(n))
                lst.add_widget(item)
        elif tab == 'updates':
            lst.add_widget(MDListItem(MDListItemLeadingAvatar(icon="plus"), MDListItemHeadlineText(text="My Status"), MDListItemSupportingText(text="Tap to add - Who viewed?")))
            for name, time, seen in self.status_data:
                lst.add_widget(MDListItem(MDListItemLeadingAvatar(text=name[0]), MDListItemHeadlineText(text=name), MDListItemSupportingText(text=f"{time} • Seen by: {seen}")))
        elif tab == 'ads':
            for title, info in self.ads_data:
                lst.add_widget(MDListItem(MDListItemHeadlineText(text=title, bold=True), MDListItemSupportingText(text=info)))
            lst.add_widget(MDListItem(MDListItemLeadingAvatar(icon="plus-box"), MDListItemHeadlineText(text="Post Your Ad"), MDListItemSupportingText(text="Ocean Blue Marketplace")))
        elif tab == 'calls':
            for name, info, icon, missed in self.call_data:
                lst.add_widget(MDListItem(MDListItemLeadingAvatar(text=name[0]), MDListItemHeadlineText(text=name, bold=True), MDListItemSupportingText(text=info), MDListItemTrailingIcon(icon=icon)))

    def filter_chats(self, text):
        if not text: self.show_tab('chats'); return
        from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingAvatar, MDListItemTrailingSupportingText
        lst = self.root.get_screen('main').ids.dynamic_list
        lst.clear_widgets()
        for av, name, msg, time, unread in self.all_chats:
            if text.lower() in name.lower() or text.lower() in msg.lower():
                item = MDListItem(MDListItemLeadingAvatar(text=av), MDListItemHeadlineText(text=name, bold=True), MDListItemSupportingText(text=f"{msg} • {time} ✓✓"), MDListItemTrailingSupportingText(text=time))
                item.bind(on_release=lambda x, n=name: self.open_chat(n))
                lst.add_widget(item)

    def focus_search(self): self.root.get_screen('main').ids.main_search.focus = True
    def skip_login(self): self.root.current = 'main'
    def open_at_world_menu(self): self.root.current = 'at_menu'
    def open_chat(self, name):
        self.root.get_screen('chat').ids.chat_bar.title = name
        self.root.get_screen('chat').ids.msg_list.clear_widgets()
        from kivymd.uix.card import MDCard
        from kivymd.uix.label import MDLabel
        for txt, me, t in [("Hi! Document bheja hai", False, "09:10"), ("Sounds good! See you then", True, "10:32 ✓✓ Seen")]:
            c = MDCard(md_bg_color=(0.06,0.45,0.73,1) if me else (1,1,1,1), radius=[16,16,2,16] if me else [16,16,16,2], size_hint_y=None, size_hint_x=None, width=280, height=55, padding=[12,8], pos_hint={'right':1} if me else {'x':0})
            c.add_widget(MDLabel(text=f"{txt}\n[font_size=10]{t}[/font_size]", text_color=(1,1,1,1) if me else (0,0,0,1), markup=True))
            self.root.get_screen('chat').ids.msg_list.add_widget(c)
        self.root.current = 'chat'

    def send_message(self):
        txt = self.root.get_screen('chat').ids.msg_input.text.strip()
        if not txt: return
        ok,_ = self.security.check_all("user", txt)
        if not ok: return
        from kivymd.uix.card import MDCard
        from kivymd.uix.label import MDLabel
        c = MDCard(md_bg_color=(0.06,0.45,0.73,1), radius=[16,16,2,16], size_hint_y=None, size_hint_x=None, width=280, height=55, padding=[12,8], pos_hint={'right':1})
        c.add_widget(MDLabel(text=f"{txt}\n[font_size=10]10:35 AM ✓✓ Seen[/font_size]", text_color=(1,1,1,1), markup=True))
        self.root.get_screen('chat').ids.msg_list.add_widget(c)
        self.root.get_screen('chat').ids.msg_input.text = ""
        if self.brain.get_reply(txt) == "JARVIS_MODE": Clock.schedule_once(lambda dt: setattr(self.root, 'current', 'jarvis'), 0.5)

    def generate_jarvis_email(self):
        d = self.root.get_screen('jarvis').ids.jarvis_dept.text
        p = self.root.get_screen('jarvis').ids.jarvis_problem.text
        self.root.get_screen('jarvis').ids.jarvis_output.text = self.brain.make_email(d, p)

ATWorldMatterApp().run()
