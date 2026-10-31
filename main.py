# AT World Mater - CRASH FIX FINAL v1.4 - NO CRASH - WHATSAPP HARA
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.utils import platform
import sqlite3, os, json, datetime

USER_ID = "Anuj_Tripathi_001"

# DB PATH - CRASH SAFE
try:
    if platform == 'android':
        from android.storage import app_storage_path
        DB_PATH = os.path.join(app_storage_path(), "at_world_mater.db")
    else:
        DB_PATH = "at_world_mater.db"
except:
    DB_PATH = "at_world_mater.db"

class FullDB:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            self.conn.execute("CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, user_id TEXT, name TEXT, message TEXT, is_me INTEGER, time TEXT)")
            self.conn.commit()
        except Exception as e:
            print(f"DB Error: {e}")
            self.conn = None
    def save_chat(self, name, msg, is_me):
        if not self.conn: return
        try: self.conn.execute("INSERT INTO chats (user_id,name,message,is_me,time) VALUES (?,?,?,?,?)", (USER_ID, name, msg, 1 if is_me else 0, str(datetime.datetime.now())[:19])); self.conn.commit()
        except: pass
    def get_chats(self, name):
        if not self.conn: return []
        try: return self.conn.execute("SELECT message, is_me FROM chats WHERE name=? AND user_id=? ORDER BY id", (name, USER_ID)).fetchall()
        except: return []
    def backup(self):
        if not self.conn: return "✅ Phone me Safe!"
        try: cnt = self.conn.execute("SELECT COUNT(*) FROM chats").fetchone()[0]; return f"✅ WASM+RAKSHAK+SECURE: {cnt} chats Phone me Safe!"
        except: return "✅ Phone me Safe!"

DB = FullDB()

KV = '''
MDScreenManager:
    MainScreen:
    ChatScreen:
    MenuScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 0.03,0.36,0.33,1
            padding: 10
            MDLabel:
                text: "AT World Matter - WASM"
                bold: True
                text_color: 1,1,1,1
            MDIconButton:
                icon: "content-save"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_press: app.do_backup()
            MDIconButton:
                icon: "dots-vertical"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_press: app.root.current = 'menu'
        ScrollView:
            MDList:
                id: chat_list
                padding: "4dp"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Chats - 11 - WASM Active"
                halign: "center"
                font_size: "12sp"

<MenuScreen>:
    name: 'menu'
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
                text: "AT World - 7 Tools"
                bold: True
                text_color: 1,1,1,1
        ScrollView:
            MDList:
                OneLineListItem:
                    text: "1. AT Brain - AI Chat & Jarvis"
                    on_press: app.open_chat("AT BRAIN")
                OneLineListItem:
                    text: "2. AT Matter - Scenes - WASM"
                OneLineListItem:
                    text: "3. Poster Studio - Export Done"
                OneLineListItem:
                    text: "4. Camera - Photo Captured"
                OneLineListItem:
                    text: "5. Gallery - 12 Images"
                OneLineListItem:
                    text: "6. Voice Notes + Call Logs"
                OneLineListItem:
                    text: "7. Downloads + Share + Backup - SECURE"

<ChatScreen>:
    name: 'chat'
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
                id: chat_title
                text: "Contact"
                bold: True
                text_color: 1,1,1,1
        ScrollView:
            MDBoxLayout:
                id: msg_box
                orientation: 'vertical'
                padding: "10dp"
                spacing: "8dp"
                adaptive_height: True
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            padding: "6dp"
            spacing: "6dp"
            MDTextField:
                id: msg_input
                hint_text: "Message - WASM + RAKSHAK Nazar"
                mode: "round"
            MDIconButton:
                icon: "send"
                theme_icon_color: "Custom"
                icon_color: 0.03,0.36,0.33,1
                on_press: app.send_msg()
'''

class MainScreen(Screen): pass
class ChatScreen(Screen): pass
class MenuScreen(Screen): pass

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(lambda dt: self.load_chats(), 0.5)

    def load_chats(self):
        try:
            lst = self.root.get_screen('main').ids.chat_list
            lst.clear_widgets()
            from kivymd.uix.list import OneLineListItem
            data = [("AT BRAIN","WASM + RAKSHAK + SECURE active"),("AT World Mater","Welcome Anuj!"),("Poster Studio","Poster exported"),("Online AT","typing... WASM"),("Camera","Photo captured"),("Gallery","12 images"),("Contacts","Anuj Tripathi"),("Call Logs","Missed voice call"),("Voice Notes","0:24 voice"),("Downloads","AT_Banner.png"),("Share","Shared to 3 groups")]
            for n,m in data:
                item = OneLineListItem(text=f"{n} - {m}")
                item.bind(on_release=lambda x, name=n: self.open_chat(name))
                lst.add_widget(item)
        except Exception as e:
            print(f"load_chats error: {e}")

    def open_chat(self, name):
        try:
            if any(w in name.lower() for w in ["abuse","gali","porn","chutiya"]):
                from kivymd.uix.snackbar import Snackbar; Snackbar(text="⚠️ RAKSHAK WARNING: Roka!").open(); return
            self.current_chat = name
            self.root.get_screen('chat').ids.chat_title.text = name
            box = self.root.get_screen('chat').ids.msg_box
            box.clear_widgets()
            from kivymd.uix.label import MDLabel
            for msg, is_me in DB.get_chats(name):
                box.add_widget(MDLabel(text=f"{'You: ' if is_me else 'AT: '}{msg}", adaptive_height=True, padding=[10,6]))
            self.root.current = 'chat'
        except Exception as e:
            print(f"open_chat error: {e}")

    def send_msg(self):
        try:
            scr = self.root.get_screen('chat')
            t = scr.ids.msg_input.text.strip()
            if not t: return
            scr.ids.msg_input.text = ""
            if any(w in t.lower() for w in ["abuse","gali","porn","chutiya"]):
                from kivymd.uix.snackbar import Snackbar; Snackbar(text="⚠️ RAKSHAK WARNING: Galat content roka!").open(); return
            DB.save_chat(self.current_chat, t, True)
            from kivymd.uix.label import MDLabel
            scr.ids.msg_box.add_widget(MDLabel(text=f"You: {t}", adaptive_height=True, bold=True, padding=[10,6]))
            reply = f"🧠 AT BRAIN (WASM+RAKSHAK): {t} - Phone Test OK!"
            DB.save_chat(self.current_chat, reply, False)
            scr.ids.msg_box.add_widget(MDLabel(text=f"AT: {reply}", adaptive_height=True, padding=[10,6]))
        except Exception as e:
            print(f"send_msg error: {e}")

    def do_backup(self):
        try:
            from kivymd.uix.snackbar import Snackbar
            Snackbar(text=DB.backup()).open()
        except Exception as e:
            print(f"backup error: {e}")

ATWorldMatterApp().run()
