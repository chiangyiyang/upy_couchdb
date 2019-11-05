from utils import load_settings
import urandom as rnd
import couchdb as db
import wifi
from time import sleep
import gc
gc.collect()


settings = load_settings()
ap = settings["ap"]
ap_pass = settings["ap_password"]
cloudant_url = settings["cloudant_url"]
cloudant_auth = settings["cloudant_auth"]
db_name = settings["db_name"]
dev_id = settings["dev_id"]

base_url = 'https://{}'.format(cloudant_url)
headers = {'Authorization': 'Basic {}'.format(cloudant_auth)}

if wifi.is_connected() == False:
    wifi.connect(ap, ap_pass)


try:
    # res = db.get_all_dbs(base_url, headers = headers)
    # res = db.get_db(base_url, db_name, headers = headers)
    # res = db.add_db(base_url, db_name, headers = headers)
    # res = db.del_db(base_url, db_name, headers = headers)
    # print(res)

    for i in range(100):
        # res = db.add_doc(
        #     base_url,
        #     db_name,
        #     db.get_uuids(base_url)['uuids'][0],
        #     {
        #         'dev_id': dev_id,
        #         'temperature': 20 + rnd.getrandbits(4),
        #         'humidity': 80 + rnd.getrandbits(4)
        #     },
        #     headers=headers
        # )

        res = db.add_doc_with_update(
            base_url,
            db_name,
            '_design/utils/_update/add_with_timestamp',
            {
                'dev_id': dev_id,
                'temperature': 20 + rnd.getrandbits(4),
                'humidity': 80 + rnd.getrandbits(4)
            },
            headers=headers
        )
        print(res)
        sleep(3)

    del res
except OSError as err:
    print(err)

# wifi.disconnect()
