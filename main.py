from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.utils import platform
import random
import os
import re
from datetime import datetime

# ======== NEW FEATURE: AT World Matter Security + User AI + JARVIS ========
class SecurityGuard:
    def __init__(self):
        self.banned_words = ["abuse", "sarkar virodhi", "bomb", "gaali", "hate", "terror"]
        self.hacking_words = ["hack", "crack", "mod apk", "bypass", "inject", "sql", "../", "root", "cheat"]
        self.store = JsonStore('at_world_matter_security.json')
    def check_all(self, user_id, message):
        msg = message.lower()
        for w in self.hacking_words:
            if w in msg:
                return False, "🚫 AT World Matter Security: Hacking attempt blocked!"
        for w in self.banned_words:
            if w in msg:
                return self.take_action(user_id, w)
        return True, ""
    def take_action(self, user_id, word):
        warnings = self.store.get(user_id)['count'] if self.store.exists(user_id) else 0
        warnings += 1
        if warnings == 1:
            self.store.put(user_id, count=warnings)
            return False, f"⚠️ AT World Matter Warning 1/2: '{word}' allowed nahi hai."
        else:
            self.store.put(user_id, count=warnings, blocked=True)
            return False, "🚫 BLOCKED by AT World Matter: 24hr block."
    def is_blocked(self, user_id):
        if self.store.exists(user_id):
            return self.store.get(user_id).get('blocked', False)
        return False

class UserMainAI:
    def __init__(self):
        self.gemini_key = "" # Yaha aapki FREE API Key ayegi
        try:
            store = JsonStore('at_chats.json')
            if store.exists("GEMINI_KEY"):
                self.gemini_key = store.get("GEMINI_KEY")['key']
        except:
            pass

    def get_reply(self, user_message):
        msg = user_message.lower()
        # JARVIS TRIGGER
        if any(x in msg for x in ["email bana", "sarkari", "government", "jal vibhag", "water pipeline", "complaint", "chithi"]):
            return "JARVIS_MODE: Sir, samajh gaya! Aapko sarkari email banana hai. Main aapko Jarvis Screen pe le chalta hu - Waha se 2 click me ban jayega! 🔥"
        if "hello" in msg or "hi" in msg:
            return "Hello! Mai AT World Matter AI hu! Jarvis Mode ON hai - Bolo kya banana hai? Email, Letter, RTI? 🧠"
        elif "kaun ho" in msg:
            return "Mai AT World Matter ka official AT BRAIN hu! Iron Man ke Jarvis jaisa - Bolke kaam karunga!"
        return f"AT BRAIN 🧠: '{user_message}' samajh gaya! 🔐 Agar email banana hai to bolo 'email bana de'"

    def create_govt_email_with_gemini(self, dept, tone, problem, consumer_no, address):
        # Agar Gemini Key nahi hai to Offline Template dega - FREE
        if not self.gemini_key or len(self.gemini_key) < 10:
            # OFFLINE TEMPLATE - Bina Internet ke
            if tone == "Sakht":
                body = f"Subject: Urgent Complaint - {dept} - Consumer No {consumer_no}\n\nTo: {dept.lower()}@gov.in\n\nSeva me,\nShri {dept} Adhikari,\n\nVishay: {problem} - {address} me gambhir samasya\n\nMahoday, Main {address} ka niwasi hu. Mere ghar ke bahar {problem} pichle 15 dino se hai. Maine 2 baar Jal Vibhag me complaint ki (Consumer No: {consumer_no}) par koi sunwai nahi hui.\n\nAapse nivedan hai ki 48 ghante me karwai karein, anyatha mujhe RTI / Consumer Forum me jana padega.\n\nDhanyavad.\n[Apka Naam]\n{address}\nDate: {datetime.now().strftime('%d-%m-%Y')}"
            else:
                body = f"Subject: Request: {problem} - {address}\n\nRespected Sir, {dept} Department,\n\nMere ghar {address} ke bahar {problem} hai. Consumer No: {consumer_no}. Kripya jaldi samadhan karein.\n\nDhanyavad."
            return body

        # ONLINE - Gemini FREE se
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.gemini_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Write a formal government complaint email in Hindi+English mix for {dept}. Tone: {tone}. Problem: {problem}. Consumer No: {consumer_no}, Address: {address}. Include Subject, To, Body, mention 2 previous complaints. Make it professional for Indian govt."
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Offline Email (Gemini Error: {e}):\n\nTo: {dept}@gov.in\nSubject: {problem}\n\nRespected Sir, {problem} at {address}. Consumer {consumer_no}. Please resolve in 48hrs."

    def log_to_main_ai(self, city, area, type_complaint):
        # Ye Main AI Heatmap ke liye - Supabase me jayega
        try:
            # Yaha Supabase code ayega - Abhi local me save kar rahe hain
            store = JsonStore('at_main_ai_heatmap.json')
            key = f"{city}_{area}_{type_complaint}"
            count = store.get(key)['count'] if store.exists(key) else 0
            store.put(key, count=count+1, city=city, area=area, type=type_complaint, last_date=str(datetime.now()))
            print(f"Main AI Logged: {key} -> {count+1}")
        except:
            pass

def is_rooted_device():
    if platform != 'android': return False
    for f in ["/system/xbin/su", "/system/bin/su"]:
        if os.path.exists(f): return True
    return False
# ======== NEW FEATURE END ========

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
    JarvisScreen:

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        Image:
            source: 'banner.png'
            size_hint: .7,.32
            pos_hint: {'center_x':.5,'center_y':.75}
        MDLabel:
            text: "AT World Matter - Jarvis ON"
            halign: "center"
            bold: True
            text_color: 0.06,0.45,0.73,1
            pos_hint: {'center_y':.56}
            font_size: "20sp"
            on_touch_down: app.on_logo_tap() if self.collide_point(*args[1].pos) else None
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
                text: "Jarvis Secure Mode - AT World Matter ✅"
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
            title: "AT World Matter"
            md_bg_color: 1,1,1,1
            specific_text_color: 0.06,0.45,0.73,1
            right_action_items: [["email-edit", lambda x: setattr(app.root, 'current', 'jarvis')], ["bell-ring", lambda x: app.test_local_push()], ["shield-account", lambda x: setattr(app.root, 'current', 'admin')], ["cog", lambda x: setattr(app.root, 'current', 'settings')]]
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

<JarvisScreen>:
    name: 'jarvis'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDTopAppBar:
            title: "AT Jarvis - Sarkari Email"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'main')]]
            right_action_items: [["content-copy", lambda x: app.copy_jarvis_email()]]
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "15dp"
                spacing: "12dp"
                adaptive_height: True
                MDLabel:
                    text: "Iron Man Jarvis - Bolo, Email Bana Du?"
                    bold: True
                    font_size: "16sp"
                    size_hint_y: None
                    height: "30dp"
                MDBoxLayout:
                    size_hint_y: None
                    height: "50dp"
                    spacing: "10dp"
                    MDRaisedButton:
                        text: "📷 Bill Scan Karo"
                        md_bg_color: 0.06,0.45,0.73,1
                        size_hint_x: .5
                        on_press: app.scan_bill()
                    MDRaisedButton:
                        text: "🎤 Bolke Batao"
                        md_bg_color: 0.6,0.2,0.8,1
                        size_hint_x: .5
                        on_press: app.voice_to_text()
                MDTextField:
                    id: jarvis_dept
                    hint_text: "Kis Vibhag Ko? Ex: Jal Vibhag, Nagar Nigam"
                    text: "Jal Vibhag"
                MDTextField:
                    id: jarvis_consumer
                    hint_text: "Consumer No / Bill No (Scan se auto ayega)"
                MDTextField:
                    id: jarvis_address
                    hint_text: "Apka Address? Ex: Gomti Nagar, Lucknow"
                    text: "Gomti Nagar, Lucknow"
                MDTextField:
                    id: jarvis_problem
                    hint_text: "Problem Kya Hai?"
                    text: "Ghar ke bahar water pipeline tooti hai, paani waste ho raha hai"
                    multiline: True
                MDBoxLayout:
                    size_hint_y: None
                    height: "45dp"
                    spacing: "8dp"
                    MDLabel:
                        text: "Tone:"
                        size_hint_x: .2
                    MDRaisedButton:
                        id: tone_pyaar
                        text: "Pyar Se"
                        size_hint_x: .25
                        md_bg_color: 0,0.6,0,1
                        on_press: app.set_tone('Pyar Se')
                    MDRaisedButton:
                        id: tone_sakht
                        text: "Sakht"
                        size_hint_x: .25
                        md_bg_color: 1,0.5,0,1
                        on_press: app.set_tone('Sakht')
                    MDRaisedButton:
                        id: tone_kanooni
                        text: "Kanooni"
                        size_hint_x: .3
                        md_bg_color: 1,0,0,1
                        on_press: app.set_tone('Kanooni')
                MDRaisedButton:
                    text: "⚡ Jarvis Se Email Banwao"
                    md_bg_color: 0.06,0.45,0.73,1
                    size_hint_y: None
                    height: "50dp"
                    font_size: "16sp"
                    bold: True
                    on_press: app.generate_jarvis_email()
                MDCard:
                    size_hint_y: None
                    height: "350dp"
                    md_bg_color: 0.95,0.95,0.95,1
                    padding: "10dp"
                    ScrollView:
                        MDLabel:
                            id: jarvis_output
                            text: "Yaha aapka sarkari email ayega...\\n\\nExample: Aap 'Bill Scan' dabao to Consumer No auto bhar jayega, fir 'Email Banwao' dabao."
                            size_hint_y: None
                            height: self.texture_size[1]
                            text_size: self.width, None

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
            text: "online - AT World Matter Secure"
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
                hint_text: "Message - 'email bana de' bolo"
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
            text: "Demo Mode - AT World Matter Secure"
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
                text: "AT World Matter"
            MDCard:
                size_hint_y: None
                height: "250dp"
                md_bg_color: 0.06,0.45,0.73,1
                padding: "15dp"
                MDLabel:
                    id: poster_preview
                    text: "AT World Matter\\nPoster Preview"
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
           
