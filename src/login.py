#!/usr/bin/env python3
"""scicat login class"""
import sys
import platform

import json

import requests
import keyring

from get_api import GetApi


class Login:
    """scicat login class"""
    api = ""
    token = ""
    date = ""

    def get_access_token(self):
        """get access token"""
        apix = GetApi()
        self.api = apix.api
        username = "ingestor"
        if platform.system() == 'Darwin':
            password = keyring.get_password('scicat', username)
        else:
            with open("config.json") as json_file:
                data = json.load(json_file)
                username = data["username"]
                password = data["password"]

        token = ""

        login_url = self.api + "/Users/login"
        config = {
            "username": username,
            "password": password
        }
        print(password)
        response = requests.post(login_url, data=config)
        print(response.json())
        token = response.json()
        if response.status_code == 200:
            self.token = token["id"]
        else:
            print("error, can't login")
            sys.exit()

        print("token id", token["id"])
        return self.token


def main():
    """main"""
    login = Login()
    login.get_access_token()


if __name__ == "__main__":
    main()
