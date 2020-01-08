#!/usr/bin/env python3
import time

from login import Login

class TestLogin():
    """loop"""

    def loop(self):
        """loop"""
        for i in range(1, 10):
            time.sleep(3)
            login = Login()
            login.get_access_token()
            


def main():
    """main"""
    login_loop = TestLogin()
    login_loop.loop()

if __name__ == "__main__":
    main()