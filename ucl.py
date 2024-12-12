import itertools

def inicializar_classificacao():
    equipas = {
        "Benfica": 10,
        "Monaco": 10,
        "Sporting": 10,
        "Feyenoord": 10,
        "Club Brugge": 10,
        "Real Madrid": 9,
        "Celtic": 9,
        "Manchester City": 8,
        "PSV": 8,
        "D. Zagreb": 8,
        "PSG": 7,
        "Stuttgart": 7,
        "Shakhtar": 4,
        "Sparta Prague": 4
    }

    return {equipe: {"points": pontos, "gd": 0} for equipe, pontos in equipas.items()}

def atualizar_classificacao(equipas, equipe, resultado, golos_marcados, golos_sofridos):
    equipas[equipe]["points"] += resultado[1]
    equipas[equipe]["gd"] += golos_marcados - golos_sofridos

def simular_jogo(resultado_predefinido=None):
    if resultado_predefinido:
        return resultado_predefinido

    golos1 = random.randint(0, 3)
    golos2 = random.randint(0, 3)

    if golos1 > golos2:
        return ("v", 3, golos1, golos2)
    elif golos1 < golos2:
        return ("d", 0, golos1, golos2)
    else:
        return ("e", 1, golos1, golos2)

def simular_scenario(calendario, resultados):
    equipas = inicializar_classificacao()

    for (equipe, jogos), equipe_resultados in zip(calendario.items(), resultados):
        for adversario, resultado in zip(jogos, equipe_resultados):
            atualizar_classificacao(equipas, equipe, resultado[:2], resultado[2], resultado[3])

    return sorted(equipas.items(), key=lambda x: (-x[1]["points"], -x[1]["gd"]))

def gerar_todos_cenarios(calendario):
    possibilidades_jogo = [
        ("v", 3, 1, 0),  # Vitória
        ("d", 0, 0, 1),  # Derrota
        ("e", 1, 1, 1)   # Empate
    ]

    resultados_por_equipe = [list(itertools.product(possibilidades_jogo, repeat=len(jogos))) for jogos in calendario.values()]
    return itertools.product(*resultados_por_equipe)

def calcular_percentagem_nao_passagem(calendario):
    total_cenarios = 0
    cenarios_nao_passagem = 0

    for resultados in gerar_todos_cenarios(calendario):
        total_cenarios += 1
        classificacao = simular_scenario(calendario, resultados)

        # Verificar posição do Benfica
        for i, (equipe, stats) in enumerate(classificacao, 1):
            if equipe == "Benfica" and i > 8:  # Benfica fora do top 8
                cenarios_nao_passagem += 1
                break

    percentagem = (cenarios_nao_passagem / total_cenarios) * 100
    return cenarios_nao_passagem, total_cenarios, percentagem

if __name__ == "__main__":
    calendario = {
        "Monaco": ["Aston Villa", "Inter"],
        "Sporting": ["RB Leipzig", "Bolonha"],
        "Feyenoord": ["Bayern de Munique", "Lille"],
        "Club Brugge": ["Juventus", "Manchester City"],
        "Real Madrid": ["Salzburg", "Brest"],
        "Celtic": ["Young Boys", "Brest"],
        "Manchester City": ["PSG", "Club Brugge"],
        "PSV": ["Crvena zvezda", "Liverpool"],
        "D. Zagreb": ["Arsenal", "AC Milan"],
        "PSG": ["Manchester City", "Stuttgart"],
        "Stuttgart": ["Slovan Bratislava", "PSG"],
        "Shakhtar": ["Brest", "Dortmund"],
        "Sparta Prague": ["Inter", "Leverkusen"]
    }

    cenarios_nao_passagem, total_cenarios, percentagem = calcular_percentagem_nao_passagem(calendario)

    print(f"Cenários em que o Benfica não passa: {cenarios_nao_passagem}")
    print(f"Total de cenários: {total_cenarios}")
    print(f"Percentagem de cenários em que o Benfica não passa: {percentagem:.2f}%")
