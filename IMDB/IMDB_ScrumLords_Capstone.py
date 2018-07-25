import pandas as pd

#===============================================================================
#     READ INPUT DATA
#===============================================================================

#--------------------------------------------------------
#--  Input File 1:  name.basics.tsv
#--------------------------------------------------------
print('Reading name.basics.tsv')
nameBasics = pd.read_csv("./Data/name.basics.tsv/data.tsv", sep='\t')
print('Complete - 1 of 7')
print(nameBasics.head(5))

#--------------------------------------------------------
#--  Input File 2:  title.akas.tsv
#--------------------------------------------------------
print('Reading title.akas.tsv')
titleAkas = pd.read_csv("./Data/title.akas.tsv/data.tsv", sep='\t',dtype={"titleId": object, "ordering": object, "title": object, "region": object, "language": object, "types": object, "attributes": object, "isOriginalTitle": object})
print('Complete - 2 of 7')
print(titleAkas.head(5))

#--------------------------------------------------------
#--  Input File 3:  title.basics.tsv
#--------------------------------------------------------
print('Reading title.basics.tsv')
titleBasics = pd.read_csv("./Data/title.basics.tsv/data.tsv", sep='\t',dtype={"tconst": object, "titleType": object, "primaryTitle": object, "originalTitle": object, "isAdult": object, "startYear": object})
#print('Complete - 3 of 7')
print(titleBasics.head(5))

#--------------------------------------------------------
#--  Input File 4:  title.crew.tsv
#--------------------------------------------------------
print('Reading title.crew.tsv')
titleCrew = pd.read_csv("./Data/title.crew.tsv/data.tsv", sep='\t')
print('Complete - 4 of 7')
print(titleCrew.head(5))

#--------------------------------------------------------
#--  Input File 5:  title.episode.tsv
#--------------------------------------------------------
print('Reading title.episode.tsv')
titleEpisode = pd.read_csv("./Data/title.episode.tsv/data.tsv", sep='\t')
print('Complete - 5 of 7')
print(titleEpisode.head(5))

#--------------------------------------------------------
#--  Input File 6:  title.principals.tsv
#--------------------------------------------------------
print('Reading title.principals.tsv')
titlePrincipals = pd.read_csv("./Data/title.principals.tsv/data.tsv", sep='\t')
print('Complete - 6 of 7')
print(titlePrincipals.head(5))

#--------------------------------------------------------
#--  Input File 7:  title.ratings.tsv
#--------------------------------------------------------
print('Reading title.ratings.tsv')
titleRatings = pd.read_csv("./Data/title.ratings.tsv/data.tsv", sep='\t',dtype={"tconst": object, "averageRating": float, "numVotes": int})
print('Complete - 7 of 7')
print(titlePrincipals.head(5))

print('\n-----all data loaded -----')