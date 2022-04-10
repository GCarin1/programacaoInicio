#Faça um programa em Python que solicite ao usuário uma quantidade de
#segundos, calcule e exiba a quantidade de horas, minutos e segundos.
class init:

    def qntH(seconds):

        seconds = seconds % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        print("Saída:")
        print(f'{hour} hora(h),{minutes} minutos(m),{seconds} segundos(s)')

    print("Entrada:") 
    n=int(input("Digite a quantidade de segundos: ")) 
    print(qntH(n))

