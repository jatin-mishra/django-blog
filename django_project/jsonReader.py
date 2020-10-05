import json

with open('posts.json', 'r') as json_file:
    json_object = json.load(json_file)

# print(json_object)

# print(json.dumps(json_object))

# print(json.dumps(json_object, indent=1))
with open('newposts.json','w') as outfile:
	json.dump(json_object,outfile, indent=1)