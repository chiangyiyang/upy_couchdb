import urequests as r


def get_uuids(base_url, headers={}):
    return r.get(base_url + "/_uuids", headers=headers).json()

def get_all_dbs(base_url, headers={}):
    return r.get(base_url + "/_all_dbs", headers=headers).json()

def get_db(base_url, db, headers={}):
    return r.get(base_url + "/" + db, headers=headers).json()

def add_db(base_url, db, headers={}):
    return r.put("{}/{}".format(base_url, db), headers=headers).json()

def del_db(base_url, db, headers={}):
    return r.delete("{}/{}".format(base_url, db), headers=headers).json()

def add_doc(base_url, db, id, doc, headers={}):
    return r.put("{}/{}/{}".format(base_url, db, id), json=doc, headers=headers).json()

def add_doc_with_update(base_url, db, path, doc, headers={}):
    return r.post("{}/{}/{}".format(base_url, db, path), json=doc, headers=headers).json()
