from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp

class ATWorldApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "AT World Matter"
        main = BoxLayout(orientation='vertical', spacing=dp(5), padding=dp(10))

        # BANNER
        try:
            banner_box = BoxLayout(size_hint_y=None, height=dp(150))
            banner_box.add_widget(Image(source='banner.png', allow_stretch=True, keep_ratio=False))
            main.add_widget(banner_box)
        except:
            main.add_widget(Label(text='AT World Matter', size_hint_y=None, height=dp(50), color=(0,0,0,1)))

        # HEADER
        header = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        try:
            header.add_widget(Image(source='icon.png', size_hint_x=None, width=dp(40)))
        except:
            pass
        header.add_widget(Label(text='AT World Matter', color=(0,0,0,1), bold=True))
        main.add_widget(header)

        # LIST
        scroll = ScrollView()
        list_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(10), padding=dp(10))
        list_box.bind(minimum_height=list_box.setter('height'))
        
        for name in ["Anuj Tripathi", "AT Group", "AT World Matter", "AT Services", "Contact Us"]:
            btn = Button(text=name, size_hint_y=None, height=dp(50), background_color=(0.2,0.6,1,1))
            list_box.add_widget(btn)
        
        scroll.add_widget(list_box)
        main.add_widget(scroll)

        return main

if __name__ == '__main__':
    ATWorldApp().run()
