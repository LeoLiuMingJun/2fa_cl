import hmac, base64, struct, hashlib, time
import os
import json


def add2clipboard(text):  # TODO ehance for different OS
    command = 'echo ' + text + '| pbcopy'
    os.system(command)


def update_key_file(key_chain):
    f = open(f'{os.path.dirname(os.path.abspath(__file__))}/keys.json', 'w+')
    f.write(json.dumps(key_chain))
    f.close()


def add_key(key_chain):
    pass


def remove_key(key_chain):
    pass


# given code


def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
    return '{0:05d}'.format(h)


def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time()) // 30)


def load_existing_keys():
    f = open(f'{os.path.dirname(os.path.abspath(__file__))}/keys.json', 'a+')
    f.seek(0, 0)
    return json.load(f)


if __name__ == "__main__":
    # load dictionary of
    try:
        key_chain: dict = load_existing_keys()
    except json.JSONDecodeError:
        key_chain: dict = {}
    # given choices
    index = 1

    idx = {}
    if key_chain:
        print("Existing Keys:")
        for key, value in key_chain.items():
            print(f"{index}: {key}")
            idx[str(index)] = value
            index += 1
        print('\n' * 3)
    print("Make your Choice:")
    print("Enter N and secret string to create a new one not implemented.")
    print("Enter D and Index to remove a key.")
    print("Enter Index number to get the TOTP token.")
    #
    usr_enter = input().upper()
    if usr_enter == 'N':
        print('enter the Name e.g. google:')
        key_name = input()
        print('enter the secret string:')
        secret = input()
        key_chain[key_name] = secret
        update_key_file(key_chain)
    elif usr_enter == 'D':
        print('enter the name or index the key you want to remove')
        value = input()
        try:
            int(value)
            del key_chain[idx[value]]
        except ValueError:
            del key_chain[value]
        update_key_file(key_chain)
    else:
        add2clipboard(get_totp_token(idx[usr_enter]))
        # update_key_file(key_chain)
        print('Done token copy to clipboard')
