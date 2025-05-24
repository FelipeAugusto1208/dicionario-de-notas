#codigo dicionario de alunos
alunos = {"João Victor dos Santos Moura": {"Matemática": [8.7, 9.0],
                                           "Português": [9.0, 10.0],
                                           "História": [7.5, 7.0],
                                           "Inglês": [8.0, 6.5],
                                           "Educação Física": [10.0, 10.0]},
         "Cesar Henrique Brum Da Costa": {"Matemática": [4.9, 8.0],
                                           "Português": [7.0, 9.0],
                                           "História": [5.0, 7.0],
                                           "Inglês": [3.0, 8.5],
                                           "Educação Física": [10.0, 10.0]},
         "Felipe Augusto Rocha":        {"Matemática": [10.0, 9.5],
                                           "Português": [8.0, 9.0],
                                           "História": [7.0, 6.0],
                                           "Inglês": [4.1, 7.6],
                                           "Educação Física": [8.0, 9.7]}}


def media_por_aluno():
     for nome, materias in alunos.items():
          print(f"Aluno: {nome}")
          for materia, notas in materias.items():
               media = sum(notas) / len(notas)
               print(f"{materia}: Média = {media:.2f}")



def media_geral_dos_alunos():
      for nome, materias in alunos.items():
        soma_notas = 0
        total_notas = 0
        print(f"Aluno: {nome}")
        for materia, notas in materias.items():
            soma_notas += sum(notas)
            total_notas += len(notas)
        media_geral = soma_notas / total_notas
        print(f"Média geral: {media_geral:.2f}")


def media_turma_por_disciplina():
    soma_por_disciplina = {}
    contador_por_disciplina = {}

    for materias in alunos.values():
        for disciplina, notas in materias.items():
            if disciplina not in soma_por_disciplina:
                soma_por_disciplina[disciplina] = 0
                contador_por_disciplina[disciplina] = 0
            soma_por_disciplina[disciplina] += sum(notas)
            contador_por_disciplina[disciplina] += len(notas)

    print("Média da turma por disciplina:")
    for disciplina in soma_por_disciplina:
        media = soma_por_disciplina[disciplina] / contador_por_disciplina[disciplina]
        print(f"{disciplina}: {media:.2f}")


def alterar_nota():
    nome_aluno = input("Digite o nome completo do aluno: ")
    if nome_aluno not in alunos:
        print("Aluno não encontrado.")
        return

    disciplinas = alunos[nome_aluno]
    print("Disciplinas disponíveis:", ", ".join(disciplinas.keys()))
    disciplina = input("Digite a disciplina: ")
    if disciplina not in disciplinas:
        print("Disciplina não encontrada para este aluno.")
        return

    print(f"Notas atuais de {disciplina}: {disciplinas[disciplina]}")
    try:
        indice = int(input("Qual nota deseja alterar? (0 para primeira, 1 para segunda): "))
        if indice not in [0, 1]:
            print("Índice inválido. Use 0 ou 1.")
            return
        nova_nota = float(input("Digite a nova nota: "))
        disciplinas[disciplina][indice] = nova_nota
        print("Nota atualizada com sucesso.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números corretamente.")

def menu():
    while True:
        print("Menu:")
        print("1 - Mostrar média por aluno")
        print("2 - Mostrar média geral dos alunos")
        print("3 - Mostrar média da turma por disciplina")
        print("4 - Alterar nota de um aluno")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            media_por_aluno()
        elif escolha == "2":
            media_geral_dos_alunos()
        elif escolha == "3":
            media_turma_por_disciplina()
        elif escolha == "4":
            alterar_nota()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()