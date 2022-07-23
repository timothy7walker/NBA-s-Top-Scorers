import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

season_stats = pd.read_csv('Seasons_Stats.csv')


seasonStats = season_stats.drop(columns=['GS', 'MP','G','FG','FGA','FG%','2P','2PA','2P%','PER','ORB','ORB%','3PAr','DRB','DRB%','TRB','TRB%','AST%','STL','STL%','BLK','BLK%','TOV','TOV%','TS%','USG%','blanl','blank2','WS','WS/48','OBPM','BPM','VORP','3P','3P%','3PA','DBPM','OWS','DWS','FTr','FT','FTA','FT%','PF','eFG%','AST'])

seasonStats = seasonStats.dropna()
seasonStats['Year'] = seasonStats['Year'].astype(int)
seasonStats['PTS'] = seasonStats['PTS'].astype(int)
seasonStats['Age'] = seasonStats['Age'].astype(int)

#playerData = pd.DataFrame(seasonStats, columns = ['Year','Player','Pos','Age','Tm','PTS'])
#playerDatalib = playerData.to_dict('index')

seasonByYear = seasonStats.sort_values(by = 'Year') 

allPlayers = seasonByYear.sort_values(by = 'PTS', ascending = False)

plt.figure(figsize=(8,5))
sns.scatterplot(data=allPlayers,x='Year',y='PTS')
plt.title('NBA All players scores 1950 - 2017') #title
plt.xlabel('Season Year') #x label
plt.ylabel('Points Scored') #y label
plt.show()

seasonByYear[['Age' ,'PTS']].describe()

seasonTopScorer = []
seasonTopScorer2 = []
for year in range(1950,2018): 
    currentYear = seasonByYear.loc[seasonByYear['Year'] == year]
    pointSort = currentYear.sort_values(by = 'PTS', ascending=False)
    seasonTopScorer.append(pointSort.iloc[[0]])
    seasonTopScorer2.append(pointSort.iloc[[1]])
    print(pointSort.iloc[[0]])
    print(pointSort.iloc[[1]])

topScorers = pd.concat(seasonTopScorer)
topScorers2 = pd.concat(seasonTopScorer2)

plt.figure(figsize=(8,5))
sns.scatterplot(data=topScorers,x='Year',y='PTS')
plt.title('NBA top Scorers 1950 - 2017') #title
plt.xlabel('Season Year') #x label
plt.ylabel('Points Scored') #y label
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=topScorers2,x='Year',y='PTS')
plt.title('NBA Runner up top scorers 1950 - 2017') #title
plt.xlabel('Season Year') #x label
plt.ylabel('Points Scored') #y label
plt.show()





