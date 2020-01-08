#!/usr/bin/env python3
"""mulitple login and collect errors"""
import platform
import getpass
import time

import requests
import keyring


class DebugLogin:
    """get error"""
    url = "https://scicat07.esss.lu.se:32223/"
    #url = "https://scitest.esss.lu.se/"
    username = ""
    username = ""
    password = ""
    success = 0
    failed = 0
    error = []

    def __init__(self):
        self.username = getpass.getuser()
        if platform.system() == 'Darwin':
            self.password = keyring.get_password('scicat', self.username)
        url = self.url + "/api/v3/PublishedData"
        response = requests.get(url, verify=False)
        print("\n\n")


    def debug(self):
        """debug"""
        login_url = self.url + "auth/msad"
        log_data = {
            "username": self.username,
            "password": self.password
        }
        print(login_url)
        response = requests.post(login_url, data=log_data, verify=False)
        print(response.json())
        if response.status_code == 200:
            print("success")
            self.success += 1
        elif response.status_code == 200:
            print("failed")
            self.failed += 1
            self.error.push(reponse.json())

    def loop(self):
        """loop"""
        for i in range(1,3):
            self.debug()

def main():
    """main"""
    debug = DebugLogin()
    debug.debug()


if __name__ == "__main__":
    main()
