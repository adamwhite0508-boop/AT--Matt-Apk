from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.softinput_mode = "below_target"

KV = '''
<SplashScreen>:
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: 'logo.png'
            size_hint: .8, .4
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            text: "Loading..."
            halign: "center"
            pos_hint: {'center_y':.35}
            theme_text_color: "Hint"

<ChatListScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT World Matter"
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["menu"]]
            right_action_items: [["video", lambda x: setattr(app.root, 'current', 'video')], ["phone", lambda x: setattr(app.root, 'current', 'calls')]]
        ScrollView:
            MDList:
                TwoLineAvatarIconListItem:
                    text: "Anuj Tripathi"
                    secondary_text: "AT World Matter ready hai sir!"
                    on_release: app.open_chat("Anuj Tripathi")
                    IconLeftWidget:
                        icon: "account-circle"
                TwoLineAvatarIconListItem:
                    text: "AT Group"
                    secondary_text: "Welcome to AT World"
                    on_release: app.open_chat("AT Group")
                    IconLeftWidget:
                        icon: "account-group"
        MDFabButton:
            icon: "message"
            pos_hint: {"right":.93,"y":.02}
            md_bg_color: 0.06, 0.45, 0.73, 1
            on_release: app.root.current = 'contacts'

<ChatScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: root.chat_name
            md_bg_color: 0.06, 0.45, 0.73, 1
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'chats')]]
            right_action_items: [["video", lambda x: setattr(app.root, 'current', 'video')], ["phone"]]
        MDLabel:
            text: "Chat secure"
            halign: "center"
            theme_text_color: "Hint"
        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "10dp"
            MDTextField:
                hint_text: "Type message..."
                mode: "round"
            MDIconButton:
                icon: "send"

<CallScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Calls"
            left_action_items: [["arrow-left", lambda x: setattr(app.root,'current','chats')]]
        MDList:
            TwoLineAvatarIconListItem:
                text: "Anuj - Outgoing"
                secondary_text: "Today, 9:30 PM"
                IconLeftWidget:
                    icon: "phone-outgoing"

<VideoCallScreen>:
    MDFloatLayout:
        md_bg_color: 0,0,0,1
        Image:
            source: 'icon.png'
            size_hint: .6, .6
            pos_hint: {'center_x':.5,'center_y':.6}
        MDLabel:
            text: "Video Calling..."
            halign: "center"
            text_color: 1,1,1,1
            pos_hint: {'center_y':.3}
        MDFabButton:
            icon: "phone-hangup"
            md_bg_color: 1,0,0,1
            pos_hint: {'center_x':.5,'y':.05}
            on_release: app.root.current = 'chats'

<ContactScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Contacts"
            left_action_items: [["arrow-left", lambda x: setattr(app.root,'current','chats')]]
        MDList:
            TwoLineAvatarIconListItem:
                text: "Invite Friends"
                IconLeftWidget:
                    icon: "account-plus"
'''

class SplashScreen(MDScreen): pass
class ChatListScreen(MDScreen): pass
class ChatScreen(MDScreen):
    chat_name = StringProperty("Chat")
class CallScreen(MDScreen): pass
class VideoCallScreen(MDScreen): pass
class ContactScreen(MDScreen): pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(ChatListScreen(name='chats'))
        sm.add_widget(ChatScreen(name='chat_view'))
        sm.add_widget(CallScreen(name='calls'))
        sm.add_widget(VideoCallScreen(name='video'))
        sm.add_widget(ContactScreen(name='contacts'))
        return sm
    def on_start(self):
        from kivy.clock import Clock
        Clock.schedule_once(lambda x: setattr(self.root, 'current', 'chats'), 2)
    def open_chat(self, name):
        self.root.get_screen('chat_view').chat_name = name
        self.root.current = 'chat_view'

ATWorldMatterApp().run()
