from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
import requests, threading
GROQ_API_KEY="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"
class ATWorldApp(MDApp):
    def build(self):
        self.title="AT World Matter"
        root=MDBoxLayout(orientation='vertical',padding=10,spacing=10)
        self.chat_layout=MDBoxLayout(orientation='vertical',size_hint_y=None,adaptive_height=True,spacing=8)
        scroll=MDScrollView()
        scroll.add_widget(self.chat_layout)
        self.input_field=MDTextField(hint_text="AT World Matter me likho...",mode="round")
        send_btn=MDRaisedButton(text="Send")
        send_btn.bind(on_release=self.send_msg)
        input_box=MDBoxLayout(orientation='horizontal',size_hint_y=None,height=60,spacing=10)
        input_box.add_widget(self.input_field)
        input_box.add_widget(send_btn)
        root.add_widget(scroll)
        root.add_widget(input_box)
        Clock.schedule_once(lambda x: self.add_msg("AT AI","Namaste Sir! Main AT World Matter ka AI hu!"),0.5)
        return root
    def add_msg(self,user,msg):
        self.chat_layout.add_widget(MDLabel(text=f"[b]{user}:[/b] {msg}",markup=True,size_hint_y=None,adaptive_height=True))
    def send_msg(self,*args):
        txt=self.input_field.text.strip()
        if not txt: return
        self.add_msg("You",txt)
        self.input_field.text=""
        self.add_msg("AT AI","Soch raha hu...")
        threading.Thread(target=self.call_groq,args=(txt,),daemon=True).start()
    def call_groq(self,user_text):
        try:
            headers={"Authorization": f"Bearer {GROQ_API_KEY}","Content-Type": "application/json"}
            payload={"model":"llama-3.3-70b-versatile","messages":[{"role":"system","content":"You are AT World Matter AI, reply in Hinglish."},{"role":"user","content":user_text}]}
            r=requests.post("https://api.groq.com/openai/v1/chat/completions",headers=headers,json=payload,timeout=30).json()
            reply=r['choices'][0]['message']['content']
            Clock.schedule_once(lambda dt: self._reply(reply),0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self._reply(f"Error: {e}"),0)
    def _reply(self,reply):
        if self.chat_layout.children: self.chat_layout.remove_widget(self.chat_layout.children[0])
        self.add_msg("AT AI",reply)
ATWorldApp().run()
