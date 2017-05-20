from json import loads, dumps
import vk_api


token='60333e916062691b1a5aaf8ab07811f1029bc23864c2198aa03a380ee3468e2a4bc096227f683402a069d'
vk = vk_api.VkApi(token=token)


def get_dogs():
    with open('Dogs.txt', 'r', encoding="utf-8") as f:
        text=f.read()
        dic =loads(text)
    return dic['items']
    

def add_dog(dog):
    dogs=get_dogs()
    dogs.append(dog)
    with open('Dogs.txt', 'w') as f:
        text=dumps({'items': dogs})
        f.write(text)

def delete_dog(name):
    dogs = get_dogs()
    dogs = [dog for dog in dogs if not dog['Name'] == name]
    with open('Dogs.txt', 'w') as f:
        text=dumps({'items': dogs})
        f.write(text)

def get_dog(name):
    dogs=get_dogs()
    dogs=[dog for dog in dogs if dog['Name']==name]
    return dogs[0]
        

#add_dog({'breed':'labrador','color':'black','age':'puppy','sex':'male','date of birth': 'January 6, 1999','tattoo':'BBI 162','name':'ENS LUMENS KEEPER of SECRETS'})
#get_dog('ENS LUMENS KEEPER of SECRETS')
