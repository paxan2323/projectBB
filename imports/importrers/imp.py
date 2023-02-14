import requests
import json

class ImporterXML: # В разработке
    def __init__(self, config):
        self.config = config

    def import_data(self):
        response = requests.get(self.config.url)
        data = response.text
        
        
        response = []
        categories = []
        services = []
        
        for d in data:
            #categories
            idCat = d[0][0]
            nameCat = d[0][1]
            categories.append({"id":idCat,"name":nameCat}) 
            #services  
            idServ = d[1][0]
            nameServ = d[1][1]
            category_id = d[1][2]
            services.append({"id":idServ,"name":nameServ,"category_id":category_id}) 
        result = {"categories": categories, "services": services}
        
        with open(f"{self.config.id}.json", "w") as file:
            json.dump(result, file)
            
            
            
            
            
            
# {
#   "categories":[
#     {
#       "id":1,
#       "name":"category-1"
#     },
#     {
#       "id":2,
#       "name":"category-2"
#     }
#   ],
#   "services":[
#     {
#       "id":"service-1",
#       "name":"sertvice-name-1",
#       "category_id":1
#     },
#     {
#       "id":"service-2",
#       "name":"sertvice-name-2",
#       "category_id":2
#     }
#   ]
# }