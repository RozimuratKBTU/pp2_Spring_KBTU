import json

date_json = open('data.json').read()

json_object = json.loads(date_json)

imdate = json_object["imdate"]
for i in imdate:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{0:50} {1:20}{2:7}{3:6} ".format(dn,descr,speed,mtu))