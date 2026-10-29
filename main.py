from kivy.app import App
from kivy.uix.label import Label

class ATWorldApp(App):
    def build(self):
        # Simple WebView wrapper - index.html ko load karega
        try:
            from jnius import autoclass
            from android.runnable import run_on_ui_thread
            from kivy.clock import Clock
            
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            @run_on_ui_thread
            def create_webview():
                webview = WebView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.getSettings().setDomStorageEnabled(True)
                webview.setWebViewClient(WebViewClient())
                # index.html same folder me hai
                webview.loadUrl('file:///android_asset/index.html')
                activity.setContentView(webview)

            Clock.schedule_once(lambda dt: create_webview(), 0)
            
        except Exception as e:
            print(f"WebView Error: {e}")
            return Label(text=f"AT WORLD Loading...\n{e}")

        from kivy.uix.boxlayout import BoxLayout
        return BoxLayout()

ATWorldApp().run()
