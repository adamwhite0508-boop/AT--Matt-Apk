from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        MDLabel:
            text: "AT WORLD"
            halign: "center"
            font_style: "H5"
            bold: True
        MDLabel:
            text: "App Successfully Opened!"
            halign: "center"
        MDRaisedButton:
            text: "Click Me - AT World Matter"
            pos_hint: {"center_x": .5}
            on_release: app.test_click()
'''

class ATWorldMatterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)
    
    def test_click(self):
        print("AT WORLD Working!")

ATWorldMatterApp().run()
