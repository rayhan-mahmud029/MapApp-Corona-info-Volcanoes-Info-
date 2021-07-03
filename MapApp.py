# -*- coding: utf-8 -*-
import pandas
import folium


data = pandas.read_csv('data.csv')
data2 = data.drop(columns = ['Lat', "Long"])
data = data.groupby('Country').sum()
latitude = list(data.Lat)
longitude = list(data.Long)   
country = list(data.index)
#print(len(country), len(latitude), len)
#for con, lat, long in zip(country, latitude,longitude):
    #print(f"Country : {con}, Latitude : {lat} & Longitude : {long}")

#DeathData
deathDF = pandas.read_csv('death_data.csv')
deathDF = deathDF.groupby('Country').sum()
tempC = list(deathDF.index)
deathDF = deathDF.drop(columns = ['Lat', 'Long'])
deathDF = deathDF.T

todayDeath = []
totalDeath = []
for con in country:
    cumuList = list(deathDF[con].to_list())
    cDeath = cumuList[-1]
    tDeath = cumuList[-1] - cumuList[-2]
    #print(con, " :", cDeath)
    totalDeath.append(cDeath)
    todayDeath.append(tDeath)
    
#maxD = max(totalDeath)
#minD = min(totalDeath)
#print(f"maxD = {maxD} & minD = {minD}")   


#totalCase
caseData = pandas.read_csv('totalCase.csv')
caseData = caseData.groupby('Country').sum()
caseData = caseData.drop(columns = ['Lat', 'Long'])
caseData = caseData.T

totalCase = []
lastDayCase = []
for Con in country:
    cumulativeList = list(caseData[Con].to_list())
    cCase = cumulativeList[-1]
    lastDay = cumulativeList[-1] - cumulativeList[-2]
    lastDayCase.append(lastDay)
    #print(Con, " :", lastDay)
    totalCase.append(cCase)
 

#totalRecover
recoverData = pandas.read_csv('recoverData.csv')
recoverData = recoverData.groupby('Country').sum()
recoverData = recoverData.drop(columns = ['Lat', 'Long'])
recoverData = recoverData.T

totalRecoverCase = []
todaysRecover = []
for Con in country:
    cumulativeList = list(recoverData[Con].to_list())
    cCase = cumulativeList[-1]
    tCase = cumulativeList[-1] - cumulativeList[-2]
    #print(Con, " :", cCase)
    totalRecoverCase.append(cCase)
    todaysRecover.append(tCase)
   


html = """ 

  <h6 style=" font-family: ubuntu; font-size: 26px; padding-left: 5px; color: red; ;">Country Name : %s </h6>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Total Case Confirmed: %s</h6>
  </div>
  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Today's Confiemed Case: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: ubuntu; font-size: 20px; padding-left: 5px; color: black; margin-top: -15px;">Total Death: %s</h6>
  </div>
  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: ubuntu; font-size: 20px; padding-left: 5px; color: black; margin-top: -15px;">Today's Death: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Total Recover: %s m</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Today's Recover: %s m</h6>
  </div>


  </div>             
           """

          

baseMap = folium.Map(width = "100%", height = '90%', location= [53.00352237505729, -10.870339025768288] , min_zoom = 1, max_zoom = 15, zoom_start = 2 ,tiles= None)
fgC = folium.FeatureGroup(name = "CoronaInfo")

for con,toCase, tCase, toDeath, tDeath, toReco, tReco, lat, lon in zip(country, totalCase, lastDayCase,totalDeath, todayDeath,totalRecoverCase, todaysRecover, latitude, longitude):
    iframe = folium.IFrame(html =  html % (con, toCase,tCase, toDeath,tDeath, toReco, tReco ) , width=400, height= 250)


    if toDeath < 10000:
        iColor = 'grey'
        Radius = 12
    elif 100000 > toDeath > 10000:
        iColor = 'green'  
        Radius = 17
    #elif 200000 > toDeath > 50000:
        #iColor = 'green' 
        #Radius = 20
    else:
        iColor = 'red' 
        Radius = 27


    fgC.add_child(folium.CircleMarker(location= [lat, lon], radius = Radius, popup = folium.Popup(iframe) , tooltip= f"Click to see Corona Case in {con}" , fill_color = iColor, color = None, fill_opacity = 0.7 ))
















#VOLCANO MAP
df = pandas.read_csv("Volcanoes.txt")
lat = list(df.LAT)
lon = list(df.LON)
height = list(df.ELEV)
loc = list(df.LOCATION)
name = list(df.NAME)
tyype = list(df.TYPE)
status = list(df.STATUS)

#Add HTML
html2 = """ 
  <h6 style=" font-family: ubuntu; font-size: 26px; padding-left: 5px; color: red; ;"> %s Volcano</h6>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Name &nbsp;&nbsp; : %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: ubuntu; font-size: 20px; padding-left: 5px; color: black; margin-top: -20px;">Location: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -20px;">Height &nbsp;: %s m</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -20px;
  disply:flex; justify-content: flex-start;">Type &nbsp; &nbsp;: %s </h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: ubuntu; font-size: 20px; padding-left: 5px; margin-top: -15px;">Status &nbsp;: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <a style="font-family: sans-serif; font-size: 18px; padding-left: 5px; margin-top: -25px; text-decoration:none;" href="https://www.google.com/search?q=%%22%s Volcano%%22" target="_blank">For more info..</a>
  </div>         
           """


fgV = folium.FeatureGroup(name = "Volacanos(US ONLY)")
for l, ln,h,lo,nm,typ,sts in zip(lat, lon,height,loc, name, tyype,status):
  iframe = folium.IFrame(html = html2 % (nm, nm,lo, str(h),typ,sts, nm ) , width=400, height=300)  

  if h < 1000:
    icolor = "gray"
  elif h < 2000:
    icolor = "orange"
  elif h < 3000:
    icolor = "green"
  else:
    icolor = "red"


  fgV.add_child(folium.Marker(location=[l, ln], popup=folium.Popup(iframe), tooltip= f"{nm} Volcano. Double click for more info.",  icon=folium.Icon(color=icolor, shape="circle")))




#fgP = folium.FeatureGroup(name = "Population")
#fgP.add_child(folium.GeoJson(data = open('./GeoJson/world.json', 'r', encoding = "utf-8-sig").read(), style_function = lambda x: {'fillColor' : 'yellow' if x['properties']['POP2005'] < 10000000 else 'green' if 10000000 < x['properties']['POP2005'] < 100000000 else 'red'}))

baseMap.add_child(fgC)
baseMap.add_child(fgV)
#baseMap.add_child(fgP)
folium.TileLayer('cartodbpositron').add_to(baseMap)
baseMap.add_child(folium.LayerControl())
baseMap.save("CoronaInfo.html")

