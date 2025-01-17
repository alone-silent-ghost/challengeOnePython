# analysis.py
def perform_analysis(experiment):
    avg = sum(experiment.results) / len(experiment.results)
    max_result = max(experiment.results)
    min_result = min(experiment.results)
    print(f"Análisis del experimento {experiment.name}:")
    print(f"Promedio: {avg}")
    print(f"Máximo: {max_result}")
    print(f"Mínimo: {min_result}")
