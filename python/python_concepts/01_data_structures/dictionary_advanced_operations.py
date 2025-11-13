import pprint

info = {
    "host": "ws1",
    "domain": "rootcap.in",
    "desc": "web server",
    "app": "apache httpd",
    "version": 2.2,
}
pprint.pprint(info)
print()

# Update Operation
item = "version"
if item in info:
    info[item] = 3.6
pprint.pprint(info)
print()

# Add Operation
info["arch"] = "x86_64"
pprint.pprint(info)
print()

# Delete Operation
value = info.pop("desc")  # del info['desc'] - use when you don't need the deleted value
print(value)
pprint.pprint(info)
print()

# Read operation
# print(info['app1'])
print(info.get("app1"))
print(info.get("app1", "tomcat"))
print()

# Iterate
for item in info:
    print(item)
print()

for key, item in info.items():  # Get both key and value of dictionary
    print(key, "->", item)
