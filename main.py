from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class ATWorldApp(App):
    def build(self):
        self.title = "AT World Matter"
        main = BoxLayout(orientation='vertical', spacing=0, padding=0)
        
        # BANNER - Upar wala Globe logo (aapka banner.png)
        try:
            banner_box = BoxLayout(size_hint_y=None, height=190, padding=5)
            banner_box.add_widget(Image(source='banner.png', allow_stretch=True, keep_ratio=True))
            main.add_widget(banner_box)
        except:
            main.add_widget(Label(text='AT World Matter', bold=True, color=(0,0,0,1), size_hint_y=None, height=50))

        # HEADER - Chhota Icon + Naam
        header = BoxLayout(size_hint_y=None, height=70, spacing=10, padding=10)
        try:
            header.add_widget(Image(source='icon.png', size_hint_x=None, width=60))
        except:
            pass
        header.add_widget(Label(text='AT World Matter', bold=True, color=(0,0,0.8,1), font_size=22))
        main.add_widget(header)

        # LIST
        scroll = ScrollView()
        list_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=8, padding=10)
        list_box.bind(minimum_height=list_box.setter('height'))
        for name in ["Anuj Tripathi", "AT Group", "AT Support", "AT World Team", "AT Matter Lab"]:
            b = Button(text=name, size_hint_y=None, height=70, background_color=(0,0.5,0.9,1), background_normal='')
            list_box.add_widget(b)
        scroll.add_widget(list_box)
        main.add_widget(scroll)
        
        main.add_widget(Button(text='AT WORLD MATTER - Working 100%!', size_hint_y=None, height=55, background_color=(0,0.7,0.3,1), background_normal=''))
        return main

ATWorldApp().run()
