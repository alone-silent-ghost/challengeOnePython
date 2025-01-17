# report.py
def generate(experiments):
    with open("informe.txt", "w") as f:
        for exp in experiments:
            f.write(f"Nombre: {exp.name}, Fecha: {exp.date}, Tipo: {exp.exp_type}, Resultados: {exp.results}\n")
            avg = sum(exp.results) / len(exp.results)
            max_result = max(exp.results)
            min_result = min(exp.results)
            f.write(f"Promedio: {avg}, Máximo: {max_result}, Mínimo: {min_result}\n\n")
    print("Informe generado exitosamente en 'informe.txt'.")
