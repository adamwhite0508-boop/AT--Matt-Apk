from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty
from datetime import datetime

KV = '''
MDScreenManager:
    SplashScreen:
    ListScreen:
    ChatScreen:
    CallScreen:
    VideoCallScreen:
    GroupCallScreen:
    ContactScreen:
    AdminScreen:
    AvatarScreen:

<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: 'logo.png'
            size_hint: .75, .42
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            text: "AT World Matter"
            halign: "center"
            font_style: "H6"
            bold: True
            text_color: 0.06, 0.45, 0.73, 1
            pos_hint: {'center_y':.32}
        MDLabel:
            text: "Secure • Calls • Groups • AI Avatar"
            halign: "center"
            theme_text_color: "Hint"
            font_size: "13sp"
            pos_hint: {'center_y':.25}

<ListScreen>:
    name: 'list'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AT World Matter"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["menu"]]
            right_action_items: [["video", lambda x: app.root.current == 'list' and setattr(app.root, 'current', 'groupcall')], ["phone", lambda x: setattr(app.root, 'current', 'calls')]]
        ScrollView:
            MDList:
                TwoLineAvatarIconListItem:
                    text: "AT BRAIN - WASM + RAKSHAK"
                    secondary_text: "AI Secure • Tap to chat"
                    on_release: app.open_chat("AT BRAIN")
                    IconLeftWidget:
                        icon: "brain"
                TwoLineAvatarIconListItem:
                    text: "AT World Group 🌍"
                    secondary_text: "12 members • Group Call Active"
                    on_release: app.open_chat("AT World Group")
                    IconLeftWidget:
                        icon: "account-group"
                TwoLineAvatarIconListItem:
                    text: "Poster Studio"
                    secondary_text: "Create poster in Blue-White"
                    on_release: app.open_chat("Poster Studio")
                    IconLeftWidget:
                        icon: "image-edit"
                TwoLineAvatarIconListItem:
                    text: "Anuj Tripathi"
                    secondary_text: "Online • Tap to call/video"
                    on_release: app.open_chat("Anuj Tripathi")
                    IconLeftWidget:
                        icon: "account-star"
                TwoLineAvatarIconListItem:
                    text: "AT Family Group 👨‍👩‍👧‍👦"
                    secondary_text: "8 members • Video group"
                    on_release: app.open_chat("AT Family Group")
                    IconLeftWidget:
                        icon: "home-group"
                TwoLineAvatarIconListItem:
                    text: "Online AT"
                    secondary_text: "typing..."
                    on_release: app.open_chat("Online AT")
                    IconLeftWidget:
                        icon: "account-check"
                TwoLineAvatarIconListItem:
                    text: "🤖 AI Avatar Studio"
                    secondary_text: "Create your AI profile photo"
                    on_release: app.root.current = 'avatar'
                    IconLeftWidget:
                        icon: "face-recognition"
                TwoLineAvatarIconListItem:
                    text: "🔐 ADMIN - All AI Chats"
                    secondary_text: "See all users AI usage"
                    on_release: app.open_admin()
                    IconLeftWidget:
                        icon: "shield-account"
                        theme_icon_color: "Custom"
                        icon_color: 1,0,0,1
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "10dp"
            spacing: "15dp"
            md_bg_color: 1,1,1,1
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
            MDFabButton:
                icon: "contacts"
                md_bg_color: 0.06, 0.45, 0.73, 1
                on_release: app.root.current = 'contacts'

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
                secondary_text: "Today 9:30 PM • 2:15"
                on_release: app.start_call("Anuj Tripathi")
                IconLeftWidget:
                    icon: "phone-outgoing"
            TwoLineAvatarIconListItem:
                text: "AT World Group - Group Call"
                secondary_text: "Yesterday • 5 participants"
                on_release: app.start_group_call("AT World Group")
                IconLeftWidget:
                    icon: "account-group"
            TwoLineAvatarIconListItem:
                text: "AT Family Group - Missed Group"
                secondary_text: "Missed group video"
                on_release: app.start_group_video("AT Family Group")
                IconLeftWidget:
                    icon: "phone-missed"
        Widget:
        MDBoxLayout:
            size_hint_y: None
            height: "90dp"
            padding: "20dp"
            MDFabButton:
                icon: "phone"
                md_bg_color: 0, 0.7, 0.2, 1
                pos_hint: {"center_x":.5}
                on_release: app.start_call("Anuj Tripathi")

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
        MDLabel:
            text: "AT Secure Video • WASM Protected"
            halign: "center"
            text_color: 0.6,0.6,0.6,1
            pos_hint: {'center_y':.27}
        MDBoxLayout:
            size_hint_y: None
            height: "90dp"
            pos_hint: {'center_x':.5,'y':.04}
            spacing: "18dp"
            padding: "20dp"
            MDFabButton:
                icon: "microphone-off"
                md_bg_color: 0.25,0.25,0.25,1
            MDFabButton:
                icon: "phone-hangup"
                md_bg_color: 1,0.2,0.2,1
                on_release: app.end_call()
            MDFabButton:
                icon: "camera-flip"
                md_bg_color: 0.25,0.25,0.25,1
            MDFabButton:
                icon: "video-off"
                md_bg_color: 0.25,0.25,0.25,1

<GroupCallScreen>:
    name: 'groupcall'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Group Calls"
            md_bg_color: 0, 0.6, 0.2, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        MDLabel:
            id: group_title
            text: "AT World Group - Group Call"
            halign: "center"
            font_style: "H6"
            size_hint_y: None
            height: "40dp"
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
                icon: "microphone-off"
                md_bg_color: 0.3,0.3,0.3,1
            MDFabButton:
                icon: "phone-hangup"
                md_bg_color: 1,0.2,0.2,1
                on_release: app.end_call()
            MDFabButton:
                icon: "video-plus"
                md_bg_color: 0, 0.6, 0.2, 1
                on_release: app.add_to_group()
            MDFabButton:
                icon: "account-group"
                md_bg_color: 0.3,0.3,0.3,1

<ContactScreen>:
    name: 'contacts'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Contacts"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'list')]]
        MDList:
            TwoLineAvatarIconListItem:
                text: "Anuj Tripathi - Admin"
                secondary_text: "Owner • AT World Matter"
                on_release: app.open_chat("Anuj Tripathi")
                IconLeftWidget:
                    icon: "account-star"
            TwoLineAvatarIconListItem:
                text: "AT Support Group"
                secondary_text: "12 members"
                on_release: app.start_group_call("AT Support Group")
                IconLeftWidget:
                    icon: "account-group"

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
            size_hint_y: .6
            Image:
                id: avatar_preview
                source: 'icon.png'
                size_hint: .55, .75
                pos_hint: {'center_x':.5,'center_y':.6}
            MDLabel:
                id: avatar_status
                text: "Select photo -> Choose style -> Generate"
                halign: "center"
                pos_hint: {'center_y':.15}
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "10dp"
            spacing: "8dp"
            MDRaisedButton:
                text: "AT Blue"
                md_bg_color: 0.06, 0.45, 0.73, 1
                on_press: app.generate_avatar("blue")
            MDRaisedButton:
                text: "Cartoon"
                md_bg_color: 0.9, 0.5, 0.1, 1
                on_press: app.generate_avatar("cartoon")
            MDRaisedButton:
                text: "Pro"
                md_bg_color: 0.2,0.2,0.2,1
                on_press: app.generate_avatar("pro")
            MDRaisedButton:
                text: "Cyber"
                md_bg_color: 0.5,0.1,0.9,1
                on_press: app.generate_avatar("cyber")
        MDBoxLayout:
            size_hint_y: None
            height: "65dp"
            padding: "12dp"
            spacing: "12dp"
            MDRaisedButton:
                text: "📁 Pick Photo"
                md_bg_color: 0.06, 0.45, 0.73, 1
                size_hint_x: .5
                on_press: app.pick_photo()
            MDRaisedButton:
                text: "✅ Set Profile"
                md_bg_color: 0, 0.7, 0.2, 1
                size_hint_x: .5
                on_press: app.set_profile()
'''

class SplashScreen(MDScreen): pass
class ListScreen(MDScreen): pass
class ChatScreen(MDScreen): pass
class CallScreen(MDScreen): pass
class VideoCallScreen(MDScreen): pass
class GroupCallScreen(MDScreen): pass
class ContactScreen(MDScreen): pass
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
        Clock.schedule_once(lambda x: setattr(self.root, 'current', 'list'), 2.2)

    def open_chat(self, title):
        self.current_chat = title
        s = self.root.get_screen('chat')
        s.ids.chat_title.title = title
        s.ids.msg_list.clear_widgets()
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        def add(t, me=False):
            s.ids.msg_list.add_widget(MDLabel(text=t, size_hint_y=None, height=dp(70), padding=(dp(12), dp(8)), md_bg_color=(0.82,0.9,1,1) if me else (1,1,1,1)))
        if self.store.exists(title):
            for m in self.store.get(title)['messages']:
                add(m['text'], m['is_me'])
        else:
            if "Group" in title:
                add(f"{title} - Group Ready 👥\\n{12 if 'World' in title else 8} members • Group Call & Video enabled")
            else:
                add(f"{title} ready! Chat + Call + Video ✅")
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
        reply = f"AT: {txt} received" if "Group" not in self.current_chat else f"{self.current_chat}: Anuj replied to '{txt}'"
        if self.current_chat == "AT BRAIN":
            reply = f"AT BRAIN 🧠: '{txt}' -> Secure Reply ✅"
        add(reply, False)
        msgs = self.store.get(self.current_chat)['messages'] if self.store.exists(self.current_chat) else []
        msgs.append({"text": f"You: {txt}", "is_me": True, "time": str(datetime.now())})
        msgs.append({"text": reply, "is_me": False, "time": str(datetime.now())})
        self.store.put(self.current_chat, messages=msgs)
        admin = self.store.get("ADMIN_ALL")['logs'] if self.store.exists("ADMIN_ALL") else []
        admin.append({"user_chat": self.current_chat, "user_msg": txt, "ai_reply": reply, "time": str(datetime.now())})
        self.store.put("ADMIN_ALL", logs=admin)
        s.ids.msg_input.text = ""
        Clock.schedule_once(lambda dt: setattr(s.ids.scroll, 'scroll_y', 0), 0.1)

    def start_call(self, name):
        self.current_chat = name
        s = self.root.get_screen('chat')
        from kivymd.uix.label import MDLabel
        from kivy.metrics import dp
        self.open_chat(name)
        s.ids.msg_list.add_widget(MDLabel(text=f"📞 Voice Call to {name} started\\nAT Secure Line • 00:02...", size_hint_y=None, height=dp(70), md_bg_color=(0.8,1,0.8,1)))

    def start_video_call(self, name):
        sc = self.root.get_screen('video')
        sc.ids.video_name.text = f"Video Calling {name}..."
        self.root.current = 'video'

    def start_group_call(self, name):
        sc = self.root.get_screen('groupcall')
        sc.ids.group_title.text = f"{name} - Group Call (4/12 joined)"
        self.root.current = 'groupcall'

    def start_group_video(self, name):
        self.start_group_call(name)

    def add_to_group(self):
        sc = self.root.get_screen('groupcall')
        sc.ids.group_title.text = "Adding member... +1 joined (5/12)"

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
            for log in reversed(self.store.get("ADMIN_ALL")['logs'][-60:]):
                sc.ids.admin_list.add_widget(MDLabel(text=f"[{log['time'][:19]}] {log['user_chat']}\\nU: {log['user_msg']}\\nAI: {log['ai_reply']}", size_hint_y=None, height=dp(90), padding=(dp(10), dp(5)), md_bg_color=(1,0.9,0.9,1)))
        self.root.current = 'admin'

    def pick_photo(self):
        try:
            from plyer import filechooser
            filechooser.open_file(on_selection=self.photo_selected)
        except:
            sc = self.root.get_screen('avatar')
            sc.ids.avatar_status.text = "Gallery (Demo) - Photo selected!"

    def photo_selected(self, sel):
        if sel:
            sc = self.root.get_screen('avatar')
            sc.ids.avatar_preview.source = sel[0]
            self.selected_photo = sel[0]
            sc.ids.avatar_status.text = f"Selected: {sel[0].split('/')[-1]}"

    def generate_avatar(self, style):
        sc = self.root.get_screen('avatar')
        sc.ids.avatar_status.text = f"Generating {style} Avatar..."
        try:
            from PIL import Image, ImageOps, ImageEnhance
            import os
            src = self.selected_photo if hasattr(self, 'selected_photo') and os.path.exists(self.selected_photo) else 'icon.png'
            img = Image.open(src).convert("RGB").resize((512,512))
            if style == "blue":
                bg = Image.new("RGB", (512,512), (15,115,185))
                img = Image.blend(img, bg, 0.3)
            elif style == "cartoon":
                img = ImageOps.posterize(img, 4)
                img = ImageEnhance.Color(img).enhance(1.5)
            elif style == "pro":
                img = ImageOps.grayscale(img).convert("RGB")
                img = ImageEnhance.Contrast(img).enhance(1.4)
            else:
                overlay = Image.new("RGB", (512,512), (0,150,255))
                img = Image.blend(img, overlay, 0.4)
            path = f"AT_Avatar_{style}.png"
            img.save(path)
            sc.ids.avatar_preview.source = path
            sc.ids.avatar_status.text = f"✅ {style} Avatar Ready! {path}"
            self.current_avatar = path
        except Exception as e:
            sc.ids.avatar_status.text = f"✅ {style} Avatar Generated (Demo)"

    def set_profile(self):
        sc = self.root.get_screen('avatar')
        if self.current_avatar:
            self.store.put("USER_PROFILE", avatar=self.current_avatar, time=str(datetime.now()))
            sc.ids.avatar_status.text = f"✅ Profile Set: {self.current_avatar}"
        else:
            sc.ids.avatar_status.text = "Pehle Avatar Generate karo!"

ATWorldMatterApp().run()
