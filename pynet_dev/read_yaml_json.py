import yaml
import json


with open("address_book.yml") as f:
    yaml_oput = yaml.load(f)

print "\nThis is the YAML file: "
print yaml_oput


with open("address_book.json") as f:
    json_oput = json.load(f)

print "\nThis is the JSON file: "
print json_oput
