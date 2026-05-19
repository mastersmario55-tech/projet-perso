case_vide = " "

plateau = [case_vide for i in range(9)]

joueur = "X"

while True:
    choix_joueur = 0

    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] !=case_vide:
       choix_joueur = int(input("Entrez une case entre 1 et 9 : "))

    plateau[choix_joueur - 1] = joueur

    for i in range(9):
        print(plateau[i], end="")
        if (i + 1) % 3 == 0:
           print("")

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[0] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        print("Le joueur " + joueur + " a remporté le match !")
        break

    joueur = "O" if joueur == "X" else "X"
