# Name: Het Patel
# Student ID: hpate384
# Descripition: This program takes many diffrent types of data and information about universities all across the world and showcases each info in a output.txt file. 

from os import path
# This function simply reads the contents of both the topUni.csv file and the capitsls.csv file, checks whether if those specific files are the same when opened, and converts it into an list representation. If the file does not match the correct file given, then the program will simply quit 

def loadCSVData(filename):
  list = []
  if (path.exists(filename)):
# This for loop basically iterates through the content in that file, and it simply omids the extra spaces while removing all the commas, and it also creates a list that contains the final output of having the extra spaces and commas removed.  
    fileContent = open(filename, "r", encoding='utf8')
    for line in fileContent:
      line = line.strip()
      data = line.split(",")
      list.append(data)
    fileContent.close()
    return list[1:]  

  print("Error: File not Found")
  quit()

#-----------removeCharacters----------------
# This function (removeCharacters) works to remove the extra brackets contained in each element. For example, in the string "[canada], this function will remove the bracktes, hence "canada" will be printed"
def removeCharacters(list):
  return str(list).strip("[").strip("]").replace("'", "")

#-----------cleanList----------------
# This function (cleanList) creates a function that is called cleanList ant it simply creates
def cleanList(uniqueElements):
  uniqueElements = list(dict.fromkeys(uniqueElements))
  return uniqueElements

#-----------findTopInternationalRankInCountry----------------
# This function (findTopInternationalRankInCountry) gets and returns the top international ranked university in the country
def findTopInternationalRankInCountry(selectedCountry, topUni):
  uniCountries = getUniCountries(topUni)
  return uniCountries[selectedCountry][0] 

#-----------findTopNationalRankInCountry----------------
# This function (findTopNationalRankInCountry) gets and returns the top national ranked university in the country
def findTopNationalRankInCountry(selectedCountry, topUni):
  uniCountries = getUniCountries(topUni)
  topNationalRankUni = uniCountries[selectedCountry][0]
  for uni in uniCountries[selectedCountry]:
    if (topNationalRankUni[3] > uni[3]):
      topNationalRankUni = uni
  return topNationalRankUni

#-----------getAverageScore-----------
# This function (getAverageScore) returns the average university score in the selected country
def getAverageScore(selectedCountry, topUni):
  sum = 0.0
  uniCountries = getUniCountries(topUni)
  for uni in uniCountries[selectedCountry]:
    sum += float(uni[8])
  return sum/len(uniCountries[selectedCountry])

#-----------getUniCountries-----------
# This function (getUniCountries) returns a dictionary, where the keys are the countries, and the values are list of
#universities within each country
def getUniCountries(topUni):
  uniCountries = {}
  for uni in topUni:
    country = uni[2].lower()
    if country not in uniCountries:
      uniCountries[country] = []
    uniCountries[country].append(uni) 
  return uniCountries

#-----------getUniContinents----------- 
# This function (getUniContinents) returns a dictionary, where the keys are the continents, and the values are list of universities within each continents
def getUniContinents(capitals, topUni):
  uniCountries = getUniCountries(topUni)
  uniContinents = {}
  for capital in capitals:
    continent = capital[5].lower()
    if continent not in uniContinents:
      uniContinents[continent] = []
    country = capital[0].lower()
    if country in uniCountries:
      uniInCountry = uniCountries[country]
      uniContinents[continent].extend(uniInCountry)
  return uniContinents

# -----------getHighScoreInContinent----------- 
# This function (getHighScoreInContinent), simply parses through the universities list and it determnines the highest score in that specific continent.
def getHighScoreInContinent(universities):
  highScoreUni = universities[0]
  for uni in universities:
    if float(uni[8]) > float(highScoreUni[8]):
      highScoreUni = uni
      
  return highScoreUni
#-----------getInformation----------- 
# This function (getInformation), acts as the main function in this module, that basiclaly uses all of the previously defined functions, to get the desired result in the output.txt file 
def getInformation(selectedCountry, topUniFileName, capitalsFileName):
  selectedCountry = selectedCountry.lower()
  lines = []
  
# part 1`
# This part simply prints out the total number of universities
  topUni = loadCSVData(topUniFileName) # gets info from csv file
  lines.append("Total number of universities, => {0}\n".format(len(topUni))) # This line simply appends or in other words adds the total number of universities to the list in the output file
  
# part2
# In a generalized fashion, this part simply shows the list of universities in a organized way. Specfically, repeated words are removed, names are in upper case, country names are followed by commas... 
  countries = []
# This for loop adds all of the respective countries to the empty list, and it is further organized by using commas (","), at the end of each country
  for uni in topUni:
    countries.append(uni[2])
  countryList = cleanList(countries)
# This part is what actually serves to display the commas, as well as makes the countries in upper case format 
  countryListFormatted = ", ".join(countryList).upper()
  lines.append("Available countries => {0}\n".format(countryListFormatted))
# This file simply shows the list of all the continent names. 
  capitals = loadCSVData(capitalsFileName)
# Creates a empty dictionary that will later store the corresponding countries 
  countriesToContinents = {}
  for row in capitals:
    countryName = row[0]
    continent = row[5]
    countriesToContinents[countryName] = continent
    
  avalibleContinents = []
  for country in countryList: 
    cont = countriesToContinents[country]
    avalibleContinents.append(cont)

  for capital in capitals:
    avalibleContinents.append(capital[5])

  availContFormatted = ", ".join(cleanList(avalibleContinents)).upper()
  lines.append("Available continents => {0}\n".format((availContFormatted)))

# part 4
# This entire part simply shwows the world rank and name of the university that has the highest international rank within the selected country.
# The topInternationalRankInCountry variable simply assigns the international rank for all universities within the selected country 
  topInternationalRankInCountry = findTopInternationalRankInCountry(selectedCountry, topUni)
  worldRank = topInternationalRankInCountry[0]
  universityName = topInternationalRankInCountry[1]
# This line showcases the world rank and unviersity name. Specfically, world rank is {0} and universityName is {1}
  lines.append("At international rank => {0} the university name is => {1}\n".format(worldRank, universityName))

# part 5
# This entire part serves to showcase the nationl rank and name of the university that has the highest national rank within the selected country 
# The parts below simply checks the national rank of all universities in the selected country 
  topNationalRankInCountry = findTopNationalRankInCountry(selectedCountry, topUni)
  nationalRank = topNationalRankInCountry[3]
  universityName = topNationalRankInCountry[1]
# This line below show cases the national rank and universityName. {0} is nationalRank, {1} is universityName
  lines.append("At national rank => {0} the university name is => {1}\n".format(nationalRank, universityName))

# part 6
# This part serves to caculate the average score of all university within the selected country
  averageScore = getAverageScore(selectedCountry, topUni)
  lines.append("The average score => {0:.2f}%\n".format(averageScore))

# part 7
# This part simply serves to find the relative score by using the averageScore and then dividing it by the highest score within the continent where the selected university is located.
  uniContinents = getUniContinents(capitals, topUni)
  for capital in capitals:
    country = capital[0].lower()
# If the selected country is equal to the capital of the country, then the continent is assigned the capital.
    if selectedCountry == country:
      continent = capital[5].lower()
      highestScore = getHighScoreInContinent(uniContinents[continent])[8]
# This line simply prints out the relative score to the top univeristy. Here, {1} is the continent, {2} is the averageScore.
      lines.append("The relative score to the top university in {0} is => ({1} / {2}) * 100% = {3:.2f}\n".format(
        continent, averageScore, highestScore, float(averageScore) / float(highestScore) * 100.0))   
  
# part 8
# This part simply shows the capitals in respect to the selected country. Depending on what country is selected, the capital will be shows. As a example, if you pick canada then ottawa wil be shown
  for capital in capitals:
    country = capital[0].lower()
# This line simply print out the captial 
    if selectedCountry == country:
      lines.append("The capital is => {0}\n".format(capital[1].upper()))  
  
# part 9
# This entire part as a whole simply serves to show all the university names where the name contains the capital of the respective country.     
  count = 0
# This for loop finds the capital in the capitals file, and it simply assign 
  for capital in capitals:
    country = capital[0].lower()
    if selectedCountry == country:
      countryCapital = capital[1].lower()
      uniCountries = getUniCountries(topUni)
      for uni in uniCountries[selectedCountry]:
        uniName = uni[1].lower()
        if countryCapital in uniName:
          count+=1
          lines.append("#{0} {1}\n".format(count, uni[1].upper()))   

  # This part serves to simply just create the output.txt file. This prints all the outputs for each part in a new file. 
  with open("output.txt", "w", encoding='utf8') as f:
    f.writelines(lines)
  f.close()