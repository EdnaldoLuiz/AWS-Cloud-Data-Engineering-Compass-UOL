animais = [
    "Gato",
    "Cachorro",
    "Elefante",
    "Leão",
    "Girafa",
    "Tigre",
    "Urso",
    "Panda",
    "Hipopótamo",
    "Zebra",
    "Camelo",
    "Rinoceronte",
    "Pássaro",
    "Peixe",
    "Cobra",
    "Jacaré",
    "Crocodilo",
    "Macaco",
    "Coelho",
    "Pinguim",
]

animais.sort()

for animal in animais:
    print(animal)

with open("animais.csv", "w") as arquivo:
    for animal in animais:
        arquivo.write(f"{animal}\n")
