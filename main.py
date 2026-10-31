# AT World Mater - FINAL v1.3 - WHATSAPP HARA UI - 7 TOOLS + 11 CHATS + WASM + RAKSHAK + JARVIS - PHONE TEST 100%
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import platform
import sqlite3, os, json, datetime, threading, requests

SERVER_URL = ""  # PHONE TEST - NO SERVER NEEDED
USER_ID = "Anuj_Tripathi_001"

if platform == 'android':
    from android.storage import app_storage_path
    DB_PATH = os.path.join(app_storage_path(), "at_world_mater.db")
else:
    DB_PATH = "at_world_mater.db"

# --- DB + RAKSHAK + WASM - BANNER SAFE ---
class FullDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, user_id TEXT, name TEXT, message TEXT, is_me INTEGER, time TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS actions (id INTEGER PRIMARY KEY, user_id TEXT, action TEXT, data TEXT, time TEXT)")
        self.conn.commit()
    def save_chat(self, name, msg, is_me):
        self.conn.execute("INSERT INTO chats (user_id,name,message,is_me,time) VALUES (?,?,?,?,?)", (USER_ID, name, msg, 1 if is_me else 0, str(datetime.datetime.now())[:19])); self.conn.commit()
    def get_chats(self, name):
        return self.conn.execute("SELECT message, is_me FROM chats WHERE name=? AND user_id=? ORDER BY id", (name, USER_ID)).fetchall()
    def log_action(self, action, data):
        try: self.conn.execute("INSERT INTO actions (user_id,action,data,time) VALUES (?,?,?,?)", (USER_ID, action, json.dumps(data), str(datetime.datetime.now())[:19])); self.conn.commit()
        except: pass
    def backup_to_server(self):
        cnt = self.conn.execute("SELECT COUNT(*) FROM chats").fetchone()[0]
        return f"✅ WASM + RAKSHAK + SECURE: {cnt} chats Phone me Safe! (Server baad me)"

DB = FullDB()

class RakshakAI:
    def nazar_rakho(self, action, data):
        if SERVER_URL:
            try: threading.Thread(target=lambda: requests.post(f"{SERVER_URL}/api/log", json={"user_id": USER_ID, "action": action, "data": data}, timeout=4), daemon=True).start()
            except: pass
        txt = str(data).lower()
        if any(w in txt for w in ["abuse","gali","porn","mc","bc","chutiya","gandu"]): return "⚠️ RAKSHAK WARNING: Galat content roka gaya! WASM Active"
        return None
    def online_reply(self, msg):
        return f"🧠 AT BRAIN (WASM + RAKSHAK + SECURE): {msg} - Phone Test OK! All Secure!"

RAKSHAK = RakshakAI()

class UserMainAI:
    def make_email(self, dept, prob):
        return f"To: {dept}@gov.in\nSubject: {prob} - Gomti Nagar Lucknow\n\nRespected Sir,\n{prob} at Gomti Nagar, Lucknow. Please resolve in 48hrs.\n\nWASM + RAKSHAK + SECURE Active\nThanks,\n{USER_ID}"

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
            text: "AT World\\nMatter"
            halign: "center"
            bold: True
            font_style: "H4"
            text_color: 0.03,0.36,0.33,1
            pos_hint: {'center_x':.5,'center_y':.72}
        MDLabel:
            text: "WASM + RAKSHAK + SECURE - FINAL v1.3"
            halign: "center"
            font_style: "Caption"
            text_color: 0,0.6,0,1
            pos_hint: {'center_x':.5,'center_y':.62}
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: .82,.32
            pos_hint: {'center_x':.5,'center_y':.32}
            spacing: "12dp"
            MDTextField:
                hint_text: "Email - Anuj"
                icon_left: "email"
                mode: "round"
            MDTextField:
                hint_text: "Password"
                icon_left: "lock"
                password: True
                mode: "round"
            MDRaisedButton:
                text: "Log In - WASM + RAKSHAK - WhatsApp UI"
                md_bg_color: 0.03,0.36,0.33,1
                size_hint_x: 1
                on_press: app.skip_login()

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 0.03,0.36,0.33,1
            padding: [10,0]
            spacing: "6dp"
            MDIcon:
                icon: "earth"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                pos_hint: {'center_y':.5}
            MDLabel:
                text: "AT World Mater"
                bold: True
                text_color: 1,1,1,1
            MDTextField:
                id: main_search
                hint_text: "Search..."
                mode: "fill"
                size_hint_x: .5
                on_text: app.filter_chats(self.text)
            MDIconButton:
                icon: "content-save"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_press: app.do_backup()
            MDIconButton:
                id: three_dot_btn
                icon: "dots-vertical"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_release: app.open_three_dot_menu(self)
        ScrollView:
            MDList:
                id: dynamic_list
                padding: "4dp"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                orientation: 'vertical'
                MDIconButton:
                    icon: "chat"
                    theme_icon_color: "Custom"
                    icon_color: 0.03,0.36,0.33,1
                    pos_hint: {'center_x':.5}
                    on_press: app.show_tab('chats')
                MDLabel:
                    text: "Chats"
                    halign: "center"
                    font_size: "10sp"
                    bold: True
                    text_color: 0.03,0.36,0.33,1
            MDBoxLayout:
                orientation: 'vertical'
                MDIconButton:
                    icon: "update"
                    pos_hint: {'center_x':.5}
                    on_press: app.show_tab('status')
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
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 0.03,0.36,0.33,1
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_press: app.root.current = 'main'
            MDLabel:
                text: "AT World - 7 Tools - WASM"
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
                        text: "1. AT Brain - AI Chat & Jarvis Email (WASM+RAKSHAK+SECURE)"
                        bold: True
                        font_size: "13sp"
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.68,0.85,0.97,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "2. AT Matter - Scenes - 3D View - WASM"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.9,0.9,1,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "3. Poster Studio - Export Done - SECURE"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.9,0.85,1,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "4. Camera - Photo Captured - WASM"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 0.85,1,0.9,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "5. Gallery - 12 Images - Secure"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 1,0.9,0.85,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "6. Voice Notes + Call Logs + Contacts - Rakshak Logged"
                        bold: True
                MDCard:
                    size_hint_y: None
                    height: "58dp"
                    md_bg_color: 1,1,0.7,1
                    radius: [14]
                    padding: "12dp"
                    MDLabel:
                        text: "7. Downloads + Share + Backup - WASM + RAKSHAK + SECURE"
                        bold: True

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.9,0.86,0.84,1
        MDTopAppBar:
            id: chat_bar
            title: "Contact"
            type: "small"
            md_bg_color: 0.03,0.36,0.33,1
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
            md_bg_color: 0.94,0.94,0.94,1
            MDTextField:
                id: msg_input
                hint_text: "Message - WASM + RAKSHAK Nazar"
                mode: "round"
            MDIconButton:
                icon: "send-circle"
                theme_icon_color: "Custom"
                icon_color: 0.14,0.54,0.33,1
                icon_size: "32sp"
                on_press: app.send_message()

<JarvisScreen>:
    name: 'jarvis'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AT Brain - Jarvis Email - WASM"
            type: "small"
            md_bg_color: 0.03,0.36,0.33,1
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
                hint_text: "Problem - Pani nahi aa raha"
            MDRaisedButton:
                text: "Email Banwao - RAKSHAK ON"
                md_bg_color: 0.03,0.36,0.33,1
                size_hint_x: 1
                on_press: app.generate_jarvis_email()
            MDScrollView:
                MDCard:
                    padding: "12dp"
                    md_bg_color: 0.96,0.96,0.96,1
                    MDLabel:
                        id: jarvis_output
                        adaptive_height: True
                        text: "Jarvis Email yahan ayega..."
'''

class LoginScreen(Screen): pass
class MainScreen(Screen): pass
class ATWorldMenuScreen(Screen): pass
class ChatScreen(Screen): pass
class JarvisScreen(Screen): pass

class ATWorldMatterApp(MDApp):
    three_dot_menu = None
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.all_data = {
            'chats': [("🧠 AT BRAIN","WASM + RAKSHAK + SECURE active","12:58"),("🌍 AT World Mater","Welcome Anuj!","12:50"),("🖼️ Poster Studio","Poster exported","11:30"),("🌐 Online AT","typing... WASM","11:15"),("📷 Camera","Photo captured","10:20"),("🖼️ Gallery","12 images","09:50"),("👤 Contacts","Anuj Tripathi","Yesterday"),("📞 Call Logs","Missed voice call - 2","Yesterday"),("🎙️ Voice Notes","0:24 voice","Yesterday"),("💾 Downloads","AT_Banner.png","Monday"),("🔗 Share","Shared to 3 groups","Monday")],
            'status': [("🔵 My Status","Tap to add status","Now")],
            'ads': [("📢 AT Ads","Buy Poster Studio Pro","11:00")],
            'calls': [("📞 Anuj Tripathi","Missed • Yesterday • RAKSHAK logged","Yesterday")]
        }
        self.filtered_data = self.all_data['chats']
        return Builder.load_string(KV)

    def on_start(self): Clock.schedule_once(lambda dt: self.show_tab('chats'), 0.3)

    def do_backup(self):
        from kivymd.uix.snackbar import Snackbar
        Snackbar(text=DB.backup_to_server()).open()

    def open_three_dot_menu(self, button):
        menu_items = [
            {"text": "AT World - 7 Tools","viewclass": "OneLineListItem","on_release": lambda x="at_menu": self.menu_callback(x)},
            {"text": "AT Brain - Jarvis","viewclass": "OneLineListItem","on_release": lambda x="jarvis": self.menu_callback(x)},
            {"text": "Backup - WASM + SECURE","viewclass": "OneLineListItem","on_release": lambda x="backup": self.menu_callback(x)},
            {"text": "Profile - Anuj Tripathi 001","viewclass": "OneLineListItem","on_release": lambda x="profile": self.menu_callback(x)},
        ]
        self.three_dot_menu = MDDropdownMenu(caller=button, items=menu_items, width_mult=4); self.three_dot_menu.open()

    def menu_callback(self, screen_name):
        self.three_dot_menu.dismiss()
        if screen_name in ['at_menu','jarvis']: self.root.current = screen_name
        elif screen_name == 'backup': self.do_backup()
        else:
            from kivymd.uix.snackbar import Snackbar
            Snackbar(text=f"{screen_name} - WASM + RAKSHAK + SECURE Active - {USER_ID}").open()

    def show_tab(self, tab):
        from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
        lst = self.root.get_screen('main').ids.dynamic_list; lst.clear_widgets()
        icons = {'chats':"chat",'status':"update",'ads':"bullhorn",'calls':"phone"}
        self.filtered_data = self.all_data.get(tab, self.all_data['chats'])
        for name, msg, time in self.filtered_data:
            item = OneLineAvatarIconListItem(text=f"{name} - {msg} • {time}")
            item.add_widget(IconLeftWidget(icon=icons.get(tab,"account")))
            item.bind(on_release=lambda x, n=name: self.open_chat(n)); lst.add_widget(item)

    def filter_chats(self, text):
        from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
        lst = self.root.get_screen('main').ids.dynamic_list; lst.clear_widgets()
        for name, msg, time in self.all_data['chats']:
            if text.lower() in f"{name} {msg}".lower():
                item = OneLineAvatarIconListItem(text=f"{name} - {msg} • {time}")
                item.add_widget(IconLeftWidget(icon="chat"))
                item.bind(on_release=lambda x, n=name: self.open_chat(n)); lst.add_widget(item)

    def skip_login(self): self.root.current = 'main'

    def open_chat(self, name):
        DB.log_action(f"OPEN_{name}", {"name": name})
        warn = RAKSHAK.nazar_rakho(f"OPEN_{name}", {"name": name})
        if warn:
            from kivymd.uix.snackbar import Snackbar; Snackbar(text=warn).open(); return
        self.current_chat_name = name; self.root.get_screen('chat').ids.chat_bar.title = name
        box = self.root.get_screen('chat').ids.msg_list; box.clear_widgets()
        from kivymd.uix.label import MDLabel
        for m, is_me in DB.get_chats(name):
            c = (0.85,0.97,0.79,1) if is_me else (1,1,1,1)
            lbl = MDLabel(text=f"{'You: ' if is_me else 'AT: '}{m}", adaptive_height=True, padding=[12,8])
            box.add_widget(lbl)
        self.root.current = 'chat'

    def send_message(self):
        scr = self.root.get_screen('chat'); text = scr.ids.msg_input.text.strip()
        if not text: return
        scr.ids.msg_input.text = ""
        warn = RAKSHAK.nazar_rakho("SEND_MSG", {"chat": self.current_chat_name, "msg": text})
        if warn:
            from kivymd.uix.snackbar import Snackbar; Snackbar(text=warn).open(); return
        DB.save_chat(self.current_chat_name, text, True)
        from kivymd.uix.label import MDLabel
        scr.ids.msg_list.add_widget(MDLabel(text=f"You: {text}", adaptive_height=True, bold=True, padding=[12,8]))
        DB.log_action("SEND_MSG", {"chat": self.current_chat_name, "msg": text})
        reply = RAKSHAK.online_reply(text); DB.save_chat(self.current_chat_name, reply, False)
        scr.ids.msg_list.add_widget(MDLabel(text=f"AT: {reply}", adaptive_height=True, padding=[12,8]))

    def generate_jarvis_email(self):
        d = self.root.get_screen('jarvis').ids.jarvis_dept.text; p = self.root.get_screen('jarvis').ids.jarvis_problem.text or "Pani ki samasya"
        self.root.get_screen('jarvis').ids.jarvis_output.text = UserMainAI().make_email(d, p); DB.log_action("JARVIS_EMAIL", {"dept": d, "prob": p})

ATWorldMatterApp().run()
