


class init:
    
    
    def intro(self):
        
            print("""\
                                :::!~!!!!!:.
                            .xUHWH!! !!?M88WHX:.
                            .X*#M@$!!  !X!M$$$$$$WWx:.
                        :!!!!!!?H! :!$!$$$$$$$$$$8X:
                        !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                        :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                        ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                        !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                        ~?WuxiW*`   `"#$$$$8!!!!??!!!
                        :X- M$$$$       `"T#$T~!8$WUXU~
                        :%`  ~#$$$m:        ~!~ ?$$$$$$
                    :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
            .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
            W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
            #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
            :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
            .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
            Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
            $R@i.~~ !     :   ~$$$$$B$$en:``
            ?MXT@Wx.~    :     ~"##*$$$$M~
            
            
            Aula 10 operações com string...
         """)
         
    def exemplo1(self):
        
        print("Inverter numero com variavel de espaço vazio")
        n=input("Digite um número: ")
        inversa =''
        for d in n:
            print(d)
            inversa = d +inversa
            
            
        print(inversa)
    def  exemplo2(self):
        frut=str(input("Digite uma fruta\n:"))
        
        print(frut[0:2))
    def exemplo3(self):
        fatura=float(input("Digite o faturamento R$: "))
        custo=float(input("Digite o custo R$: "))
        lucro = fatura - custo
        print( f"R${lucro:_.2f}")
    def choseexemplo(self):
        self.intro()
        
        c=int(input("Qual exemplo da aula 10 voce quer executar ? \n 1- Exemplo 01 \n 2- Exemplo 02\n:"))
    
        if(c==1):self.exemplo1()
        if(c==2):self.exemplo2()
        

        
        
start = init()
start.choseexemplo()