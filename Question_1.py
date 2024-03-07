# """
# create a new  array of dictionary by extracting data from data,json
# new dictionay thus created should be as shown below


# [
#     {
#      "name": "Organic Honeycrisp Apples Bag",
#      "categories": ["Produce","Fruits","Apples",
#      "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
#      "base_price":0.64,
#      "availability_status":true
#     },
#     {
#      "name": "Granny Smith Apples",
#      "categories": ["Produce","Fruits","Apples",
#      "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
#      "base_price":0.64,
#      "availability_status":true
#     }
#     .
#     .
#     .
#     .
    
# ]


# Remember to extract all items above illustrated are just sample
# """





import json
with open('/home/fahis/exam/rotech_exam/Set 1/data.json', 'r') as file:
    data = json.load(file)
    
    new_array = []
    for item in data["items"]:
        new_dict = {
        
        "name": item.get("name"),
        "categories": item.get("categories"),
        "image": item.get("images"),
        "base_price": item.get("base_price"),
        "availability_status": item.get("availability_status")
        
    }
        new_array.append(new_dict)

print(new_array)
