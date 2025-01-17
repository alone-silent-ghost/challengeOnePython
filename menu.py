# menu.py
import experiment
import analysis
import report

experiments = []

def show_menu():
    print("\nMenú de opciones:")
    print("1. Agregar experimento")
    print("2. Ver experimentos")
    print("3. Analizar resultados")
    print("4. Generar informe")
    print("5. Salir")
    return int(input("Seleccione una opción: "))

def add_experiment():
    name = input("Nombre del experimento: ")
    date = input("Fecha de realización (DD/MM/AAAA): ")
    exp_type = input("Tipo de experimento (Química/Biología/Física): ")
    results = list(map(float, input("Resultados (separados por comas): ").split(',')))
    exp = experiment.Experiment(name, date, exp_type, results)
    experiments.append(exp)
    print("Experimento agregado exitosamente.")

def view_experiments():
    for exp in experiments:
        exp.display()

def analyze_experiment():
    name = input("Ingrese el nombre del experimento a analizar: ")
    for exp in experiments:
        if exp.name == name:
            analysis.perform_analysis(exp)
            return
    print("Experimento no encontrado.")

def generate_report():
    report.generate(experiments)
