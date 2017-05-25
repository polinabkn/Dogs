from json import loads, dumps

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

def get_information():
    with open('Information.txt', 'r', encoding="utf-8") as f:
        text1=f.read()
        dic1 =loads(text1)
    return dic1['items']

def get_breeditem(name):
    breeds=get_information()
    breeds=[breed for breed in breeds if breed['Breed']==name]
    return breeds[0]

def get_breedinfo(name):
    need=get_breeditem(name)
    return need['Information']
        
