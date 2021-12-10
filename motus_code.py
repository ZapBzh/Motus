import random

motJoueur = input 
MotAlea = ['soleil', 'joyaux', 'cinema' , 'citron' , 'castor' , 'bonzai' , 'doutes' , 'destin' , 'pinard' , 'cypres' ]  #liste des mot possible
def selectRandom(MotAlea):
    return random.choice(MotAlea) #le programme choisit un mot au hasard

print (" Taper un mot à 6 lettre. Les lettre rouge sont bien placé. Les lettre jaunes sont presente mais mal placé. Les lettres bleu ne sont pas dans le mot.") #indiquation des consignes au joueur




def Motus(motJoueur):
    quelmot = 0
    
    for i in range(motJoueur): #quelle mot à été choisit
        if (motJoueur [i] == "soleil" ):
        quelmot+=1
        
        if (motJoueur [i] == "joyaux"):
        quelmot+=2
        
        if (motJoueur [i] == "cinema"):
        quelmot+=3
        
        if (motJoueur [i] == "citron"):
        quelmot+=4
        
        if (motJoueur [i] == "castor"):
        quelmot+=5
        
        if (motJoueur [i] == "bonzai"):
        quelmot+=6
        
        if (motJoueur [i] == "doutes"):
        quelmot+=7
        
        if (motJoueur [i] == "destin"):
        quelmot+=8
        
        if (motJoueur [i] == "pinard"):
        quelmot+=9
        
        if (motJoueur [i] == "cypres"):
        quelmot+=10




int(input) #demande au joueur de tapper son mot 
