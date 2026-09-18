contactos = {
    "maria": {"nombre_completo": "maria camila carrillo santana",
        "phone":3246567106,
        "adress": "santo domingo"
        }, 
    "juan": {"nombre_completo":"juan camilo rojas torres",
        "phone":3135468346,
        "adress":"malambo"}
}
print(contactos["maria"]["nombre_completo"])
print(contactos)["juan"]["nombre_completo"]

Runners = {
    "Logan sargeant":{ 
        "nombre_completo":"Logan Hunter sargeant",
        "profession":"Runner F1", 
        "start_of_career":"karting_in_2008", 
        "age":25, 
        "awards":37
        },
    "max verstapen": {"nombre_completo":"max_emilian_verstapen", 
                      "profession": "Runner F1", "nickname": "the Flying Dutchman", "age":"28 years old",
                      "awards":247}
}

print(Runners["Logan sargeant"]["nombre_completo"])
print(Runners["max verstapen"]["nombre_completo"])
