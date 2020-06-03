import csv

allScores=[]

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

#open the file, remove identifiers, return the values 
def readFile(fileName):
    with open(fileName) as csvfile:
        traitValues=[]
        readCSV = csv.reader(csvfile,  delimiter=',')
        for row in readCSV:
            traitValues.append(row[1:41])
            passwords.append(row[0])
        traitValues.remove(traitValues[0]) 
        traitValues.remove(traitValues[0])

        for row in range(0,len(traitValues)):
            for vals in range(0,len(traitValues[row])):
                if traitValues[row][vals]=='':
                    traitValues[row][vals]=0
                traitValues[row][vals]=int(traitValues[row][vals])
        
    return traitValues

#returns the dictionary for each password            
def createDictionary(traitValues):           

    dict = {"Bold": traitValues[0], "Envious": traitValues[1], "Cooperative": traitValues[2], "Unenvious": traitValues[3], "Sympathetic": traitValues[4], "Intellectual": traitValues[5],
                   "Philosophical": traitValues[6], "Energetic": traitValues[7], "Rude": traitValues[8], "Practical": traitValues[9], "Imaginative": traitValues[10], "Warm": traitValues[11], "Deep": traitValues[12],
                   "Sloppy": traitValues[13], "Unintellectual": traitValues[14], "Moody": traitValues[15], "Fretful": traitValues[16], "Quiet": traitValues[17], "Systematic": traitValues[18], "Jealous": traitValues[19],
                   "Shy": traitValues[20], "Organized": traitValues[21], "Extroverted": traitValues[22], "Uncreative": traitValues[23], "Disorganized": traitValues[24], "Talkative": traitValues[25],
                   "Relaxed": traitValues[26], "Unsympathetic": traitValues[27], "Complex": traitValues[28], "Harsh": traitValues[29], "Touchy": traitValues[30], "Efficient": traitValues[31], "Cold": traitValues[32],
                   "Careless": traitValues[33], "Withdrawn": traitValues[34], "Kind": traitValues[35], "Temperamental": traitValues[36], "Inefficient": traitValues[37], "Creative": traitValues[38],
                   "Bashful": traitValues[39]}
    return dict


def reverse(x):
    if x == 1:
        x = 9
    elif x == 2:
        x = 8
    elif x == 3:
        x = 7
    elif x == 4:
        x = 6
    elif x == 6:
        x = 4
    elif x == 7:
        x = 3
    elif x == 8:
        x = 2
    elif x == 9:
        x = 1
    return x

#scores the individual dictionaries 
def scorePassword(Dictionary1):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    for i in Dictionary1:
        if i == "Bashful":
            Dictionary1["Bashful"] = reverse(Dictionary1.get(i))
        elif i == "Quiet":
            Dictionary1["Quiet"] = reverse(Dictionary1.get(i))
        elif i == "Shy":
            Dictionary1["Shy"] = reverse(Dictionary1.get(i))
        elif i == "Withdrawn":
            Dictionary1["Withdrawn"] = reverse(Dictionary1.get(i))
        elif i == "Cold":
            Dictionary1["Cold"] = reverse(Dictionary1.get(i))
        elif i == "Harsh":
            Dictionary1["Harsh"] = reverse(Dictionary1.get(i))
        elif i == "Rude":
            Dictionary1["Rude"] = reverse(Dictionary1.get(i))
        elif i == "Unsympathetic":
            Dictionary1["Unsympathetic"] = reverse(Dictionary1.get(i))
        elif i == "Careless":
            Dictionary1["Careless"] = reverse(Dictionary1.get(i))
        elif i == "Disorganized":
            Dictionary1["Disorganized"] = reverse(Dictionary1.get(i))
        elif i == "Inefficient":
            Dictionary1["Inefficient"] = reverse(Dictionary1.get(i))
        elif i == "Sloppy":
            Dictionary1["Sloppy"] = reverse(Dictionary1.get(i))
        elif i == "Relaxed":
            Dictionary1["Relaxed"] = reverse(Dictionary1.get(i))
        elif i == "Unenvious":
            Dictionary1["Unenvious"] = reverse(Dictionary1.get(i))
        elif i == "Uncreative":
            Dictionary1["Uncreative"] = reverse(Dictionary1.get(i))
        elif i == "Unintellectual":
            Dictionary1["Unintellectual"] = reverse(Dictionary1.get(i))

    for n in Dictionary1:
        if n == "Bashful":
            sum1 += Dictionary1.get(n)
        elif n == "Bold":
            sum1 += Dictionary1.get(n)
        elif n == "Energetic":
            sum1 += Dictionary1.get(n)
        elif n == "Extroverted":
            sum1 += Dictionary1.get(n)
        elif n == "Quiet":
            sum1 += Dictionary1.get(n)
        elif n == "Shy":
            sum1 += Dictionary1.get(n)
        elif n == "Talkative":
            sum1 += Dictionary1.get(n)
        elif n == "Withdrawn":
            sum1 += Dictionary1.get(n)

    for m in Dictionary1:
        if m == "Cold":
            sum2 += Dictionary1.get(m)
        elif m == "Cooperative":
            sum2 += Dictionary1.get(m)
        elif m == "Harsh":
            sum2 += Dictionary1.get(m)
        elif m == "Kind":
            sum2 += Dictionary1.get(m)
        elif m == "Rude":
            sum2 += Dictionary1.get(m)
        elif m == "Sympathetic":
            sum2 += Dictionary1.get(m)
        elif m == "Unsympathetic":
            sum2 += Dictionary1.get(m)
        elif m == "Warm":
            sum2 += Dictionary1.get(m)

    for x in Dictionary1:
        if x == "Careless":
            sum3 += Dictionary1.get(x)
        elif x == "Disorganized":
            sum3 += Dictionary1.get(x)
        elif x == "Efficient":
            sum3 += Dictionary1.get(x)
        elif x == "Inefficient":
            sum3 += Dictionary1.get(x)
        elif x == "Organized":
            sum3 += Dictionary1.get(x)
        elif x == "Practical":
            sum3 += Dictionary1.get(x)
        elif x == "Sloppy":
            sum3 += Dictionary1.get(x)
        elif x == "Systematic":
            sum3 += Dictionary1.get(x)

    for s in Dictionary1:
        if s == "Envious":
            sum4 += Dictionary1.get(s)
        elif s == "Fretful":
            sum4 += Dictionary1.get(s)
        elif s == "Jealous":
            sum4 += Dictionary1.get(s)
        elif s == "Moody":
            sum4 += Dictionary1.get(s)
        elif s == "Relaxed":
            sum4 += Dictionary1.get(s)
        elif s == "Temperamental":
            sum4 += Dictionary1.get(s)
        elif s == "Touchy":
            sum4 += Dictionary1.get(s)
        elif s == "Unenvious":
            sum4 += Dictionary1.get(s)

    for t in Dictionary1:
        if t == "Complex":
            sum5 += Dictionary1.get(t)
        elif t == "Deep":
            sum5 += Dictionary1.get(t)
        elif t == "Creative":
            sum5 += Dictionary1.get(t)
        elif t == "Imaginative":
            sum5 += Dictionary1.get(t)
        elif t == "Intellectual":
            sum5 += Dictionary1.get(t)
        elif t == "Philosophical":
            sum5 += Dictionary1.get(t)
        elif t == "Uncreative":
            sum5 += Dictionary1.get(t)
        elif t == "Unintellectual":
            sum5 += Dictionary1.get(t)

    BigFive = {"Extraversion": sum1, "Agreeable": sum2, "Conscientious": sum3, "Neurotic": sum4, "Openness/Intellect": sum5}

    return BigFive

#creates a list of the dictionaries
def totalScores(traitValues):
    for x in traitValues:
        dict=createDictionary(x)
        allScores.append(scorePassword(dict))
totalScores(readFile('Q23CSVcopy.csv'))

with open('Q23Scores.csv','w') as out:

    csv_out=csv.writer(out)
    csv_out.writerow(['Extraversion','Agreeable','Conscientious','Neurotic','Openness/Intellect'])
    for dictionaries in allScores:
        csv_out.writerow(dictionaries.values())
            
