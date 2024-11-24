import requests
import time

while True:
    print("waiting for inbox")
    get = requests.get("http://127.0.0.1:50001/InboxNotifier")
    processInbox = bool(get.json())
    print("processing new inbox")
    if processInbox:
        processing = {
            'do' : 'stuff'
        }
        post = requests.post("http://127.0.0.1:50000/doStuff", json = processing)
        payload = {
            'newInboxAvailable' : False
        }
        post = requests.post("http://127.0.0.1:50001/InboxNotifier", json = payload)
    time.sleep(3)