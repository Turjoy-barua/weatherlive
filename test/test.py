import random

def jeu() :
   

   
    lieux = ["sous le lit", "derrière l'oreiller", "sous la couverture", "sur l'armoire", "dans l'armoire", "sous l'armoire", "sur le placard", "dans le placard", "sous le placard", "dans le tiroir du haut", "dans le tiroir du milieu", "dans le tiroir du bas", "sur la table de chevet", "dans le tiroir de la table de chevet", "sous la table de chevet", "sur l'étagère du haut de la bibliothèque", "sur l'étagère du milieu de la bibliothèque", "sur l'étagère du bas de la bibliothèque"]
    indices = ["belle tentative ratée ! peut-être te rattraperas-tu dans l'armoire ?", "bien essayé... peut-être sous le lit tu trouveras qui sais...", "t'es vraiment pas facile toi ! essaye dans l'étagère du haut de la bibliothèque."]
    item = ["chapeau", "glaive", "flambeau", "fusil", "renard", "aspirateur", "bouclier", "elexyr mystérieux", "écureuil", "caca"]
   
    def placer_monstre(lieux) :
        placement = int(random.randint(0, len(lieux) - 1 ))
        return placement

    def trouver_item(item) :
            item_trouvé = random.randint(0, len(item) - 1)
            print(f"bravo vous avez eu un {item_trouvé} !")
            item.pop(item_trouvé)


    monstre = placer_monstre(lieux)

    print("Tu te trouves dans une mysterieuse chambre, un monstre s'y cache. Ne le trouve pas ou il te mangera.")

    lieu_fouillé=str(input("où fouilles-tu ? "))

    n=30
    m=0

    while lieu_fouillé != lieux[monstre] :
        if lieu_fouillé not in lieux :
            if m == 0 :
                n = 30
                m = 30
            elif n > 0 :
                p=random.randint(0, len(indices) - 1)
                print(p)
                print(indices[p])
                nouveaux_indices = []
                nouveaux_indices.append(indices[p])
                indices.pop(p)
                n = n - 10
            elif n == 0 :
                b=random.randint(0, len(nouveaux_indices) - 1)
                print(nouveaux_indices[b])
                indices = []
                indices.append(nouveaux_indices[b])
                nouveaux_indices.pop(b)
                m = m - 10
            else :
                print("oula")
               
        else :
            trouver_item(item)
            lieux.pop(lieu_fouillé)
        lieu_fouillé=str(input("où fouilles-tu ? "))

   
    print("voilà le monstre ! vous vous faîtes manger.")
jeu()