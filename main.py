import random

# list of words for the game
mots = ["python", "programmation", "ordinateur", "algorithme", "developpeur"]

def choose_word():
    return random.choice(mots)

def display_word(word, found_letters):
    result = ""
    for letter in word:
        if letter in found_letters:
            result += letter
        else:
            result += "_"
    return result

def main():
    mot = choose_word()
    lettres_trouvees = set()
    erreurs = 0
    max_erreurs = 6

    print("Bienvenue au jeu du Pendu!")
    
    while erreurs < max_erreurs:
        print("\nMot actuel:", display_word(mot, lettres_trouvees))
        print("Erreurs:", erreurs, "/", max_erreurs)
        
        lettre = input("Devinez une lettre: ").lower()
        
        if len(lettre) != 1:
            print("Veuillez entrer une seule lettre.")
            continue
        
        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
            continue
        
        if lettre in mot:
            lettres_trouvees.add(lettre)
            print("Bonne devinette!")
        else:
            erreurs += 1
            print("Mauvaise devinette.")
        
        if set(mot) == lettres_trouvees:
            print("\nFélicitations! Vous avez gagné!")
            print("Le mot était:", mot)
            return
    
    print("\nDésolé, vous avez perdu.")
    print("Le mot était:", mot)

main()