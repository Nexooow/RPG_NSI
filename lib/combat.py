"""
Module de gestion des effets en combat.
(Ce module est séparé pour éviter les importations circulaires.)
"""
import random


def add_effets(cible, effets: dict):
    """
    Ajoute des effets à une cible (personnage, monstre, etc.).
    """
    for nom, (niveau, duree) in effets.items():
        if nom in cible["effets"]:
            if nom == "brulure":
                # pour 'brulure' on incrémente le niveau au lieu de prendre le max
                cible["effets"][nom][0] += niveau
            else:
                cible["effets"][nom][0] = max(cible["effets"][nom][0], niveau)
            if duree == -1 or cible["effets"][nom][1] == -1:  # -1 correspond à une durée infinie
                cible["effets"][nom][1] = -1
            else:
                cible["effets"][nom][1] = max(cible["effets"][nom][1], duree)
        else:
            cible["effets"][nom] = [niveau, duree]


def calcul_degats(attaquant, cible):
    """
    Calcule les dégâts infligés par un attaquant à une cible.
    Prend en compte l'arme, les attributs, les coups critiques et les effets
    """
    arme = attaquant.get("arme")
    if arme is None:
        arme = {
            "degats": 1,
            "critique": 5
        }
    degats = arme.get("degats", 1) + attaquant["attributs"].get("force", 1)

    # Effet d'alcoolemie : augmente les dégâts infligés
    if "alcoolemie" in attaquant.get("effets", {}) and attaquant["type"] == "personnage":
        niveau_alcoolemie = attaquant["effets"]["alcoolemie"][0]
        degats *= 1 + (niveau_alcoolemie * 0.1)  # +10% dégâts par niveau

    # Coup critique
    crit = arme.get("critique", 5) + attaquant["attributs"].get("chance", 1) > random.randint(1, 100)
    if crit:
        degats *= 2

    effets_cible = cible.get("effets", {})

    # Effet de vulnérabilité : augmente les dégâts subis
    if "vulnerabilite" in effets_cible:
        niveau_vulnerabilite = cible["effets"]["vulnerabilite"][0]
        degats *= 1 + (niveau_vulnerabilite * 0.2)  # +20% dégâts subis par niveau
    if "reduction_degats" in effets_cible:
        niveau_reduction = cible["effets"]["reduction_degats"][0]
        degats *= max(0, 1 - (niveau_reduction * 0.15))  # -15% dégâts subis par niveau
    if "invulnerabilite_physique" in effets_cible:
        degats = 0

    if "saignement" in effets_cible:
        # plus la vie est basse, plus le saignement fait de dégâts
        degats += cible["max_vie"] * (effets_cible["saignement"][0] * 0.05) * (1 - (cible["vie"] / cible["max_vie"]))

    if "marque" in effets_cible:
        degats *= 1.5
        del cible["effets"]["marque"]

    return degats
