# combination of key value pairs
dic = {
    "guru": "human being",
    "spoon": "object"
}

# print(dic["guru"]) # return error
# print(dic.get("guru"))  # return None
# print(dic.keys())
# print(dic.values())

# for value in dic.keys():
#     print(dic[value])

print(dic.items())

for key, value in dic.items():
    print(key, value)