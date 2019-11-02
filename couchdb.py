import urequests as r


def get_all_dbs(base_url):
    return r.get(base_url + "/_all_dbs").json()

def get_db(base_url, db, headers={}):
    return r.get(base_url + "/" + db, headers=headers).json()

def add_db(base_url, db, headers={}):
    return r.put("{}/{}".format(base_url, db), headers=headers).json()

def del_db(base_url, db, headers={}):
    return r.delete("{}/{}".format(base_url, db), headers=headers).json()

def add_doc(base_url, db, doc, headers={}):
    return r.post("{}/{}".format(base_url, db), json=doc, headers=headers).json()

def add_doc_with_update(base_url, db, path, doc, headers={}):
    return r.post("{}/{}/{}".format(base_url, db, path), json=doc, headers=headers).json()
