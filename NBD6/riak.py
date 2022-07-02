#!/usr/bin/env python

import riak

client = riak.RiakClient(host="192.168.1.128", pb_port=8087)
bucket = client.bucket("s14924")

print "Wrzucenie do bazy:"
key = "Ezreal"
value = {"name": "Ezreal", "range": True, "baseHP": 600, "attackSpeed": 0.72}
ezreal = bucket.new(key, data=value)
ezreal.store()

print "Pobranie z bazy i wypisanie:"
ezrealPobrany = bucket.get(key)
print ezrealPobrany.encoded_data

print "Modyfikacja:"
ezrealPobrany.data["baseHP"] = 666
ezrealPobrany.store()

print "Pobranie z bazy i wypisanie:"
ezrealPobrany = bucket.get(key)
print ezrealPobrany.encoded_data

print "Usuniecie z bazy:"
ezrealPobrany.delete()

print "Proba pobrania z bazy:"
ezrealPobrany = bucket.get(key)
print ezrealPobrany.encoded_data