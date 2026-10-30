from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty
from kivy.clock import Clock
from datetime import datetime

KV = '''
MDScreenManager:
    SplashScreen:
    ListScreen:
    ChatScreen:
    CallScreen:
    VideoCallScreen:
    GroupCallScreen:
    AdminScreen:
    AvatarScreen:

<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: 'banner.png'
            size_hint: .85, .55
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            text: "AT World Matter"
            halign: "center"
            font_style: "H6"
            bold: True
            text_color: 0.06, 0.45, 0.73, 1
            pos_hint: {'center_y':.28}

<ListScreen>:
    name: 'list'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AT World Mater"
            md_bg_color: 0.06, 0.45, 0.73, 1
            right_action_items: [["video", lambda x: setattr(app.root, 'current', 'groupcall')], ["phone", lambda x: setattr(app.root, 'current', 'calls')]]
        ScrollView:
            MDList:
                TwoLineAvatarIconListItem:
                    text: "AT BRAIN - WASM + RAKSHAK"
                    secondary_text: "AI Secure Active"
                    on_release: app.open_chat("AT BRAIN")
                    IconLeftWidget:
                        icon: "brain"
                TwoLineAvatarIconListItem:
                    text: "AT World Group 🌍"
                    secondary_text: "12 members • Group Call"
                    on_release: app.open_chat("AT World Group")
                    IconLeftWidget:
                        icon: "account-group"
                TwoLineAvatarIconListItem:
                    text: "Anuj Tripathi"
                    secondary_text: "Owner • Call / Video"
                    on_release: app.open_chat("Anuj Tripathi")
                    IconLeftWidget:
                        icon: "account-star"
                TwoLineAvatarIconListItem:
                    text: "Poster Studio"
                    secondary_text: "Create poster"
                    on_release: app.open_chat("Poster Studio")
                    IconLeftWidget:
                        icon: "image-edit"
                TwoLineAvatarIconListItem:
                    text: "🤖 AI Avatar Studio"
                    secondary_text: "Create AI profile photo"
                    on_release: app.root.current = 'avatar'
                    IconLeftWidget:
                        icon: "face-recognition"
                TwoLineAvatarIconListItem:
                    text: "🔐 ADMIN - All AI Chats"
                    secondary_text: "See users AI usage"
                    on_release: app.open_admin()
                    IconLeftWidget:
                        icon: "shield-account"
        MDBoxLayout:
            size_hint_y: None
            height: "62dp"
            padding: "10dp"
            spacing: "15dp"
            MDFabButton:
                icon: "phone"
                md_bg_color: 0.06, 0.45, 0.73, 1
                on_release: app.root.current = 'calls'
            MDFabButton:
                icon: "video"
                md_bg_color: 0.06, 0.45, 0.73, 1
                on_release: app.start_video_call("AT World Group")
            MDFabButton:
                icon: "account-group"
                md_bg_color: 0, 0.6, 0.2, 1
                on_release: app.root.current = 'groupcall'

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.96, 0.97, 1, 1
        MDTopAppBar:
            id: chat_title
            title: "Chat"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
            right_action_items: [["video", lambda x: app.start_video_call(app.current_chat)], ["phone", lambda x: app.start_call(app.current_chat)], ["account-group", lambda x: app.start_group_call(app.current_chat)]]
        ScrollView:
            id: scroll
            MDList:
                id: msg_list
                padding: "10dp"
                spacing: "8dp"
        MDBoxLayout:
            size_hint_y: None
            height: "62dp"
            padding: "6dp"
            spacing: "6dp"
            md_bg_color: 1,1,1,1
            MDTextField:
                id: msg_input
                hint_text: "Message"
                mode: "round"
            MDIconButton:
                icon: "send"
                md_bg_color: 0.06, 0.45, 0.73, 1
                icon_color: 1,1,1,1
                on_press: app.send_message()

<CallScreen>:
    name: 'calls'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Calls"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        MDList:
            TwoLineAvatarIconListItem:
                text: "Anuj Tripathi - Outgoing"
                secondary_text: "Today 9:30 PM"
                on_release: app.start_call("Anuj Tripathi")
                IconLeftWidget:
                    icon: "phone-outgoing"
            TwoLineAvatarIconListItem:
                text: "AT World Group - Group Call"
                secondary_text: "5 participants"
                on_release: app.start_group_call("AT World Group")
                IconLeftWidget:
                    icon: "account-group"
        Widget:

<VideoCallScreen>:
    name: 'video'
    MDFloatLayout:
        md_bg_color: 0.05, 0.05, 0.08, 1
        Image:
            source: 'icon.png'
            size_hint: .45, .45
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            id: video_name
            text: "Calling..."
            halign: "center"
            text_color: 1,1,1,1
            font_style: "H6"
            pos_hint: {'center_y':.32}
        MDBoxLayout:
            size_hint_y: None
            height: "90dp"
            pos_hint: {'center_x':.5,'y':.05}
            spacing: "18dp"
            padding: "20dp"
            MDFabButton:
                icon: "phone-hangup"
                md_bg_color: 1,0.2,0.2,1
                on_release: app.end_call()

<GroupCallScreen>:
    name: 'groupcall'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Group Calls"
            md_bg_color: 0, 0.6, 0.2, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        MDGridLayout:
            cols: 2
            spacing: "5dp"
            padding: "5dp"
            MDCard:
                md_bg_color: 0.1,0.1,0.1,1
                MDLabel:
                    text: "Anuj\\n🎙️"
                    halign: "center"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.1,0.1,0.1,1
                MDLabel:
                    text: "You\\n🎥"
                    halign: "center"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.15,0.15,0.15,1
                MDLabel:
                    text: "AT Support\\n🔇"
                    halign: "center"
                    text_color: 1,1,1,1
            MDCard:
                md_bg_color: 0.15,0.15,0.15,1
                MDLabel:
                    text: "+9 more\\n👥"
                    halign: "center"
                    text_color: 1,1,1,1
        MDBoxLayout:
            size_hint_y: None
            height: "90dp"
            padding: "15dp"
            spacing: "15dp"
            MDFabButton:
                icon: "phone-hangup"
                md_bg_color: 1,0.2,0.2,1
                on_release: app.end_call()
            MDFabButton:
                icon: "account-group"
                md_bg_color: 0, 0.6, 0.2, 1
                on_release: app.add_to_group()

<AdminScreen>:
    name: 'admin'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "ADMIN - All AI Chats"
            md_bg_color: 1,0,0,1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        ScrollView:
            MDList:
                id: admin_list

<AvatarScreen>:
    name: 'avatar'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AI Avatar Studio"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        MDFloatLayout:
            size_hint_y: .65
            Image:
                id: avatar_preview
                source: 'icon.png'
                size_hint: .55, .75
                pos_hint: {'center_x':.5,'center_y':.6}
            MDLabel:
                id: avatar_status
                text: "Pick photo -> Choose style"
                halign: "center"
                pos_hint: {'center_y':.15}
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "10dp"
            spacing: "8dp"
            MDRaisedButton:
                text: "AT Blue"
                on_press: app.generate_avatar("blue")
            MDRaisedButton:
                text: "Cartoon"
                on_press: app.generate_avatar("cartoon")
            MDRaisedButton:
                text: "Pro"
                on_press: app.generate_avatar("pro")
            MDRaisedButton:
                text: "Cyber"
                on_press: app.generate_avatar("cyber")
        MDBoxLayout:
            size_hint_y: None
            height: "65dp"
            padding: "12dp"
            spacing: "12dp"
            MDRaisedButton:
                text: "📁 Pick Photo"
                size_hint_x: .5
                on_press: app.pick_photo()
            MDRaisedButton:
                text: "✅ Set Profile"
                md_bg_color: 0, 0.7, 0.2, 1
                size_hint_x: .5
                on_press: app.set_profile()
'''

from kivymd.uix.screen import MDScreen
class SplashScreen(MDScreen): pass
class ListScreen(MDScreen): pass
class ChatScreen(MDScreen): pass
class CallScreen(MDScreen): pass
class VideoCallScreen(MDScreen): pass
class GroupCallScreen(MDScreen): pass
class AdminScreen(MDScreen): pass
class AvatarScreen(MDScreen): pass

class ATWorldMatterApp(MDApp):
    current_chat = StringProperty("")
    selected_photo = StringProperty("icon.png")
    current_avatar = StringProperty("")
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.store = JsonStore("at_chats.json")
        return Builder.load_string(KV)
    def on_start(self):
        Clock.schedule_once(lambda x: setattr(self.root, 'current', 'list'), 1.8)
    def open_chat(self, title):
        self.current_chat = title
        s = self.root.get_screen('chat')
        s.ids.chat_title.title = title
        s.ids.msg_list.clear_widgets()
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        def add(t, me=False):
            s.ids.msg_list.add_widget(MDLabel(text=t, size_hint_y=None, height=dp(70), padding=(dp(12), dp(8)), md_bg_color=(0.82,0.9,1,1) if me else (1,1,1,1)))
        msgs = self.store.get(title)['messages'] if self.store.exists(title) else []
        if msgs:
            for m in msgs: add(m['text'], m['is_me'])
        else:
            add(f"{title} ready! Chat+Call+Video+Group ✅")
        self.root.current = 'chat'
    def send_message(self):
        s = self.root.get_screen('chat')
        txt = s.ids.msg_input.text.strip()
        if not txt: return
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        def add(t, me=False):
            s.ids.msg_list.add_widget(MDLabel(text=t, size_hint_y=None, height=dp(65), padding=(dp(12), dp(8)), md_bg_color=(0.82,0.9,1,1) if me else (1,1,1,1)))
        add(f"You: {txt}", True)
        reply = f"AT BRAIN: '{txt}' -> Secure Reply ✅" if self.current_chat=="AT BRAIN" else f"{self.current_chat}: {txt} received"
        add(reply, False)
        msgs = self.store.get(self.current_chat)['messages'] if self.store.exists(self.current_chat) else []
        msgs.append({"text": f"You: {txt}", "is_me": True}); msgs.append({"text": reply, "is_me": False})
        self.store.put(self.current_chat, messages=msgs)
        admin = self.store.get("ADMIN_ALL")['logs'] if self.store.exists("ADMIN_ALL") else []
        admin.append({"user_chat": self.current_chat, "user_msg": txt, "ai_reply": reply, "time": str(datetime.now())})
        self.store.put("ADMIN_ALL", logs=admin)
        s.ids.msg_input.text = ""
    def start_call(self, name):
        self.open_chat(name)
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        self.root.get_screen('chat').ids.msg_list.add_widget(MDLabel(text=f"📞 Voice Call to {name} started\\nSecure Line", size_hint_y=None, height=dp(70), md_bg_color=(0.8,1,0.8,1)))
    def start_video_call(self, name):
        self.root.get_screen('video').ids.video_name.text = f"Video Calling {name}..."
        self.root.current = 'video'
    def start_group_call(self, name):
        self.root.current = 'groupcall'
    def add_to_group(self): pass
    def end_call(self):
        self.root.current = 'list'
    def open_admin(self):
        sc = self.root.get_screen('admin')
        sc.ids.admin_list.clear_widgets()
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        if not self.store.exists("ADMIN_ALL"):
            sc.ids.admin_list.add_widget(MDLabel(text="No AI usage yet!", size_hint_y=None, height=dp(50)))
        else:
            for log in reversed(self.store.get("ADMIN_ALL")['logs'][-50:]):
                sc.ids.admin_list.add_widget(MDLabel(text=f"[{log['time'][:19]}] {log['user_chat']}\\n{log['user_msg']}", size_hint_y=None, height=dp(80)))
        self.root.current = 'admin'
    def pick_photo(self):
        sc = self.root.get_screen('avatar')
        sc.ids.avatar_status.text = "Photo selected (Demo)!"
    def generate_avatar(self, style):
        sc = self.root.get_screen('avatar')
        sc.ids.avatar_status.text = f"✅ {style} Avatar Generated!"
        try:
            from PIL import Image, ImageOps, ImageEnhance
            import os
            src = 'icon.png'
            img = Image.open(src).convert("RGB").resize((512,512))
            if style=="blue":
                bg = Image.new("RGB", (512,512), (15,115,185))
                img = Image.blend(img, bg, 0.3)
            img.save(f"AT_Avatar_{style}.png")
            sc.ids.avatar_preview.source = f"AT_Avatar_{style}.png"
            self.current_avatar = f"AT_Avatar_{style}.png"
        except:
            self.current_avatar = "icon.png"
    def set_profile(self):
        sc = self.root.get_screen('avatar')
        sc.ids.avatar_status.text = "✅ Profile Set!"

ATWorldMatterApp().run()
