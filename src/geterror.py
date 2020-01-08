#!/usr/bin/env python3
"""mulitple login and collect errors"""
import platform
import getpass
import time
import urllib3

import requests
import keyring


class DebugLogin:
    """get error"""
    url = "https://scicat07.esss.lu.se:32223/"
    #url = "https://scitest.esss.lu.se/"
    # url = "https://scicat.esss.se/"
    username = ""
    username = ""
    password = ""
    success = 0
    failed = 0
    error = []

    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.username = getpass.getuser()
        if platform.system() == 'Darwin':
            self.password = keyring.get_password('scicat', self.username)
        url = self.url + "/api/v3/PublishedData/findOne"
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
        elif response.status_code == 500:
            print("failed")
            self.failed += 1
            self.error.append(response.json())

    def loop(self):
        """loop"""
        self.total = 3
        for i in range(0,self.total):
            time.sleep(2)
            self.debug()
            

    def report(self):
        print(f'success {self.success}/{self.total}')
        print(f'failed {self.failed}/{self.total}')

def main():
    """main"""
    debug = DebugLogin()
    debug.loop()
    debug.report()


if __name__ == "__main__":
    main()
