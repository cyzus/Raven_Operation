def create_dict(words):
    dict={}
    dict2=[]
    for word in words:
        try:
            dict[word]+=1
        except:
            dict[word]=1
    for word in dict:
        dict2.append((word,dict[word]))
    return dict2

def import_email(spamnumber,ifspam,num_of_feature):
    allword=[]
    for n in range(1,400):
        if ifspam:
            link='Spam/Spam'+str(spamnumber)+'/'+str(n)+'.txt'
        else:
            link='Normalset/'+str(n)+'.txt'
        try:
            with open(link,'r') as email:
                for sentence in email:
                    word=[]
                    for letter in sentence:
                        if letter!=' ':
                            word.append(letter)
                        else:
                            word="".join(word)
                            allword.append(word)
                            word=[]
        except:
            pass
    eliminate_word=[""]
    with open('eliminate_word.txt','r') as elimination:
        for word in elimination:
            word = word.replace("\t\n","")
            word = word.replace("\t", "")
            word = word.replace("\t\t", "")
            word = word.replace("\n", "")
            eliminate_word.append(word)
    for index in range(len(allword)):
        if allword[index] in eliminate_word:
            allword[index] = '999'
        if len(allword[index])==1:
            allword[index] = '999'
    while True:
        try:
            allword.remove('999')
        except:
            break
    dict = sorted(create_dict(allword), key=lambda k: k[-1],reverse=True)
    feature=[]
    for i in range(num_of_feature):
        feature.append(dict[i])
    return feature



