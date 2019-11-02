
from time import sleep
import wifi
import couchdb as db
import urandom as rnd
from machine import Pin
from utils import load_settings

settings = load_settings()
ap = settings["ap"]
ap_pass = settings["ap_password"]
account = settings["db_account"]
password = settings["db_password"]
# base64_auth = settings["base64_auth"]
server = settings["server"]
port = settings["port"]
db_name = settings["db_name"]
dev_id = settings["dev_id"]

led = Pin(2, Pin.OUT)
base_url = 'http://{}:{}'.format(server, port)

sleep(2)

while True:
    led.value(0)
    if wifi.is_connected() == False:
        wifi.connect(ap, ap_pass)
    try:
        res = db.add_doc_with_update(base_url, db_name, '_design/utils/_update/add_with_timestamp',
                                     {'dev_id': dev_id, 'temperature': 20 + rnd.getrandbits(4), 'humidity': 80 + rnd.getrandbits(4)})
        print(res)
    except OSError as err:
        print(err)
    led.value(1)
    sleep(3)


# wifi.disconnect()
