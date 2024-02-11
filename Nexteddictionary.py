referencebooks={
    "book1":{
        "name": "Programming with Python",
        "year": 2021,
        "author": "Abhishek",
        "price":1000
    },
    "book2":{
        "name": "I am sorry",
        "year": 2023,
        "author": "Saurav",
        "price":1500
    },
    "book3":{
        "name": "Alchii manchey",
        "year": 2022,
        "author": "Aaiyaa",
        "price":2000
    },
    "book4":{
        "name": "Hacker",
        "year": 2021,
        "author": "Mukundaa",
        "price":2500
    },
    "book5":{
        "name": "Subtle arts",
        "year": 2019,
        "author": "Saru",
        "price":3000
    },
    "book6":{
        "name": "Ikigai",
        "year": 2023,
        "author": "Yushaa",
        "price":35000
    }
}
print(referencebooks.values())
print(len(referencebooks.values()))
for key in referencebooks.values():
    if(key.get("price")<1500):
        print(key.values())  
    