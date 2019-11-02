import urequests as r


def get_all_dbs(base_url):
    return r.get(base_url + "/_all_dbs").json()

def get_db(base_url, db):
    return r.get(base_url + "/" + db).json()

def add_db(base_url, db, headers):
    return r.put("{}/{}".format(base_url, db), headers=headers).json()

def del_db(base_url, db, headers):
    return r.delete("{}/{}".format(base_url, db), headers=headers).json()

def add_doc(base_url, db, doc):
    return r.post("{}/{}".format(base_url, db), json=doc).json()

def add_doc_with_update(base_url, db, path, doc):
    return r.post("{}/{}/{}".format(base_url, db, path), json=doc).json()
