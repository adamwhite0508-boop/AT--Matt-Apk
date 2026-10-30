from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp
import random
from datetime import datetime

KV = '''
MDScreenManager:
    LoginScreen:
    MainScreen:
    ChatScreen:
    VideoScreen:
    SettingsScreen:
    PosterScreen:
    AvatarScreen:
    AdminScreen:
    GroupCallScreen:
    StatusScreen:

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: 'banner.png'
            size_hint: .7,.32
            pos_hint: {'center_x':.5,'center_y':.75}
        MDLabel:
            text: "AT World Mater"
            halign: "center"
            bold: True
            text_color: 0.06,0.45,0.73,1
            pos_hint: {'center_y':.56}
            font_size: "20sp"
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: .85,.32
            pos_hint: {'center_x':.5,'center_y':.35}
            spacing: "12dp"
            MDTextField:
                id: phone_input
                hint_text: "Mobile number"
                input_filter: "int"
                max_text_length: 10
                icon_left: "cellphone"
            MDTextField:
                id: otp_input
                hint_text: "OTP"
                input_filter: "int"
                max_text_length: 6
                icon_left: "key"
            MDLabel:
                id: otp_status
                text: "Simple Mode - No Internet Needed ✅"
                halign: "center"
                font_size: "11sp"
                text_color: 0,0.6,0,1
        MDBoxLayout:
            size_hint: .85,None
            height: "48dp"
            pos_hint: {'center_x':.5,'center_y':.17}
            spacing: "10dp"
            MDRaisedButton:
                text: "Send OTP"
                md_bg_color: 0.06,0.45,0.73,1
                size_hint_x: .5
                on_press: app.send_otp()
            MDRaisedButton:
                text: "Verify"
                md_bg_color: 0,0.6,0.2,1
                size_hint_x: .5
                on_press: app.verify_otp()
        MDTextButton:
            text: "Skip - Demo Login"
            text_color: 0.06,0.45,0.73,1
            bold: True
            pos_hint: {'center_x':.5,'center_y':.09}
            on_press: app.skip_login()

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AT World Mater"
            md_bg_color: 1,1,1,1
            specific_text_color: 0.06,0.45,0.73,1
            right_action_items: [["bell-ring", lambda x: app.test_local_push()], ["shield-account", lambda x: setattr(app.root, 'current', 'admin')], ["cog", lambda x: setattr(app.root, 'current', 'settings')]]
        MDBoxLayout:
            size_hint_y: None
            height: "48dp"
            MDFlatButton:
                id: tab_chats
                text: "CHATS"
                bold: True
                text_color: 0.06,0.45,0.73,1
                size_hint_x: .25
                on_press: app.switch_tab('chats')
            MDFlatButton:
                id: tab_status
                text: "STATUS"
                text_color: 0.6,0.6,0.6,1
                size_hint_x: .25
                on_press: app.switch_tab('status')
            MDFlatButton:
                id: tab_groups
                text: "GROUPS"
                text_color: 0.6,0.6,0.6,1
                size_hint_x: .25
                on_press: app.switch_tab('groups')
            MDFlatButton:
                id: tab_calls
                text: "CALLS"
                text_color: 0.6,0.6,0.6,1
                size_hint_x: .25
                on_press: app.switch_tab('calls')
        ScrollView:
            MDList:
                id: chat_list
        MDFloatLayout:
            size_hint_y: None
            height: "75dp"
            MDFabButton:
                id: fab
                icon: "message-text"
                md_bg_color: 0.06,0.45,0.73,1
                pos_hint: {'x':.82,'y':.15}
                on_press: app.fab_action()

<StatusScreen>:
    name: 'status_main'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "Status"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
            right_action_items: [["plus", lambda x: app.add_status()]]
        ScrollView:
            MDList:
                id: status_list
                padding: "10dp"

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.93,0.9,0.84,1
        MDTopAppBar:
            id: chat_title
            title: "Chat"
            md_bg_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
            right_action_items: [["video", lambda x: app.start_video_call(app.current_chat)], ["phone", lambda x: app.start_call(app.current_chat)], ["paperclip", lambda x: app.share_file()]]
        MDLabel:
            id: status_label
            text: "online"
            font_size: "11sp"
            text_color: 0,0.6,0,1
            size_hint_y: None
            height: "18dp"
            padding: [15,0]
            md_bg_color: 1,1,1,1
        ScrollView:
            id: chat_scroll
            MDList:
                id: msg_list
                padding: "10dp"
                spacing: "6dp"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            padding: "6dp"
            spacing: "6dp"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "microphone"
                theme_text_color: "Custom"
                text_color: 0.06,0.45,0.73,1
                on_press: app.start_voice_record()
                on_release: app.stop_voice_record()
            MDTextField:
                id: msg_input
                hint_text: "Message"
                mode: "round"
                on_text: app.show_typing(self.text)
            MDIconButton:
                icon: "send"
                md_bg_color: 0.06,0.45,0.73,1
                icon_color: 1,1,1,1
                on_press: app.send_message()

<VideoScreen>:
    name: 'video'
    MDFloatLayout:
        md_bg_color: 0.05,0.05,0.08,1
        Image:
            source: 'icon.png'
            size_hint: .5,.5
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            id: video_name
            text: "Calling..."
            halign: "center"
            text_color: 1,1,1,1
            font_style: "H6"
            pos_hint: {'center_y':.32}
        MDLabel:
            id: agora_status
            text: "Demo Mode - Real Call in Next Update"
            halign: "center"
            text_color: 0,1,0,1
            font_size: "12sp"
            pos_hint: {'center_y':.25}
        MDFabButton:
            icon: "phone-hangup"
            md_bg_color: 1,0.2,0.2,1
            pos_hint: {'center_x':.5,'y':.05}
            on_release: app.root.current = 'main'

<GroupCallScreen>:
    name: 'groupcall'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.05,0.05,0.08,1
        MDTopAppBar:
            title: "Group Call - 6 People"
            md_bg_color: 0.1,0.1,0.1,1
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        MDGridLayout:
            cols: 2
            spacing: "5dp"
            padding: "5dp"
            MDCard:
                md_bg_color: 0.2,0.2,0.2,1
                MDLabel:
                    text: "You"
                    halign: "center"
                    text_color: 0,1,0,1
            MDCard:
                md_bg_color: 0.2,0.2,0.2,1
                MDLabel:
                    text: "Anuj"
                    halign: "center"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.2,0.2,0.2,1
                MDLabel:
                    text: "Riya"
                    halign: "center"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.2,0.2,0.2,1
                MDLabel:
                    text: "+3 more"
                    halign: "center"
                    text_color: 1,1,0,1
        MDFabButton:
            icon: "phone-hangup"
            md_bg_color: 1,0.2,0.2,1
            pos_hint: {'center_x':.5,'y':.05}
            on_release: app.root.current = 'main'

<PosterScreen>:
    name: 'poster'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "Poster Studio"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: "15dp"
            spacing: "12dp"
            MDTextField:
                id: poster_text
                hint_text: "Poster pe kya likhna hai?"
                text: "AT World Mater"
            MDCard:
                size_hint_y: None
                height: "250dp"
                md_bg_color: 0.06,0.45,0.73,1
                padding: "15dp"
                MDLabel:
                    id: poster_preview
                    text: "AT World Mater\\nPoster Preview"
                    halign: "center"
                    text_color: 1,1,1,1
                    font_style: "H5"
                    bold: True
            MDBoxLayout:
                size_hint_y: None
                height: "45dp"
                spacing: "10dp"
                MDRaisedButton:
                    text: "Blue Theme"
                    md_bg_color: 0.06,0.45,0.73,1
                    size_hint_x: .5
                    on_press: app.create_poster('blue')
                MDRaisedButton:
                    text: "Festival"
                    md_bg_color: 1,0.5,0,1
                    size_hint_x: .5
                    on_press: app.create_poster('festival')
            MDRaisedButton:
                text: "Save Poster"
                md_bg_color: 0,0.6,0.2,1
                pos_hint: {'center_x':.5}
                on_press: app.save_poster()

<AvatarScreen>:
    name: 'avatar'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AI Avatar Studio"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: "15dp"
            spacing: "15dp"
            Image:
                id: avatar_img
                source: 'icon.png'
                size_hint: None,None
                size: "200dp","200dp"
                pos_hint: {'center_x':.5}
            MDLabel:
                id: avatar_status
                text: "Tap to generate your avatar"
                halign: "center"
            MDBoxLayout:
                size_hint_y: None
                height: "45dp"
                spacing: "10dp"
                MDRaisedButton:
                    text: "Business"
                    size_hint_x: .33
                    on_press: app.generate_avatar('business')
                MDRaisedButton:
                    text: "Cartoon"
                    md_bg_color: 0.6,0.2,0.8,1
                    size_hint_x: .33
                    on_press: app.generate_avatar('cartoon')
                MDRaisedButton:
                    text: "AI Pro"
                    md_bg_color: 0,0.6,0.2,1
                    size_hint_x: .33
                    on_press: app.generate_avatar('pro')

<SettingsScreen>:
    name: 'settings'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "Settings"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "18dp"
                spacing: "18dp"
                adaptive_height: True
                MDLabel:
                    text: "Icon Size Adjust"
                    bold: True
                MDSlider:
                    id: icon_slider
                    min: 30
                    max: 80
                    value: 50
                    on_value: app.adjust_icon_size(*args)
                MDRaisedButton:
                    text: "Test Notification 🔔"
                    md_bg_color: 0.06,0.45,0.73,1
                    pos_hint: {'center_x':.5}
                    on_press: app.test_local_push()
                MDRaisedButton:
                    text: "Save & Apply"
                    md_bg_color: 0,0.6,0.2,1
                    pos_hint: {'center_x':.5}
                    on_press: app.save_icon_settings()
                MDTextButton:
                    text: "Logout"
                    pos_hint: {'center_x':.5}
                    on_press: app.logout()

<AdminScreen>:
    name: 'admin'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "ADMIN - All Chats (Local)"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
        ScrollView:
            MDList:
                id: admin_list
'''

from kivymd.uix.screen import MDScreen
class LoginScreen(MDScreen): pass
class MainScreen(MDScreen): pass
class ChatScreen(MDScreen): pass
class VideoScreen(MDScreen): pass
class SettingsScreen(MDScreen): pass
class PosterScreen(MDScreen): pass
class AvatarScreen(MDScreen): pass
class AdminScreen(MDScreen): pass
class GroupCallScreen(MDScreen): pass
class StatusScreen(MDScreen): pass

class ATWorldMatterApp(MDApp):
    current_chat = StringProperty("")
    current_tab = StringProperty("chats")
    icon_size = NumericProperty(50)
    is_recording = BooleanProperty(False)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.store = JsonStore("at_chats.json")
        return Builder.load_string(KV)

    def on_start(self):
        if self.store.exists("ICON_SETTINGS"):
            self.icon_size = self.store.get("ICON_SETTINGS")['size']
        if self.store.exists("USER_LOGIN"):
            self.root.current = 'main'
            Clock.schedule_once(lambda x: self.load_chats(), 0.3)
        else:
            self.root.current = 'login'

    def send_otp(self):
        s = self.root.get_screen('login')
        if len(s.ids.phone_input.text) != 10:
            s.ids.otp_status.text = "10 digit number dalo"
            return
        otp = random.randint(100000, 999999)
        self.current_otp = str(otp)
        self.temp_phone = s.ids.phone_input.text
        s.ids.otp_status.text = f"Demo OTP: {otp} ✅"

    def verify_otp(self):
        s = self.root.get_screen('login')
        if hasattr(self, 'current_otp') and s.ids.otp_input.text == self.current_otp:
            self.store.put("USER_LOGIN", phone=self.temp_phone)
            self.root.current = 'main'
            self.load_chats()
        else:
            s.ids.otp_status.text = f"Wrong! Sahi OTP {getattr(self, 'current_otp', '')} hai"

    def skip_login(self):
        self.store.put("USER_LOGIN", phone="DEMO")
        self.root.current = 'main'
        self.load_chats()

    def logout(self):
        if self.store.exists("USER_LOGIN"):
            self.store.delete("USER_LOGIN")
        self.root.current = 'login'

    def adjust_icon_size(self, i, v): self.icon_size = int(v)
    def save_icon_settings(self):
        self.store.put("ICON_SETTINGS", size=self.icon_size)
        self.root.current = 'main'
        self.load_chats()

    def test_local_push(self):
        try:
            from plyer import notification
            notification.notify(title="AT World Mater 🔔", message="Local Push - Simple Mode ✅", app_name="AT World Mater")
        except: print("Push Sent")
        print("Push Sent ✅")

    def switch_tab(self, tab):
        self.current_tab = tab
        sc = self.root.get_screen('main')
        for tid in ['tab_chats', 'tab_status', 'tab_groups', 'tab_calls']:
            sc.ids[tid].text_color = (0.6, 0.6, 0.6, 1)
        sc.ids[f'tab_{tab}'].text_color = (0.06, 0.45, 0.73, 1)
        if tab == 'chats':
            sc.ids.fab.icon = "message-text"
            self.load_chats()
        elif tab == 'status':
            sc.ids.fab.icon = "plus"
            self.load_status()
            sc.ids.chat_list.clear_widgets()
            from kivymd.uix.list import OneLineAvatarIconListItem
            sc.ids.chat_list.add_widget(OneLineAvatarIconListItem(text="My Status - Tap to add", on_release=lambda x: setattr(self.root, 'current', 'status_main')))
        elif tab == 'groups':
            sc.ids.fab.icon = "account-group"
            self.load_chats()
        else:
            sc.ids.fab.icon = "phone-plus"
            self.load_chats()

    def load_chats(self):
        if self.current_tab == 'status': return
        from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget
        sc = self.root.get_screen('main')
        sc.ids.chat_list.clear_widgets()
        if self.current_tab == 'chats':
            data = [("AT BRAIN", "AI Secure • online ✓✓", "brain", "Now"), ("Anuj Tripathi", "You: Hello ✓✓ Read", "account-star", "09:45 AM"), ("AT World Mater", "Welcome ✓✓", "earth", "09:15 AM"), ("Poster Studio", "Tap to create poster", "image-edit", "Yesterday"), ("AI Avatar Studio", "Tap to create avatar", "face-recognition", "Yesterday"), ("ADMIN", "See all local chats", "shield-account", "Now")]
        elif self.current_tab == 'groups':
            data = [("AT World Group 🌍", "Anuj: Group call 9 PM", "account-group", "11:00 AM"), ("AT Family Group", "8 members • Group call", "home-group", "10:00 AM")]
        else:
            data = [("Anuj Tripathi", "Outgoing • 9:30 PM ✓✓", "phone-outgoing", "9:30 PM"), ("AT World Group", "Group • 5 members", "account-group", "Yesterday")]
        for title, sub, icon, time in data:
            it = TwoLineAvatarIconListItem(text=f"{title} • {time}", secondary_text=sub, on_release=lambda x, t=title: self.open_chat(t))
            it.add_widget(IconLeftWidget(icon=icon))
            sc.ids.chat_list.add_widget(it)

    def fab_action(self):
        if self.current_tab == 'calls': self.start_call("Anuj Tripathi")
        elif self.current_tab == 'groups': self.root.current = 'groupcall'
        elif self.current_tab == 'status': self.add_status()
        else: self.load_chats()

    def load_status(self):
        from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget
        sc = self.root.get_screen('status_main')
        sc.ids.status_list.clear_widgets()
        statuses = self.store.get("STATUSES")['list'] if self.store.exists("STATUSES") else [("My Status", "Today, 9:00 AM"), ("Anuj Tripathi", "Today, 8:30 AM"), ("AT World Mater", "Today, 7:00 AM")]
        for name, time in statuses:
            it = TwoLineAvatarIconListItem(text=name, secondary_text=time)
            it.add_widget(IconLeftWidget(icon="account-circle"))
            sc.ids.status_list.add_widget(it)

    def add_status(self):
        lst = self.store.get("STATUSES")['list'] if self.store.exists("STATUSES") else []
        lst.insert(0, ("My Status", datetime.now().strftime("Today, %I:%M %p")))
        self.store.put("STATUSES", list=lst)
        self.load_status()
        self.root.current = 'status_main'
        self.test_local_push()

    def open_chat(self, title):
        if title == "Poster Studio": self.root.current = 'poster'; return
        if title == "AI Avatar Studio": self.root.current = 'avatar'; return
        if title == "ADMIN": self.load_admin(); self.root.current = 'admin'; return
        self.current_chat = title
        s = self.root.get_screen('chat')
        s.ids.chat_title.title = title
        s.ids.status_label.text = "online" if "AT" in title else "last seen today, 9:30 PM"
        s.ids.msg_list.clear_widgets()
        def add_msg(t, me=False, tick="✓✓"):
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.label import MDLabel
            from kivymd.uix.button import MDIconButton
            box = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(70), padding=(dp(8), dp(4)), spacing=dp(5), md_bg_color=(0.82, 0.9, 1, 1) if me else (1, 1, 1, 1))
            lbl = MDLabel(text=f"{t} {tick if me else ''}", size_hint_x=.85)
            btn = MDIconButton(icon="dots-vertical", size_hint_x=.15, on_release=lambda x, txt=t: self.show_msg_menu(txt))
            box.add_widget(lbl); box.add_widget(btn)
            s.ids.msg_list.add_widget(box)
        msgs = self.store.get(title)['messages'] if self.store.exists(title) else []
        if msgs:
            for m in msgs: add_msg(m['text'], m['is_me'], m.get('tick', '✓✓'))
        else: add_msg(f"{title} ready! Simple Mode ✅")
        self.root.current = 'chat'

    def show_typing(self, text):
        s = self.root.get_screen('chat')
        s.ids.status_label.text = "typing..." if text else "online"

    def send_message(self):
        s = self.root.get_screen('chat')
        txt = s.ids.msg_input.text.strip()
        if not txt: return
        def add_msg(t, me=False, tick="✓"):
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.label import MDLabel
            box = MDBoxLayout(size_hint_y=None, height=dp(70), padding=(dp(8), dp(4)), md_bg_color=(0.82, 0.9, 1, 1) if me else (1, 1, 1, 1))
            box.add_widget(MDLabel(text=f"{t} {tick if me else ''}"))
            s.ids.msg_list.add_widget(box)
        add_msg(f"You: {txt}", True, "✓")
        Clock.schedule_once(lambda dt: add_msg(f"You: {txt}", True, "✓✓"), 0.5)
        Clock.schedule_once(lambda dt: add_msg(f"You: {txt}", True, "✓✓ Read • Blue"), 1.2)
        reply = f"AT BRAIN 🧠: '{txt}' samajh gaya! Simple AI 🔐" if self.current_chat == "AT BRAIN" else f"{self.current_chat}: {txt} received ✓✓"
        Clock.schedule_once(lambda dt: add_msg(reply, False), 0.8)
        msgs = self.store.get(self.current_chat)['messages'] if self.store.exists(self.current_chat) else []
        msgs.append({"text": f"You: {txt}", "is_me": True, "tick": "✓✓ Read"})
        msgs.append({"text": reply, "is_me": False, "tick": "✓✓"})
        self.store.put(self.current_chat, messages=msgs)
        s.ids.msg_input.text = ""

    def show_msg_menu(self, txt):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton
        def reply(*a): dialog.dismiss(); self.root.get_screen('chat').ids.msg_input.text = f"Reply to {txt}: "
        def delete(*a): dialog.dismiss(); self.delete_message(txt)
        def star(*a): dialog.dismiss(); self.star_message(txt)
        dialog = MDDialog(title=f"Message: {txt[:25]}", buttons=[MDFlatButton(text="Reply", on_release=reply), MDFlatButton(text="⭐ Star", on_release=star), MDFlatButton(text="🗑️ Delete", on_release=delete)])
        dialog.open()

    def delete_message(self, txt):
        if self.store.exists(self.current_chat):
            msgs = self.store.get(self.current_chat)['messages']
            msgs = [m for m in msgs if m['text'] != txt]
            self.store.put(self.current_chat, messages=msgs)
            self.open_chat(self.current_chat)

    def star_message(self, txt):
        starred = self.store.get("STARRED")['list'] if self.store.exists("STARRED") else []
        starred.append({"chat": self.current_chat, "text": txt, "time": str(datetime.now())})
        self.store.put("STARRED", list=starred)

    def start_voice_record(self):
        self.is_recording = True
        self.root.get_screen('chat').ids.status_label.text = "🎤 Recording... slide to cancel"
    def stop_voice_record(self):
        if not self.is_recording: return
        self.is_recording = False
        self.root.get_screen('chat').ids.status_label.text = "online"
        from kivymd.uix.label import MDLabel
        self.root.get_screen('chat').ids.msg_list.add_widget(MDLabel(text=f"🎤 Voice • 0:{random.randint(2,15)} sec • Play ▶️ ✓✓", size_hint_y=None, height=dp(60), md_bg_color=(0.82, 0.9, 1, 1)))

    def share_file(self):
        from kivymd.uix.label import MDLabel
        self.root.get_screen('chat').ids.msg_list.add_widget(MDLabel(text="📎 Photo.jpg shared ✓✓ (Demo)", size_hint_y=None, height=dp(60), md_bg_color=(1, 1, 0.8, 1)))

    def start_call(self, name):
        sc = self.root.get_screen('video')
        sc.ids.video_name.text = f"Calling {name}..."
        sc.ids.agora_status.text = "Demo Voice Call - Real in Next Update"
        self.root.current = 'video'
    def start_video_call(self, name):
        sc = self.root.get_screen('video')
        sc.ids.video_name.text = f"Video Calling {name}..."
        sc.ids.agora_status.text = "Demo Video Call - Real in Next Update"
        self.root.current = 'video'

    def create_poster(self, theme):
        txt = self.root.get_screen('poster').ids.poster_text.text
        sc = self.root.get_screen('poster').ids.poster_preview
        sc.text = f"{txt}\nAT WORLD MATER" if theme == 'blue' else f"🎉 {txt} 🎉\nFestival"
        sc.parent.md_bg_color = (0.06, 0.45, 0.73, 1) if theme == 'blue' else (1, 0.5, 0, 1)
    def save_poster(self): print("Poster Saved"); self.test_local_push()
    def generate_avatar(self, style):
        s = self.root.get_screen('avatar')
        s.ids.avatar_status.text = f"{style} generating..."
        Clock.schedule_once(lambda dt: setattr(s.ids.avatar_status, 'text', f"✅ {style} Avatar Ready! (Demo)"), 1.5)

    def load_admin(self):
        from kivymd.uix.list import TwoLineListItem
        sc = self.root.get_screen('admin')
        sc.ids.admin_list.clear_widgets()
        for key in self.store.keys():
            if key not in ["USER_LOGIN", "ICON_SETTINGS", "BACKUP", "STATUSES", "STARRED"]:
                msgs = self.store.get(key).get('messages', [])
                sc.ids.admin_list.add_widget(TwoLineListItem(text=key, secondary_text=f"{len(msgs)} msgs • {msgs[-1]['text'][:25] if msgs else 'No chat'}"))

ATWorldMatterApp().run()
