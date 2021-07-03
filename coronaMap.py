# -*- coding: utf-8 -*-
import pandas

data = pandas.read_csv('data.csv')
#data = data.drop(columns = [2:5])
data2 = data.drop(columns = ['Lat', 'Long'])
                  
data2 = data2.groupby('Country').sum()

country = list(data.index)

data.set_index('Country', inplace = True)
country2 = list(data.index)
print(country2)
countryCheck = []
for con in country2:
    if con in countryCheck:
        print(con)
    countryCheck.append(con)


latitude = []
longitude =[]
for con in country:
    latList = list(data[con].to_list())
    print(latList)





#DeathData
deathDF = pandas.read_csv('death_data.csv')
deathDF = deathDF.groupby('Country').sum()
deathDF = deathDF.drop(columns = ['Lat', 'Long'])
deathDF = deathDF.T
totalDeath = []
for con in country:
    cumuList = list(deathDF[con].to_list())
    cDeath = cumuList[-1]
    #print(con, " :", cDeath)
    totalDeath.append(cDeath)
    

#totalCase
caseData = pandas.read_csv('totalCase.csv')
caseData = caseData.groupby('Country').sum()
caseData = caseData.drop(columns = ['Lat', 'Long'])
caseData = caseData.T

totalCase = []
for Con in country:
    cumulativeList = list(caseData[Con].to_list())
    cCase = cumulativeList[-1]
    #print(Con, " :", cCase)
    totalCase.append(cCase)
    

#totalRecover
recoverData = pandas.read_csv('recoverData.csv')
recoverData = recoverData.groupby('Country').sum()
recoverData = recoverData.drop(columns = ['Lat', 'Long'])
recoverData = recoverData.T

totalRecoverCase = []
for Con in country:
    cumulativeList = list(recoverData[Con].to_list())
    cCase = cumulativeList[-1]
    #print(Con, " :", cCase)
    totalRecoverCase.append(cCase)

