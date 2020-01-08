#!/usr/bin/env python3
"""get api"""
import os


class GetApi:
    """get api"""

    def __init__(self):
        # self.api = "http://127.0.0.1:3000/"
        self.base_url = "https://scitest.esss.lu.se/"
        #self.base_url = "https://scicat.esss.se/"
        self.api = os.path.join(self.base_url, "api/v3/")

    def get(self):
        """get api"""
        return self.base_url


def main():
    """main"""
    vis = GetApi()
    print(vis.get())


if __name__ == "__main__":
    main()
