from .Action import Action


class Condition(Action):

    def __init__(self, jeu, data):
        super().__init__(jeu, data)

    def executer(self):
        super().executer()
        result = eval(self.data.get("condition", False), {
            "jeu": self.jeu,
        })
        if self.data["type-condition"] == "if" and result:
            self.complete = True
