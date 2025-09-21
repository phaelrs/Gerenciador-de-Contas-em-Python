from contas import criar_banco, adicionar_conta, listar_contas, contas_proximas

def menu():
    criar_banco()
    
    while True:
        print("\n=== GERENCIADOR DE CONTAS ===")
        print("1 - Adicionar conta")
        print("2 - Listar contas")
        print("3 - Ver contas próximas do vencimento")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome da conta: ")
            valor = float(input("Valor (R$): "))
            vencimento = input("Data de vencimento (AAAA-MM-DD): ")
            adicionar_conta(nome, valor, vencimento)
            print("✅ Conta adicionada!")
        elif opc == "2":
            contas = listar_contas()
            if not contas:
                print("Nenhuma conta cadastrada.")
            else:
                for c in contas:
                    print(f"ID:{c[0]} | {c[1]} | R${c[2]:.2f} | Vence em: {c[3]}")
        elif opc == "3":
            proximas = contas_proximas()
            if proximas:
                print("⚠️ Contas próximas do vencimento:")
                for c in proximas:
                    print(f"{c[1]} - vence em {c[3]} (R${c[2]:.2f})")
            else:
                print("Nenhuma conta próxima do vencimento.")
        elif opc == "0":
            print("Saindo... até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
