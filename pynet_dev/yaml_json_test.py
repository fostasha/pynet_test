import yaml
import json

ip_addr = ['10','0','20','1']
ip_addr2 = ['10','0','21','1']
ip_addr3 = ['10','0','22','1']


address_book = [[ip_addr], [ip_addr2], [ip_addr3]]

address_book.append({})
address_book[-1]
address_book[-1]['attribs'] = range(5)

for list in address_book:
    for x in list:
        print x


#YAML
#yaml.dump(address_book, default_flow_style=False)

#Creates .yml file with variable address_book info
with open(("address_book.yml"), "w") as f:
    f.write(yaml.dump(address_book, default_flow_style=False))

print "\nThis is the YAML file address_book.yml as a variable:"
#Creates variable with .yml file's info
with open("address_book.yml") as f:
    yaml_address_book = yaml.load(f)

print yaml_address_book

#########################

#JSON

address_book_json = json.dumps(address_book)

with open (("address_book.json"), "w") as f:
    json.dump(address_book, f)

with open("address_book.json") as f:
    json_address_book = json.load(f)

print "\nThis is the JSON file address_book.json as a variable:"

print json_address_book
