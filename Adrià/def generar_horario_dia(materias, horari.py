def generar_horario_dia(materias, horario_disponible):
    # Inicializar una matriz para almacenar los resultados intermedios
    dp = [[0] * 5 for _ in range(len(materias) + 1)]

    # Recorrer las materias
    for i in range(1, len(materias) + 1):
        materia = materias[i - 1]
        horas_materia = horario_disponible[materia]

        # Recorrer las horas disponibles para la materia actual
        for hora in horas_materia:
            inicio, fin = map(int, hora.split("-"))
            # Recorrer las columnas de la matriz de derecha a izquierda para evitar conflictos de horario
            for j in range(4, inicio - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - (fin - inicio)] + 1)

    # Reconstruir el horario a partir de la matriz dp
    horario = {}
    horas_asignadas = 4
    for i in range(len(materias), 0, -1):
        materia = materias[i - 1]
        horas_materia = horario_disponible[materia]
        for hora in horas_materia:
            inicio, fin = map(int, hora.split("-"))
            if dp[i][horas_asignadas] == dp[i - 1][horas_asignadas - (fin - inicio)] + 1:
                horario[materia] = hora
                horas_asignadas -= (fin - inicio)
                break

    return horario

# Definir las materias y sus horas disponibles
horario_materias = {
    "Matemáticas": ["8:00-10:00", "14:00-16:00"],
    "Historia": ["10:00-12:00", "16:00-18:00"],
    "Ciencias": ["12:00-14:00", "18:00-20:00"],
    "Literatura": ["8:00-10:00", "14:00-16:00"],
    "Física": ["10:00-12:00", "16:00-18:00"]
}

# Definir los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Generar y mostrar el horario para cada día de la semana
for dia in dias_semana:
    print(f"Horario para el día {dia}:")
    horario_dia = generar_horario_dia(list(horario_materias.keys()), horario_materias)
    for materia, hora in horario_dia.items():
        print(f"{materia}: {hora}")
    print()
