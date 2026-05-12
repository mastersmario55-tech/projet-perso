import random


def intro_melatar():
    print("=== MELATAR: CHRONIQUES DE VESTICUL ===")
    print("Ton monde animalo-humanoide etait presque normal...")
    print("...jusqu'a ce qu'une pierre magique vous aspire.")
    print("Orguy et Gaibard tombent au Royaume de Vesticul,")
    print("un pays heroic fantasy absurde, sale et tres bureaucratique.\n")


def afficher_dialogue(lignes):
    for ligne in lignes:
        print(ligne)


def ajuster_cohesion(joueur, delta, raison):
    ancienne = joueur["cohesion"]
    joueur["cohesion"] = max(-5, min(5, joueur["cohesion"] + delta))
    if delta > 0:
        joueur["accords"] += 1
    elif delta < 0:
        joueur["desaccords"] += 1
    variation = joueur["cohesion"] - ancienne
    signe = "+" if variation >= 0 else ""
    print(
        f"Cohesion d'equipe: {ancienne} -> {joueur['cohesion']} ({signe}{variation}) [{raison}]"
    )


def afficher_journal_quete(joueur):
    allies = []
    if joueur.get("barnabe_aide", False):
        allies.append("Barnabe le sorcier")
    if joueur.get("zouzon_aide", False):
        allies.append("Zouzon Acktarr")
    if not allies:
        allies.append("Aucun allie confirme")

    indices = []
    if joueur.get("rumeur_taverne", False):
        indices.append("Rumeur de taverne sur les bandits")
    if joueur.get("barnabe_aide", False):
        indices.append("Piste des 3 fragments runiques")
    if not indices:
        indices.append("Aucun indice majeur")

    print("\n=== JOURNAL DE QUETE ===")
    print(f"Hero actif: {joueur['nom']} ({joueur['classe']})")
    print(f"Allies: {', '.join(allies)}")
    print(f"Indices: {', '.join(indices)}")
    print(f"Accords: {joueur['accords']} | Desaccords: {joueur['desaccords']}")
    print(f"Cohesion du duo: {joueur['cohesion']} (de -5 a +5)")
    print("========================")


def dialogue_arrivee_stade(joueur):
    lignes = [
        "\nOrguy: Euh... pourquoi le ciel sent la biere et la sueur ?",
        "Gaibard: Parce qu'on est dans un stade. Et il y a un troll qui vend des merguez.",
        "Orguy: On etait dans notre salon y'a 10 secondes.",
        "Gaibard: La pierre magique nous a teleporte. Reste calme.",
    ]
    if joueur["nom"] == "Orguy":
        lignes.append("Orguy: Calme ? Je suis un canard, pas un moine.")
    else:
        lignes.append("Gaibard: Respire. On observe, puis on decide.")
    afficher_dialogue(lignes)


def dialogue_choix_stade(choix):
    if choix == "1":
        afficher_dialogue(
            [
                "\nOrguy: Oui! Enfin un sport avec des coups autorises.",
                "Gaibard: Je suis presque sur que ce n'est pas le reglement...",
                "Orguy: Alors on va l'ameliorer.",
            ]
        )
        return

    afficher_dialogue(
        [
            "\nGaibard: Sortie de secours, couloir gauche. On evite le chaos.",
            "Orguy: D'accord, mais si quelqu'un nous provoque, je reponds.",
            "Gaibard: Evidemment que quelqu'un va nous provoquer.",
        ]
    )


def dialogue_sortie_stade():
    afficher_dialogue(
        [
            "\nOrguy: Bon. On est vivants. C'est deja une victoire.",
            "Gaibard: Et perdus dans un royaume inconnu. Priorite: comprendre Vesticul.",
            "Orguy: Priorite 2: trouver a manger.",
        ]
    )


def dialogue_avant_rencontre(rencontre):
    lignes = {
        1: [
            "\nGaibard: Premiere rue, premiere embuscade. Classique.",
            "Orguy: J'adore quand une ville dit bonjour avec un couteau.",
        ],
        2: [
            "\nOrguy: Je commence a croire que Vesticul taxe meme l'air.",
            "Gaibard: Oui. Et je suis sur qu'ils ont un formulaire pour respirer.",
        ],
        3: [
            "\nGaibard: Encore un effort. Ensuite, on trouve un plan pour rentrer chez nous.",
            "Orguy: Ou on prend le controle du coin. C'est aussi un plan.",
        ],
    }
    afficher_dialogue(lignes.get(rencontre, []))


def choisir_protagoniste():
    print("Choisis ton protagoniste:")
    print("1. Orguy - canard tete brulee, gros degats, moins de PV")
    print("2. Gaibard - ours au grand coeur, plus de PV, degats reguliers")
    choix = input("> ").strip()

    if choix == "1":
        return {
            "nom": "Orguy",
            "partenaire": "Gaibard",
            "classe": "Canard berserk",
            "niveau": 1,
            "hp_max": 28,
            "hp": 28,
            "atk_min": 7,
            "atk_max": 13,
            "potions": 3,
            "xp": 0,
            "or": 0,
            "eloquence": 2,
            "charisme": 4,
            "intelligence": 1,
            "barnabe_aide": False,
            "zouzon_aide": False,
            "kebab_reconfort": 0,
            "rumeur_taverne": False,
            "cohesion": 0,
            "accords": 0,
            "desaccords": 0,
        }

    return {
        "nom": "Gaibard",
        "partenaire": "Orguy",
        "classe": "Ours protecteur",
        "niveau": 1,
        "hp_max": 36,
        "hp": 36,
        "atk_min": 5,
        "atk_max": 10,
        "potions": 3,
        "xp": 0,
        "or": 0,
        "eloquence": 3,
        "charisme": 2,
        "intelligence": 3,
        "barnabe_aide": False,
        "zouzon_aide": False,
        "kebab_reconfort": 0,
        "rumeur_taverne": False,
        "cohesion": 0,
        "accords": 0,
        "desaccords": 0,
    }


def creer_ennemi(niveau):
    base = random.choice(
        [
            ("Gobelin comptable", "gobelin", 18, 5, 10),
            ("Squelette syndique", "squelette", 20, 6, 12),
            ("Loup fiscal", "loup", 22, 7, 13),
            ("Bandit poetique", "bandit", 24, 8, 14),
        ]
    )
    nom, ennemi_type, hp_base, atk_base, dc_base = base
    hp = hp_base + (niveau - 1) * 4
    atk = atk_base + (niveau - 1)
    dc = dc_base + (niveau - 1)
    return {
        "nom": nom,
        "type": ennemi_type,
        "hp_max": hp,
        "hp": hp,
        "atk": atk,
        "diplomatie_dc": dc,
    }


def creer_boss(niveau):
    hp = 38 + (niveau - 1) * 6
    atk = 9 + (niveau - 1)
    dc = 17 + (niveau - 1)
    return {
        "nom": "Controleur Supreme de Vesticul",
        "type": "boss",
        "hp_max": hp,
        "hp": hp,
        "atk": atk,
        "diplomatie_dc": dc,
    }


def ennemi_match(niveau):
    hp = 20 + (niveau - 1) * 4
    atk = 6 + (niveau - 1)
    dc = 13 + (niveau - 1)
    return {
        "nom": "Capitaine gobelin des Vesticul Bulls",
        "type": "gobelin",
        "hp_max": hp,
        "hp": hp,
        "atk": atk,
        "diplomatie_dc": dc,
    }


def ennemi_steward(niveau):
    hp = 18 + (niveau - 1) * 3
    atk = 5 + (niveau - 1)
    dc = 11 + (niveau - 1)
    return {
        "nom": "Arbitre nain furieux",
        "type": "nain",
        "hp_max": hp,
        "hp": hp,
        "atk": atk,
        "diplomatie_dc": dc,
    }


def afficher_statut(joueur, ennemi):
    print("\n" + "=" * 52)
    print(
        f"{joueur['nom']} ({joueur['classe']}) | PV: {joueur['hp']}/{joueur['hp_max']} | Potions: {joueur['potions']}"
    )
    print(
        f"Social: Eloq {joueur['eloquence']} | Cha {joueur['charisme']} | Int {joueur['intelligence']}"
    )
    print(
        f"Equipe: Cohesion {joueur['cohesion']} | Accords {joueur['accords']} | Desaccords {joueur['desaccords']}"
    )
    print(f"{ennemi['nom']} | PV: {ennemi['hp']}/{ennemi['hp_max']}")
    print("=" * 52)


def attaque_joueur(joueur, ennemi):
    bonus_cohesion = 1 if joueur.get("cohesion", 0) >= 3 else 0
    degats = (
        random.randint(joueur["atk_min"], joueur["atk_max"])
        + joueur["niveau"]
        + bonus_cohesion
    )
    ennemi["hp"] -= degats
    print(f"{joueur['nom']} frappe et inflige {degats} degats a {ennemi['nom']}.")


def capacite_speciale(joueur, ennemi):
    if joueur["nom"] == "Orguy":
        print("Orguy active 'Plongeon Furieux'.")
        degats = random.randint(10, 18) + joueur["niveau"]
        recul = random.randint(1, 4)
        ennemi["hp"] -= degats
        joueur["hp"] = max(1, joueur["hp"] - recul)
        print(f"{ennemi['nom']} prend {degats} degats. Orguy perd {recul} PV de recul.")
        return

    print("Gaibard active 'Etreinte Bienveillante'.")
    degats = random.randint(6, 11) + joueur["niveau"]
    soin = random.randint(4, 8)
    ennemi["hp"] -= degats
    joueur["hp"] = min(joueur["hp_max"], joueur["hp"] + soin)
    print(f"{ennemi['nom']} prend {degats} degats. Gaibard recupere {soin} PV.")


def utiliser_potion(joueur):
    if joueur["potions"] <= 0:
        print("Plus de potion dans le sac.")
        return
    soin = 15
    joueur["potions"] -= 1
    joueur["hp"] = min(joueur["hp_max"], joueur["hp"] + soin)
    print(f"Potion bue: +{soin} PV.")


def repliques_diplomatie(ennemi_type, succes):
    lignes = {
        "gobelin": {
            True: [
                "Tu proposes un contrat de pub pour son club.",
                "Le gobelin hesite, puis signe sur une serviette grasse.",
            ],
            False: [
                "Tu parles fair-play. Il entend 'faiblard'.",
                "Le gobelin te repond avec un tacle a hauteur de tete.",
            ],
        },
        "nain": {
            True: [
                "Tu reconnais l'autorite de l'arbitre et critiques le VAR.",
                "Le nain approuve et te laisse passer contre une poignee de main.",
            ],
            False: [
                "Tu contestes une decision d'arbitrage vieille de 20 ans.",
                "Le nain voit rouge. Tres rouge.",
            ],
        },
        "squelette": {
            True: [
                "Tu offres de classer ses dossiers par ordre alphabetique.",
                "Le squelette soupire et accepte une treve administrative.",
            ],
            False: [
                "Tu promets de simplifier la paperasse.",
                "Le squelette te montre un formulaire de 87 pages pour mentir.",
            ],
        },
        "loup": {
            True: [
                "Tu expliques un montage fiscal legal mais ennuyeux.",
                "Le loup fiscal perd l'envie de mordre et prend des notes.",
            ],
            False: [
                "Tu dis 'taxe carbone' sans preparer ton argumentaire.",
                "Le loup grogne: 'Controle surprise.'",
            ],
        },
        "bandit": {
            True: [
                "Tu complimentes sa poesie et proposes un recital payant.",
                "Le bandit poetique range sa dague et demande des rimes.",
            ],
            False: [
                "Tu corriges sa metrique au mauvais moment.",
                "Le bandit crie 'c'est de l'art!' puis attaque.",
            ],
        },
        "boss": {
            True: [
                "Tu arrives avec dossier, cachet et 3 copies certifiees.",
                "Le Controleur Supreme declare: 'Procedure validee. Circulez.'",
            ],
            False: [
                "Tu as oublie le formulaire B-12 annexe tripliquee.",
                "Le Controleur Supreme sonne la cloche des sanctions immediates.",
            ],
        },
        "default": {
            True: [
                "Tu trouves les mots justes.",
                "Ton adversaire accepte de negocier.",
            ],
            False: [
                "Ton discours manque de conviction.",
                "L'adversaire reste hostile.",
            ],
        },
    }
    bloc = lignes.get(ennemi_type, lignes["default"])
    return bloc[succes]


def tenter_diplomatie(joueur, ennemi):
    base = random.randint(1, 12)
    score = (
        base
        + joueur["eloquence"]
        + joueur["charisme"]
        + (joueur["intelligence"] // 2)
        + joueur["niveau"]
    )
    if joueur.get("cohesion", 0) >= 2:
        score += 1
    elif joueur.get("cohesion", 0) <= -2:
        score -= 1
    difficulte = ennemi.get("diplomatie_dc", 12)
    ennemi_type = ennemi.get("type", "default")

    print(
        f"Tu tentes la diplomatie... (score {score} vs difficulte {difficulte})"
    )
    if score >= difficulte:
        afficher_dialogue(repliques_diplomatie(ennemi_type, True))
        print(f"{ennemi['nom']} baisse les armes apres discussion.")
        return True

    afficher_dialogue(repliques_diplomatie(ennemi_type, False))
    print(f"{ennemi['nom']} n'est pas convaincu et reste hostile.")
    return False


def tour_joueur(joueur, ennemi):
    print("\nAction:")
    print("1. Attaquer")
    print("2. Capacite speciale")
    print("3. Boire une potion")
    print("4. Fuir")
    print("5. Dialoguer (diplomatie)")
    choix = input("> ").strip()

    if choix == "1":
        attaque_joueur(joueur, ennemi)
        return "continuer"
    if choix == "2":
        capacite_speciale(joueur, ennemi)
        return "continuer"
    if choix == "3":
        utiliser_potion(joueur)
        return "continuer"
    if choix == "4":
        chance = 0.6 if joueur["nom"] == "Orguy" else 0.45
        if random.random() < chance:
            print("Fuite reussie.")
            return "fuite"
        print("Fuite ratee.")
        return "continuer"
    if choix == "5":
        if tenter_diplomatie(joueur, ennemi):
            return "resolution"
        return "continuer"

    print("Choix invalide.")
    return "continuer"


def tour_ennemi(joueur, ennemi):
    degats = random.randint(max(1, ennemi["atk"] - 2), ennemi["atk"] + 2)
    if joueur.get("cohesion", 0) <= -3:
        degats += 1
        print("Le duo se dispute: l'ennemi profite de l'ouverture (+1 degat).")
    joueur["hp"] -= degats
    print(f"{ennemi['nom']} attaque et inflige {degats} degats.")
    if joueur["hp"] <= 0 and joueur.get("kebab_reconfort", 0) > 0:
        joueur["kebab_reconfort"] -= 1
        joueur["hp"] = 14
        print("Le Kebab de Zouzon te sauve in extremis: +14 PV.")


def scene_cite_imperiale(joueur):
    print("\n=== CHAPITRE 1: LA CITE IMPERIALE ===")
    print("Apres le stade, Orguy et Gaibard rejoignent la Cite Imperiale de Vesticul.")
    print("Devant vous: le Sanctuaire du Savoir... et tout un quartier tres louche.")

    visites = {
        "sanctuaire": False,
        "ville": False,
        "taverne": False,
        "kebab": False,
    }

    while True:
        print("\nQue faire ?")
        print("1. Aller au Sanctuaire du Savoir (Barnabe le sorcier)")
        print("2. Se balader en ville (boutiques)")
        print("3. Entrer dans une taverne au pif")
        print("4. Manger au 'Zouzon Kebab'")
        print("5. Conseil du duo (accords/desaccords)")
        print("6. Ouvrir le journal de quete")
        print("7. Quitter la cite et poursuivre la quete")
        choix = input("> ").strip()

        if choix == "1":
            if visites["sanctuaire"]:
                print("Barnabe t'a deja donne ses conseils.")
                continue
            visites["sanctuaire"] = True
            print("\nAu Sanctuaire, Barnabe le sorcier vous accueille.")
            afficher_dialogue(
                [
                    "Barnabe: Vous venez d'un autre monde? Classique, ici.",
                    "Gaibard: Vous pouvez nous aider a rentrer?",
                    "Barnabe: Peut-etre. Il vous faut trois fragments runiques.",
                    "Orguy: Et bien sur, c'est dangereux.",
                    "Barnabe: Evidemment.",
                ]
            )
            joueur["barnabe_aide"] = True
            joueur["intelligence"] += 1
            joueur["eloquence"] += 1
            joueur["potions"] += 1
            ajuster_cohesion(joueur, +1, "Le duo suit le conseil de Barnabe")
            print("Barnabe vous booste: +1 Intelligence, +1 Eloquence, +1 potion.")
            continue

        if choix == "2":
            if visites["ville"]:
                print("Tu as deja fait le tour des boutiques pour aujourd'hui.")
                continue
            visites["ville"] = True
            print("\nVous flanez entre armuriers hors de prix et marchands douteux.")
            gain_or = random.randint(4, 10)
            joueur["or"] += gain_or
            if random.random() < 0.5:
                joueur["potions"] += 1
                print(f"Vous revendez des babioles: +{gain_or} or et +1 potion.")
            else:
                print(f"Vous revendez des babioles: +{gain_or} or.")
            continue

        if choix == "3":
            if visites["taverne"]:
                print("La taverne est deja videe. Plus rien a y gratter.")
                continue
            visites["taverne"] = True
            print("\nDans la taverne, un ancien garde vous file des infos utiles.")
            joueur["hp"] = joueur["hp_max"]
            joueur["rumeur_taverne"] = True
            ajuster_cohesion(joueur, +1, "Le duo partage les infos de terrain")
            print("Vous recuperes tous vos PV et obtenez un tuyau sur les bandits locaux.")
            continue

        if choix == "4":
            if visites["kebab"]:
                print("Zouzon vous salue: 'Revenez apres la quete, les amis.'")
                continue
            visites["kebab"] = True
            print("\nBienvenue au 'Zouzon Kebab'!")
            afficher_dialogue(
                [
                    "Zouzon Acktarr: Ici, on nourrit les heros... et on les equipe.",
                    "Orguy: Enfin un professionnel serieux.",
                    "Gaibard: Vous connaissez Barnabe?",
                    "Zouzon: On a fait l'armee ensemble. Dites-lui bonjour.",
                ]
            )
            joueur["zouzon_aide"] = True
            joueur["charisme"] += 1
            joueur["kebab_reconfort"] += 1
            ajuster_cohesion(joueur, +1, "Repas strategique chez Zouzon")
            print("Bonus de Zouzon: +1 Charisme et 1 Kebab de secours (rez en combat).")
            continue

        if choix == "5":
            print("\nConseil du duo: quelle approche prendre ?")
            print("1. Plan prudent de Gaibard (infos et tactique)")
            print("2. Plan explosif d'Orguy (action immediate)")
            print("3. Compromis: infiltration puis action")
            sous_choix = input("> ").strip()
            if sous_choix == "1":
                joueur["intelligence"] += 1
                ajuster_cohesion(joueur, +1, "Plan de Gaibard retenu")
                print("+1 Intelligence.")
                continue
            if sous_choix == "2":
                joueur["atk_min"] += 1
                joueur["atk_max"] += 1
                ajuster_cohesion(joueur, -1, "Plan d'Orguy impose")
                print("Attaque +1/+1.")
                continue
            if sous_choix == "3":
                joueur["eloquence"] += 1
                ajuster_cohesion(joueur, +2, "Compromis accepte")
                print("+1 Eloquence.")
                continue
            print("Choix invalide.")
            continue

        if choix == "6":
            afficher_journal_quete(joueur)
            continue

        if choix == "7":
            if not visites["sanctuaire"] and not visites["kebab"]:
                print("Vous partez sans allies. C'est un choix... audacieux.")
            else:
                print("Vous quittez la Cite Imperiale mieux prepares.")
            return

        print("Choix invalide.")


def attribuer_points_sociaux(joueur, points=2):
    print(f"\nTu gagnes {points} points de competences sociales.")
    for _ in range(points):
        while True:
            print("Ou placer 1 point ?")
            print("1. Eloquence")
            print("2. Charisme")
            print("3. Intelligence")
            choix = input("> ").strip()
            if choix == "1":
                joueur["eloquence"] += 1
                break
            if choix == "2":
                joueur["charisme"] += 1
                break
            if choix == "3":
                joueur["intelligence"] += 1
                break
            print("Choix invalide.")

    print(
        f"Nouvelles stats sociales: Eloq {joueur['eloquence']} | Cha {joueur['charisme']} | Int {joueur['intelligence']}"
    )


def gain_victoire(joueur, boss=False, diplomatique=False):
    if boss:
        xp = random.randint(18, 26)
        or_gagne = random.randint(14, 24)
    elif diplomatique:
        xp = random.randint(9, 14)
        or_gagne = random.randint(8, 15)
    else:
        xp = random.randint(10, 16)
        or_gagne = random.randint(6, 14)

    joueur["xp"] += xp
    joueur["or"] += or_gagne
    if diplomatique:
        print(f"\nResolution pacifique! +{xp} XP, +{or_gagne} or.")
    else:
        print(f"\nVictoire! +{xp} XP, +{or_gagne} or.")

    seuil = joueur["niveau"] * 22
    while joueur["xp"] >= seuil:
        joueur["xp"] -= seuil
        joueur["niveau"] += 1
        joueur["hp_max"] += 5
        joueur["hp"] = joueur["hp_max"]
        joueur["atk_min"] += 1
        joueur["atk_max"] += 1
        print(f"Niveau superieur! {joueur['nom']} passe niveau {joueur['niveau']}.")
        attribuer_points_sociaux(joueur, points=2)
        seuil = joueur["niveau"] * 22


def combat(joueur, ennemi):
    while ennemi["hp"] > 0 and joueur["hp"] > 0:
        afficher_statut(joueur, ennemi)
        resultat = tour_joueur(joueur, ennemi)

        if resultat == "fuite":
            return "fuite"
        if resultat == "resolution":
            return "victoire_diplomatique"

        if ennemi["hp"] > 0:
            tour_ennemi(joueur, ennemi)

    if joueur["hp"] <= 0:
        return "defaite"
    return "victoire"


def scene_stade(joueur):
    print("\n=== PROLOGUE: STADE DES DEUX TRIBUNES ===")
    print("Orguy et Gaibard apparaissent en plein stade de foot.")
    print("Match en cours: Gobelins FC contre Nains Athletico.")
    print("La foule hurle: 'Des nouveaux! Faites-les jouer!'\n")
    dialogue_arrivee_stade(joueur)

    while True:
        print("Choix:")
        print("1. Participer au match")
        print("2. Chercher une sortie pour eviter les ennuis")
        choix = input("> ").strip()

        if choix == "1":
            dialogue_choix_stade(choix)
            print("\nTu entres sur la pelouse... ca devient vite un combat de rue.")
            resultat = combat(joueur, ennemi_match(joueur["niveau"]))
            if resultat == "defaite":
                return "defaite"
            if resultat == "fuite":
                print("Tu quittes le terrain sous les sifflets.")
                return "fuite"

            print("Le public adore. Un sponsor douteux te lance une bourse.")
            gain_victoire(joueur, diplomatique=(resultat == "victoire_diplomatique"))
            joueur["or"] += 8
            print("+8 or bonus de prime de match.")
            return "ok"

        if choix == "2":
            dialogue_choix_stade(choix)
            print("\nVous longez les couloirs pour trouver une sortie de secours...")
            if random.random() < 0.6:
                joueur["potions"] += 1
                print("Sortie trouvee sans bruit. Un vendeur te file 1 potion gratuite.")
                return "ok"

            print("Rate: un arbitre nain vous repere et charge.")
            resultat = combat(joueur, ennemi_steward(joueur["niveau"]))
            if resultat == "defaite":
                return "defaite"
            if resultat == "fuite":
                print("Vous fuyez enfin hors du stade.")
                return "fuite"

            print("Vous neutralisez l'arbitre et filez vers Vesticul.")
            gain_victoire(joueur, diplomatique=(resultat == "victoire_diplomatique"))
            return "ok"

        print("Choix invalide.")


def lancer_jeu():
    intro_melatar()
    joueur = choisir_protagoniste()

    resultat_prologue = scene_stade(joueur)
    if resultat_prologue == "defaite":
        print("\nFin precoce: vous vous faites sortir du stade sur civiere.")
        print(f"Niveau atteint: {joueur['niveau']} | Or: {joueur['or']}")
        return
    if resultat_prologue == "fuite":
        print("\nVous echappez au chaos du stade et reprenez votre souffle.")
        return

    dialogue_sortie_stade()
    scene_cite_imperiale(joueur)
    afficher_journal_quete(joueur)
    print(f"\n{joueur['nom']} entre dans les rues tordues de Vesticul.")
    print("Objectif: survivre ou negocier pendant 3 rencontres puis affronter le boss.\n")

    rencontre = 1
    while rencontre <= 3 and joueur["hp"] > 0:
        dialogue_avant_rencontre(rencontre)
        ennemi = creer_ennemi(joueur["niveau"])
        if rencontre == 1 and joueur.get("rumeur_taverne", False):
            ennemi["diplomatie_dc"] = max(8, ennemi["diplomatie_dc"] - 2)
            print("Grace aux infos de taverne, tu sais comment parler a cet ennemi.")
        print(f"--- Rencontre {rencontre}: {ennemi['nom']} ---")
        resultat = combat(joueur, ennemi)

        if resultat == "fuite":
            print("Tu evites le combat et te caches dans une taverne.")
            return
        if resultat == "defaite":
            break

        gain_victoire(joueur, diplomatique=(resultat == "victoire_diplomatique"))
        if rencontre % 2 == 0:
            joueur["potions"] += 1
            print("Un marchand louche te donne 1 potion en promotion douteuse.")

        if rencontre < 3:
            continuer = input("\nContinuer vers la prochaine zone ? (o/n): ").strip().lower()
            if continuer != "o":
                print("Tu quittes Vesticul pour aujourd'hui.")
                return
        rencontre += 1

    if joueur["hp"] <= 0:
        print("\nTu es tombe au combat. Melatar devra attendre.")
        print(f"Niveau atteint: {joueur['niveau']} | Or: {joueur['or']}")
        return

    print("\n=== BOSS: Le Controleur Supreme de Vesticul ===")
    boss = creer_boss(joueur["niveau"])
    if joueur.get("barnabe_aide", False):
        boss["diplomatie_dc"] = max(10, boss["diplomatie_dc"] - 2)
        print("Les conseils de Barnabe t'aident face a la bureaucratie supreme.")
    resultat_boss = combat(joueur, boss)

    if resultat_boss == "defaite":
        print("\nLe Controleur te fait remplir des formulaires jusqu'a l'epuisement...")
        print(f"Niveau atteint: {joueur['niveau']} | Or: {joueur['or']}")
        return
    if resultat_boss == "fuite":
        print("\nTu fuis devant la paperasse sacree. Fin de chapitre.")
        return

    gain_victoire(joueur, boss=True, diplomatique=(resultat_boss == "victoire_diplomatique"))
    print("\nVictoire du duo legendaire!")
    print("Orguy et Gaibard gardent la pierre magique, pour l'instant...")
    print(f"Stat final: Niveau {joueur['niveau']} | Or: {joueur['or']} | PV: {joueur['hp']}")


if __name__ == "__main__":
    lancer_jeu()

