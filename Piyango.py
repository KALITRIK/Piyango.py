from random import randint

Başla = True

while Başla:

    bir = randint(0,1000)
    iki = randint(0,1000)
    üç = randint(0,1000)
    dört = randint(0,1000)
    beş = randint(0,1000)

    Tebrik = []
    IphoneX = []

    Tebrik.append(bir)
    Tebrik.append(iki)
    Tebrik.append(üç)
    Tebrik.append(dört)
    IphoneX.append(beş)

    print("Asıl ödülü kazanmak için tahmin edilmesi gereken sayılar: ", Tebrik)
    print("Asıl ödülü kazanmak için tahmin edilmesi gereken sayı: ", IphoneX)
    input("Başlamak için Enter'e Bas!")

    while True:
        ab = randint(0,1000)
        print(ab)
    
        if ab in Tebrik:
            print("TEBRİKLER! Ödülüne daha da yaklaştın!")
            input("İlerlemek için Enter'e Bas!")
        
            if ab == ab:
                Tebrik.remove(ab)
        
        if Tebrik == []:    
        
            if ab in IphoneX:
                print("Yakışır koçuma IphoneX kazandın.")
                if ab == ab:
                    IphoneX.remove(ab)
                
                başlayak = input("Yeniden başlayalım mı? (Y/N)")
                if başlayak == "Y":
                    Başla = True
                
                if başlayak == "N":
                    Başla = False  
                    
        if (Tebrik) == []:
            if(IphoneX) == []:
                break
                

        
    
    

input("Çıkmak için Enter'e Basınız!")
