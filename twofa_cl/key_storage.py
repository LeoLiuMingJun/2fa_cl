import json
import os
import twofa_cl.core
import pyperclip

KEY_STORAGE_FILE = f'{os.path.dirname(os.path.abspath(__file__))}/keys.json'


class KeyChain:
    def __init__(self):
        with open(KEY_STORAGE_FILE, 'a+') as f:
            f.seek(0, 0)
            self.keys = json.load(f)

    def add(self, secret, key_name):
        self.keys[key_name] = secret
        self.update()

    def delete(self, key_name):
        del self.keys[key_name]
        self.update()

    def update(self):
        with open(KEY_STORAGE_FILE, 'w+') as f:
            f.write(json.dumps(self.keys))

    def list(self):
        index = 1
        if self.keys:
            print("Existing Keys:")
            for key, value in self.keys.items():
                print(f"{index}: {key}")
                index += 1

    def get(self, key):
        try:
            int(key)
            index = 0
            for _, value in self.keys.items():
                index += 1
                if index == key:
                    token = twofa_cl.core.get_totp_token(value)
                    pyperclip.copy(token)
                    return token
        except ValueError:
            secret = self.keys[key]
            token = twofa_cl.core.get_totp_token(secret)
            pyperclip.copy(token)
            return token
