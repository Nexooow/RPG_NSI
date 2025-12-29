from .Action import Action

from .AjoutItems import AjoutItems
from .AjoutTemps import AjoutTemps
from .Boutique import Boutique
from .Combat import Combat
from .Damage import Damage
from .Deplacement import Deplacement
from .Dialogue import Dialogue
from .RandomAction import RandomAction
from .Selection import Selection
from .SelectionAction import SelectionAction

actions_par_type = {
    "ajout-items": AjoutItems,
    "ajout-temps": AjoutTemps,
    "boutique": Boutique,
    "combat": Combat,
    "damage": Damage,
    "deplacement": Deplacement,
    "dialogue": Dialogue,
    "random": RandomAction,
    "select": SelectionAction,
    "selection-action": SelectionAction
}
