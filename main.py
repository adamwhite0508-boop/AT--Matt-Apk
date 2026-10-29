from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ATWorldApp(App):
    def build(self):
        self.title = "AT World Matter"
        main = BoxLayout(orientation='vertical')
        header = BoxLayout(size_hint_y=None, height=60)
        header.add_widget(Label(text='AT World Matter', bold=True))
        scroll = ScrollView()
        list_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=2)
        list_box.bind(minimum_height=list_box.setter('height'))
        chats = ["Anuj Tripathi", "AT Group", "AT Support"]
        for name in chats:
            b = Button(text=name, size_hint_y=None, height=70)
            list_box.add_widget(b)
        scroll.add_widget(list_box)
        main.add_widget(header)
        main.add_widget(scroll)
        main.add_widget(Button(text='AT WORLD Working!', size_hint_y=None, height=50))
        return main

ATWorldApp().run()
