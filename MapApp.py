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
  <div>
  <h6 style=" font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  font-size: %s; padding-left: 5px; color: %s;">Country Name : %s </h6></div>
  <div>
  <h6 style=" font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 15px; padding-left: 5px; color: purple; margin-top: -50px; padding-top:-20px;">Last Update: 22 Jun, 2021 </h6></div>


  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; padding-left: 5px; margin-top: -15px;">Total Case Confirmed: %s</h6>
  </div>
  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; padding-left: 5px; margin-top: -30px;">Today's Confirmed Case: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; padding-left: 5px; color: black; margin-top: -30px;">Total Death: %s</h6>
  </div>
  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;; font-size: 16px; padding-left: 5px; color: black; margin-top: -30px;">Today's Death: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;; font-size: 16px; padding-left: 5px; margin-top: -30px;">Total Recover: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;; font-size: 16px; padding-left: 5px; margin-top: -30px;">Today's Recover: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <a style="font-family: sans-serif; font-size: 15px; padding-left: 5px; margin-top: -30px; text-decoration:none;" href="https://www.google.com/search?q=%%22%s Corona Update%%22" target="_blank">For more info..</a>
  </div>    
  </div>             
           """

          

baseMap = folium.Map(width = "100%", height = '90%', location= [24.213947958206976, 90.13233056778674] , min_zoom = 1, max_zoom = 15, zoom_start = 4 ,tiles= None)
fgC = folium.FeatureGroup(name = "CoronaInfo")

for con,toCase, tCase, toDeath, tDeath, toReco, tReco, lat, lon in zip(country, totalCase, lastDayCase,totalDeath, todayDeath,totalRecoverCase, todaysRecover, latitude, longitude):

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

#for font settings by len of country name
    if len(con) <= 6:
      cFont = "24px"
    elif 6 < len(con) <= 10:
      cFont = "21px"
    elif 10 < len(con) < 13:
      cFont = "20px"
    else:
      cFont = "18px" 

    iframe = folium.IFrame(html =  html % (cFont, iColor, con, toCase,tCase, toDeath,tDeath, toReco, tReco,con) , width=320, height= 250)





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
  <h6 style=" font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 24px; padding-left: 5px; color: %s; ;"> %s Volcano</h6>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 18px; padding-left: 5px; margin-top: -30px;">Name &nbsp;&nbsp; : %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style=" font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 18px; padding-left: 5px; color: black; margin-top: -30px;">Location: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 18px; padding-left: 5px; margin-top: -30px;">Height &nbsp;: %s m</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 18px; padding-left: 5px; margin-top: -30px; disply:flex; justify-content: flex-start;">Type &nbsp; &nbsp;: %s </h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <h6 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 18px; padding-left: 5px; margin-top: -30px;">Status &nbsp;: %s</h6>
  </div>

  <div style="display: flex; justify-content: space-between;">
  <a style="font-family: sans-serif; font-size: 16px; padding-left: 5px; margin-top: -25px; text-decoration:none;" href="https://www.google.com/search?q=%%22%s Volcano%%22" target="_blank">For more info..</a>
  </div>         
           """


fgV = folium.FeatureGroup(name = "Volacanos(US ONLY)")
for l, ln,h,lo,nm,typ,sts in zip(lat, lon,height,loc, name, tyype,status):

  if h < 1000:
    icolor = "gray"
  elif h < 2000:
    icolor = "orange"
  elif h < 3000:
    icolor = "green"
  else:
    icolor = "red"

  iframe = folium.IFrame(html = html2 % (icolor, nm, nm,lo, str(h),typ,sts, nm ) , width=300, height=300)  



  fgV.add_child(folium.Marker(location=[l, ln], popup=folium.Popup(iframe), tooltip= f"{nm} Volcano. Double click for more info.",  icon=folium.Icon(color=icolor, shape="circle")))




#fgP = folium.FeatureGroup(name = "Population")
#fgP.add_child(folium.GeoJson(data = open('./GeoJson/world.json', 'r', encoding = "utf-8-sig").read(), style_function = lambda x: {'fillColor' : 'yellow' if x['properties']['POP2005'] < 10000000 else 'green' if 10000000 < x['properties']['POP2005'] < 100000000 else 'red'}))

baseMap.add_child(fgC)
baseMap.add_child(fgV)
#baseMap.add_child(fgP)
folium.TileLayer('cartodbpositron').add_to(baseMap)
baseMap.add_child(folium.LayerControl())
baseMap.save("CoronaInfo.html")

