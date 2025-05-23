from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from encryptor import generate_key, encrypt_folder
from decryptor import decrypt_folder, load_key
import os
from kivy.utils import platform

# Define target folder
if platform == 'android':
    from android.storage import app_storage_path
    BASE_PATH = app_storage_path()
else:
    BASE_PATH = os.getcwd()

TARGET_FOLDER = os.path.join(BASE_PATH, "test_files")
os.makedirs(TARGET_FOLDER, exist_ok=True)

class RansomwareSimulator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.status_label = Label(text="Welcome to the Ransomware Simulator", font_size=16)
        self.add_widget(self.status_label)

        self.encrypt_button = Button(text="🔐 Encrypt Files", size_hint=(1, 0.2))
        self.encrypt_button.bind(on_press=self.encrypt_files)
        self.add_widget(self.encrypt_button)

        self.input_key = TextInput(hint_text="Enter decryption key...", multiline=False, size_hint=(1, 0.2))
        self.add_widget(self.input_key)

        self.decrypt_button = Button(text="🔓 Decrypt Files", size_hint=(1, 0.2))
        self.decrypt_button.bind(on_press=self.decrypt_files)
        self.add_widget(self.decrypt_button)

    def encrypt_files(self, instance):
        key = generate_key()
        encrypt_folder(TARGET_FOLDER, key)
        self.status_label.text = f"Files encrypted in: {TARGET_FOLDER}"

    def decrypt_files(self, instance):
        try:
            user_key = self.input_key.text.encode()
            stored_key = load_key()
            if user_key == stored_key:
                decrypt_folder(TARGET_FOLDER, user_key)
                self.status_label.text = "✅ Files decrypted successfully."
            else:
                self.status_label.text = "❌ Wrong key."
        except Exception as e:
            self.status_label.text = f"Error: {e}"

class RansomApp(App):
    def build(self):
        return RansomwareSimulator()

if __name__ == "__main__":
    RansomApp().run()
