#f=open('train.csv',"r")
#list=f.readlines()
#f.close()

#count=0
#male=0
#female=0
#k=[]
#for i in range(1,len(list)):
#    k=list[i].strip().split(",")
#    if k[1]=='1' and k[5]=='male':
#        male+=1
#    if k[1]=='1' and k[5]=='female':
#        female+=1
#count=female+male
#print('число выживших-',count,'число выживших женщин-',female,'число выживших мужчин-',male)


#ПЕРЕВОДЧИК
#eng_morze_dict={'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
#      'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
#        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ':' '}
#n=input()
#perevod=[]
#for value in n:
#    perevod.append(eng_morze_dict[value])
#print(perevod)