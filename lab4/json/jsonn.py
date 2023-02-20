import json

file =open('sample-data.json')
s = file.read()
file.close()
d = json.loads(s)
imdata = d["imdata"]
print("""Interface Status================================================================================""")
print("""DN                                             Description             Speed         MTU """)

for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:50} {descr:20}{speed:14}{mtu:6} ")
    



