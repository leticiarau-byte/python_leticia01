#=====================================
# Calculadora em python 
# Operações Básicas 
# ====================================

print("\n---calculadora da Letícia--- ")


def soma(a,b) :
    return  a + b 

def subtracao (a,b) : 
    return a-b

def multiplicacao(a, b) : 
        return a*b
def divisao(a, b) : 
    if b == 0: 
        return "Divisão 0 "
    else: 
        return a/b 
   

opcao = 1
while opcao!=0: 
    
    
    print("\n---calculando--- ")

    opcao = int(input("Digite o que desejar: \n1-soma \n2-multiplicação \n3-divisão \n4-subtração\n0-Sair\n")) 
    
    if opcao != 0 :
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("\nDigite o segundo número: "))

        if opcao == 1: 
            resultado = soma(num1, num2)
            print(f"\nSOMA: Resultado: {resultado}\n")
        
        elif opcao == 2: 
            resultado = multiplicacao(num1, num2)
            print(f"\nMULTIPLICAÇÃO: Resultado: {resultado}\n")
        
        elif opcao == 3: 
            resultado = divisao(num1, num2)
            print(f"\nDIVISÃO: Resultado: {resultado}\n")
        
        elif opcao == 4: 
            resultado = subtracao(num1, num2)
            print(f"\nSUBTRAÇÃO: Resultado: {resultado}\n")   
    else : 
        print("SISTEMA FINALIZADO")
        