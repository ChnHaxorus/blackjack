import random

cartes = [1,2,3,4,5,6,7,8,9,10,10,10]
main_croupier = []
main_joueur = []

#premier tour

def start():
    print("La partie peut commencer **Distribution des cartes**")
    print("Carte tirée pour le joueur : ")
    main_joueur.append(distribution())
    print("Carte tirée pour le croupier : ")
    main_croupier.append(distribution())
    print("Carte tirée pour le joueur : ")
    main_joueur.append(distribution())
    somme_as = asse()
    if sum(somme_as[1])==21:
        print("Blackjack ! Vous remportez la main !")
        exit()
    print("Votre main vaut ",sum(somme_as[1]) ,"et j'ai ",sum(somme_as[0]),".")
    return [main_croupier,main_joueur]

def distribution():
    carte = random.choice(cartes)
    print(carte)
    return carte

def asse():
    sommeJ = sum(main_joueur)
    sommeC = sum(main_croupier)
    for i in range(len(main_joueur)):
        if main_joueur[i] == 1 and sommeJ <= 11:
            del main_joueur[i]
            main_joueur.insert(i,11)
    for y in range(len(main_croupier)):
        if main_croupier[y] == 1 and sommeC <= 11:
            del main_croupier[y]
            main_croupier.insert(y,11)
    return [main_croupier,main_joueur]

start()

#second tour

def choix_option():
    option = input("Que souhaitez vous faire ? tirer ou arreter ? ")
    return option

def choix(x):
    if x == "tirer":
        print("Carte tirée pour le joueur : ")
        main_joueur.append(distribution())
        somme_as = asse()
        if sum(somme_as[1])==21:
            print("Blackjack ! Vous remportez la main !")
            exit()
        elif sum(somme_as[1])>21:
            print("Dommage. Vous perdez la main en ayant fait ",sum(somme_as[1]))
            exit()
        elif sum(somme_as[1])<21:
            print("Votre main vaut ",sum(somme_as[1]) ,"et j'ai ",sum(somme_as[0]),".")
            choix(choix_option())
            return [main_croupier,main_joueur]
    if x == "arreter":
        print("Carte tirée pour le croupier : ")
        main_croupier.append(distribution())
        somme_as = asse()
        if sum(somme_as[0])==21:
            print("Blackjack ! Je remporte la main !")
            exit()
        elif sum(somme_as[0])>21:
            print("Félicitations ! Vous remportez la main car j'ai fait ",sum(somme_as[0]))
            return [main_croupier,main_joueur]
        elif sum(somme_as[0])<21:
            while sum(main_croupier) < 17:
                print("Carte tirée pour le croupier : ")
                main_croupier.append(distribution())
                somme_as = asse()
                print("Ma main vaut ",sum(somme_as[0]))
            if sum(somme_as[0])>21:
                print("Félicitations ! Vous remportez la main car j'ai fait ",sum(somme_as[0]))
                exit()
            elif sum(somme_as[0])<sum(somme_as[1]):
                print("Félicitations vous remportez la main. J'ai fait ",sum(somme_as[0]))
                exit()
            elif sum(somme_as[0])>sum(somme_as[1]):
                print("Je remporte la main en ayant fait ",sum(somme_as[0]))
                exit()
            elif sum(somme_as[0])==sum(somme_as[1]):
                print("Egalité. ")
                exit()
            return [main_croupier,main_joueur]
            
    else:
        print("Vous n'avez pas saisi une option correcte. ")
        choix(choix_option())
        return None

choix(choix_option())
