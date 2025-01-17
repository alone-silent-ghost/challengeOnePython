# experiment.py
class Experiment:
    def __init__(self, name, date, exp_type, results):
        self.name = name
        self.date = date
        self.exp_type = exp_type
        self.results = results

    def display(self):
        print(f"Nombre: {self.name}, Fecha: {self.date}, Tipo: {self.exp_type}, Resultados: {self.results}")
