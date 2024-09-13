import requests
import time
from datetime import datetime

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def urlinfo():
    print(Y + "Note : URL = http://example.com")
    url = input("URL >> ")
    print("-" * 50)
    print(cyan + "          Trace Results        ")
    print("-" * 50)
    
    try:
        r = requests.get(url, allow_redirects=True)  # Follow redirects if they occur
        current_datetime = datetime.now()
        print("[+] Traced Date and Time :", current_datetime)
        
        # Check if the request was redirected (status code 3xx)
        if r.history:
            print(green + "[-] 301 Redirected")
            for resp in r.history:
                print(cyan + f"Redirected from: {resp.url} -> {r.url}")
        else:
            print(green + "[-] No Redirect")
            print(cyan + "[-] Final URL: " + r.url)
    
    except Exception as e:
        print(red + "Error Occurred: " + str(e))

if __name__ == "__main__":
    urlinfo()
