# AT World Mater - FINAL - WHATSAPP CLONE + RAKSHAK - PHONE TEST
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex, platform
from kivy.graphics import Color, Rectangle, Ellipse, RoundedRectangle
import sqlite3, os, json, datetime, threading, requests

Window.clearcolor = get_color_from_hex("#FFFFFF")

SERVER_URL = ""  # PHONE TEST KE LIYE KHALI - SERVER NAHI CHAHIYE
USER_ID = "Anuj_Tripathi_001"

if platform == 'android':
    from android.storage import app_storage_path
    DB_PATH = os.path.join(app_storage_path(), "at_world_mater.db")
else:
    DB_PATH = "at_world_mater.db"

class FullDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, user_id TEXT, name TEXT, message TEXT, is_me INTEGER, time TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS actions (id INTEGER PRIMARY KEY, user_id TEXT, action TEXT, data TEXT, time TEXT)")
    def save_chat(self, name, msg, is_me):
        self.conn.execute("INSERT INTO chats (user_id,name,message,is_me,time) VALUES (?,?,?,?,?)", (USER_ID, name, msg, 1 if is_me else 0, str(datetime.datetime.now())[:19]))
        self.conn.commit()
    def get_chats(self, name):
        cur = self.conn.execute("SELECT message, is_me FROM chats WHERE name=? AND user_id=? ORDER BY id", (name, USER_ID))
        return cur.fetchall()
    def log_action(self, action, data):
        self.conn.execute("INSERT INTO actions (user_id,action,data,time) VALUES (?,?,?,?)", (USER_ID, action, json.dumps(data), str(datetime.datetime.now())[:19]))
        self.conn.commit()
    def backup_to_server(self):
        if not SERVER_URL:
            return "✅ Phone me save ho gaya! (Server baad me)"
        try:
            all_chats = self.conn.execute("SELECT * FROM chats").fetchall()
            threading.Thread(target=lambda: requests.post(f"{SERVER_URL}/api/backup", json={"user_id": USER_ID, "chats": str(all_chats)}, timeout=5)).start()
            return f"✅ {len(all_chats)} chats SERVER pe backup!"
        except Exception as e:
            return f"Backup fail: {e}"

DB = FullDB()

class RakshakAI:
    def nazar_rakho(self, action, data):
        if not SERVER_URL:
            return None
        def send_online():
            try:
                requests.post(f"{SERVER_URL}/api/log", json={"user_id": USER_ID, "action": action, "data": data}, timeout=4)
            except:
                pass
        threading.Thread(target=send_online).start()
        txt = str(data).lower()
        if "abuse" in txt or "gali" in txt or "porn" in txt:
            return "⚠️ RAKSHAK WARNING: Galat content roka gaya!"
        return None
    def online_reply(self, msg):
        if SERVER_URL:
            try:
                r = requests.post(f"{SERVER_URL}/api/chat", json={"msg": msg, "user_id": USER_ID}, timeout=5)
                if r.status_code == 200:
                    return r.json().get("reply", f"🧠 AT BRAIN: {msg}")
            except:
                pass
        return f"🧠 AT BRAIN (Offline): {msg}\nWASM + RAKSHAK + SECURE Active - Phone Test OK!"

RAKSHAK = RakshakAI()

def show_warning(text):
    Popup(title='AT RAKSHAK', content=Label(text=text, text_size=(dp(280),None)), size_hint=(0.85,0.35)).open()

class ChatRow(BoxLayout):
    def __init__(self, icon, name, msg, time, unread=0, on_press=None, **kw):
        super().__init__(orientation='horizontal', size_hint_y=None, height=dp(72), padding=[dp(12),dp(6)], spacing=dp(12), **kw)
        self.on_press = on_press
        av = BoxLayout(size_hint_x=None, width=dp(50))
        with av.canvas.before:
            Color(rgba=get_color_from_hex("#DFE5E7"))
            self.ell = Ellipse(size=(dp(50),dp(50)), pos=(av.x, av.y+dp(6)))
        av.bind(pos=lambda i,v: setattr(self.ell, 'pos', (v[0], v[1]+dp(6))))
        av.add_widget(Label(text=icon, font_size=dp(22)))
        self.add_widget(av)
        mid = BoxLayout(orientation='vertical')
        mid.add_widget(Label(text=name, bold=True, color=(0,0,0,1), halign='left', font_size=dp(15), text_size=(dp(180),None), size_hint_y=0.6))
        mid.add_widget(Label(text=msg, color=(0.5,0.5,0.5,1), halign='left', font_size=dp(12), text_size=(dp(180),None), size_hint_y=0.4))
        self.add_widget(mid)
        self.add_widget(Label(text=time, color=get_color_from_hex("#25D366") if unread else get_color_from_hex("#666666"), font_size=dp(11), size_hint_x=None, width=dp(50)))
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.on_press:
            self.on_press()
            return True
        return super().on_touch_down(touch)

class MainScreen(Screen):
    def __init__(self, sm, **kw):
        super().__init__(**kw)
        self.sm = sm
        root = BoxLayout(orientation='vertical')
        h = BoxLayout(size_hint_y=None, height=dp(56), padding=[dp(12),0,dp(5),0])
        with h.canvas.before:
            Color(rgba=get_color_from_hex("#075E54"))
            h.bg = Rectangle(pos=h.pos, size=h.size)
        h.bind(pos=lambda i,v: setattr(i.bg, 'pos', v), size=lambda i,v: setattr(i.bg, 'size', v))
        h.add_widget(Label(text="AT World Mater", bold=True, color=(1,1,1,1), font_size=dp(18), halign='left', text_size=(dp(180),None)))
        h.add_widget(Button(text="💾", background_normal='', background_color=(0,0,0,0), color=(1,1,1,1), size_hint_x=None, width=dp(40), on_press=lambda x: show_warning(DB.backup_to_server())))
        root.add_widget(h)
        tabs = BoxLayout(size_hint_y=None, height=dp(44))
        with tabs.canvas.before:
            Color(rgba=get_color_from_hex("#075E54"))
            tabs.bg = Rectangle(pos=tabs.pos, size=tabs.size)
        tabs.bind(pos=lambda i,v: setattr(i.bg, 'pos', v), size=lambda i,v: setattr(i.bg, 'size', v))
        for name in ["CHATS","STATUS","CALLS"]:
            tabs.add_widget(Button(text=name, background_normal='', background_color=(0,0,0,0), color=(1,1,1,1), bold=(name=="CHATS"), font_size=dp(13)))
        root.add_widget(tabs)
        scroll = ScrollView()
        box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=0)
        box.bind(minimum_height=box.setter('height'))
        data = [("🧠","AT BRAIN","WASM + RAKSHAK + SECURE active","12:58",3),("🌍","AT World Mater","Welcome","12:50",1),("🖼️","Poster Studio","Poster exported","11:30",0),("🌐","Online AT","typing...","11:15",5),("📷","Camera","Photo captured","10:20",0),("🖼️","Gallery","12 images","09:50",0),("👤","Contacts","Anuj Tripathi","Yesterday",0),("📞","Call Logs","Missed voice call","Yesterday",2),("🎙️","Voice Notes","0:24 voice","Yesterday",0),("💾","Downloads","AT_Banner.png","Monday",0),("🔗","Share","Shared to 3 groups","Monday",0)]
        for icon,name,msg,time,unread in data:
            box.add_widget(ChatRow(icon,name,msg,time,unread, on_press=lambda n=name: self.open_chat(n)))
        scroll.add_widget(box)
        root.add_widget(scroll)
        self.add_widget(root)
    def open_chat(self, name):
        DB.log_action(f"OPEN_{name}", {"name": name})
        warn = RAKSHAK.nazar_rakho(f"OPEN_{name}", {"name": name})
        if warn:
            show_warning(warn)
            return
        s = self.sm.get_screen('chat')
        s.set_chat(name)
        self.sm.current = 'chat'

class ChatScreen(Screen):
    def set_chat(self, name):
        self.chat_name = name
        self.clear_widgets()
        root = BoxLayout(orientation='vertical')
        h = BoxLayout(size_hint_y=None, height=dp(56), padding=[dp(5),0,dp(5),0], spacing=dp(5))
        with h.canvas.before:
            Color(rgba=get_color_from_hex("#075E54"))
            h.bg = Rectangle(pos=h.pos, size=h.size)
        h.bind(pos=lambda i,v: setattr(i.bg, 'pos', v), size=lambda i,v: setattr(i.bg, 'size', v))
        back = Button(text="<", background_normal='', background_color=(0,0,0,0), color=(1,1,1,1), size_hint_x=None, width=dp(35), on_press=lambda x: setattr(self.manager, 'current', 'main'))
        h.add_widget(back)
        h.add_widget(Label(text=name, bold=True, color=(1,1,1,1), font_size=dp(16), halign='left', text_size=(dp(200),None)))
        root.add_widget(h)
        self.msg_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(8), padding=dp(10))
        self.msg_box.bind(minimum_height=self.msg_box.setter('height'))
        with self.msg_box.canvas.before:
            Color(rgba=get_color_from_hex("#E5DDD5"))
            self.msg_box.bg = Rectangle(pos=self.msg_box.pos, size=self.msg_box.size)
        self.msg_box.bind(pos=lambda i,v: setattr(i.bg, 'pos', v), size=lambda i,v: setattr(i.bg, 'size', v))
        scroll = ScrollView()
        scroll.add_widget(self.msg_box)
        root.add_widget(scroll)
        for msg, is_me in DB.get_chats(name):
            self.add_bubble(msg, is_me)
        bottom = BoxLayout(size_hint_y=None, height=dp(52), padding=dp(6), spacing=dp(6))
        ti_box = BoxLayout(padding=[dp(10),0])
        with ti_box.canvas.before:
            Color(rgba=(1,1,1,1))
            ti_box.bg = RoundedRectangle(pos=ti_box.pos, size=ti_box.size, radius=[dp(24)])
        ti_box.bind(pos=lambda i,v: setattr(i.bg, 'pos', v), size=lambda i,v: setattr(i.bg, 'size', v))
        self.ti = TextInput(hint_text="Message", background_normal='', background_color=(0,0,0,0), multiline=False, on_text_validate=self.send_msg)
        ti_box.add_widget(self.ti)
        bottom.add_widget(ti_box)
        send = Button(text="➤", size_hint_x=None, width=dp(48), background_normal='', background_color=get_color_from_hex("#25D366"), color=(1,1,1,1), on_press=self.send_msg)
        bottom.add_widget(send)
        root.add_widget(bottom)
        self.add_widget(root)
    def add_bubble(self, text, is_me):
        bubble = BoxLayout(size_hint_y=None, height=dp(60), size_hint_x=None, width=dp(260))
        with bubble.canvas.before:
            Color(rgba=get_color_from_hex("#DCF8C6") if is_me else get_color_from_hex("#FFFFFF"))
            bubble.rect = RoundedRectangle(pos=bubble.pos, size=bubble.size, radius=[dp(8)])
        bubble.bind(pos=lambda i,v: setattr(i.rect, 'pos', v), size=lambda i,v: setattr(i.rect, 'size', v))
        bubble.add_widget(Label(text=text, color=(0,0,0,1), font_size=dp(13), text_size=(dp(240),None), halign='left'))
        self.msg_box.add_widget(bubble)
    def send_msg(self, *args):
        text = self.ti.text.strip()
        if not text:
            return
        self.ti.text = ""
        DB.save_chat(self.chat_name, text, True)
        self.add_bubble(text, True)
        DB.log_action("SEND_MSG", {"chat": self.chat_name, "msg": text})
        warn = RAKSHAK.nazar_rakho("SEND_MSG", {"chat": self.chat_name, "msg": text})
        if warn:
            show_warning(warn)
            return
        reply = RAKSHAK.online_reply(text)
        DB.save_chat(self.chat_name, reply, False)
        self.add_bubble(reply, False)

class ATWorldMaterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(sm, name='main'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

ATWorldMaterApp().run()# AT World Mater - FINAL - WHATSAPP CLONE + RAKSHAK
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex, platform
from kivy.graphics import Color, Rectangle, Ellipse, RoundedRectangle
import sqlite3, os, json, datetime, threading, requests

Window.clearcolor = get_color_from_hex("#FFFFFF")
SERVER_URL = "https://at-world-server.onrender.com"
USER_ID = "Anuj_Tripathi_001"

if platform == 'android':
    from android.storage import app_storage_path
    DB_PATH = os.path.join(app_storage_path(), "at_world_mater.db")
else:
    DB_PATH = "at_world_mater.db"

class FullDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, user_id TEXT, name TEXT, message TEXT, is_me INTEGER, time TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS actions (id INTEGER PRIMARY KEY, user_id TEXT, action TEXT, data TEXT, time TEXT)")
    def save_chat(self, name, msg, is_me):
        self.conn.execute("INSERT INTO chats (user_id,name,message,is_me,time) VALUES (?,?,?,?,?)", (USER_ID, name, msg, 1 if is_me else 0, str(datetime.datetime.now())[:19]))
        self.conn.commit()
    def get_chats(self, name):
        cur = self.conn.execute("SELECT message, is_me FROM chats WHERE name=? AND user_id=? ORDER BY id", (name, USER_ID))
        return cur.fetchall()
    def log_action(self, action, data):
        self.conn.execute("INSERT INTO actions (user_id,action,data,time) VALUES (?,?,?,?)", (USER_ID, action, json.dumps(data), str(datetime.datetime.now())[:19]))
        self.conn.commit()
    def backup_to_server(self):
        try:
            all_chats = self.conn.execute("SELECT * FROM chats").fetchall()
            threading.Thread(target=lambda: requests.post(f"{SERVER_URL}/api/backup", json={"user_id": USER_ID, "chats": str(all_chats)}, timeout=5)).start()
            return f"✅ {len(all_chats)} chats SERVER pe backup!"
        except Exception as e:
            return f"Backup fail: {e}"

DB = FullDB()

class RakshakAI:
    def nazar_rakho(self, action, data):
        def send_online():
            try:
                requests.post(f"{SERVER_URL}/api/log", json={"user_id": USER_ID, "action": action, "data": data}, timeout=4)
            except:
                pass
        threading.Thread(target=send_online).start()
        txt = str(data).lower()
        if "ab
