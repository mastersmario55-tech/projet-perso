def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees 
salaire_annuel = float(input("Entrez votre salaire annuel : "))
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))
horaire = salaire_horaire(salaire_hebdomadaire(salaire_mensuel(salaire_annuel)), heures_travaillees)
print(f"Votre salaire horaire est de {horaire:.2f} euros.")