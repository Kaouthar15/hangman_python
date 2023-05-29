import random
from art import tprint
aff="" 
lettre=''
s='oui'
print('\t')   
tprint('\t \t     Bienvenue')      
while s!='non':   
  lettre='' 
  aff=''      
  print('''        
         
                    \033[1;33;40mＬｅｓ Ｃａｔéｇｏｒｉｅｓ\033[32m      
                              
                                  °
                                 ( )
                                (   )
                               (     )
                              (       ) 
                             (         )
                            (  1-Pays   ) 
                           (   2-Corps   )
                          (    3-Fruit    ) 
                         (    4-Animaux    )  
                        (    5-Fast-Food    ) 
                       (________      _______)\033[33m 
                                ||||||
                                ||||||
                                ||||||\033[30m     
        ''')
  d= {1:['algerie', 'egypte', 'maroc', 'tunisie', 'libye', 'soudan', 'syrie', 'liban', 'uae', 'qatar', 'bahrein', 'oman', 'irak', 'yemen'],
      2:['cerveau', 'coeur', 'poumons', 'foie', 'reins', 'estomac', 'nez', 'sourcils', 'veines', 'bouche', 'yeux', 'muscles', 'os', 'genoux', 'peau'],
      3:['pomme', 'banane', 'orange', 'cerise', 'fraise', 'peche', 'ananas', 'mangue', 'grenade', 'litchi', 'kiwi', 'avocat', 'citron'],
      4:['lion', 'tigre', 'elephant', 'girafe', 'zebre',  'croco', 'aigle', 'ours', 'chien', 'chat', 'souris', 'singe', 'gorille', 'leopard'],
      5:['hamburger', 'poulet', 'sandwich', 'pizza', 'tacos', 'donuts', 'frites', 'poisson', 'nuggets', 'hotdog', 'wraps']}  

  la_catégorie=int(input('''
                        
                      ----------------------------                            
                      | Entrez votre catégorie : |
                      ---------------------------- 
            
                        ''')) 
  L=d[la_catégorie] 
  mot_à_deviner=random.choice(L) 
  #print(mot_à_deviner)     
  for i in mot_à_deviner :  
    aff+= "_ "     
  essaie=7 
  while essaie>0: 
    print('Mots à deviner : ', aff) 
    devination = input('Entrez un lettre : ').lower() 
    if devination in mot_à_deviner:
      lettre+=devination 
      print('\033[32m\nＢｏｎ ｃｈｏｉｘ :)\n')     
    else : 
      essaie-=1
      print('\033[31m\nＭａｕｖａｉｓ ｃｈｏｉｘ :( \n')   
      if essaie < 7:    
        print('===========Y==')  
      if essaie <6:
        print('||/        | ')
      if essaie <5:
        print('||         O  ')
      if essaie <4:
        print('||        /|\  ')
      if essaie <3 :
        print('||       _/ \_   ') 
      if essaie <2 : 
        print('||             ')
      if essaie <1 :   
        print('''===============''')
        tprint ('\nPERDU\n')
        print(f'Le mot était :{mot_à_deviner}\n')
                      
    aff = ""  
    for j in mot_à_deviner: 
        if j in lettre: 
            aff += j + " "    
        else:
            aff += "_ "     
    if "_" not in aff: 
      tprint("\n Felicitation") 
      break
  s=input('\033[33m Voulez vous rejouer? (oui/non) :').lower()    


  

  
    

  
  




