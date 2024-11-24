import requests
import time

while True:
    payload = {
        'newInboxAvailable' : True
    }
    print("new inbox available")
    post = requests.post("http://127.0.0.1:50001/InboxNotifier", json = payload)
    print("waiting")
    time.sleep(3)

