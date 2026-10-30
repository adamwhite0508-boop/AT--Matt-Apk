# AT World Mater - FINAL - WHATSAPP CLONE + RAKSHAK
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
