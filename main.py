#!/usr/bin/env python3
import fire
from twofa_cl import key_storage

storage = key_storage.KeyChain()


def list():
    return storage.list()


def get(key):
    return storage.get(key)


def add(secret, name):
    return storage.add(secret, name)


def delete(name):
    return storage.delete(name)


if __name__ == '__main__':
    fire.Fire()
