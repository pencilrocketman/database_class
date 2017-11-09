import requests
import json
import csv,sys,os
num=sys.argv[1]
def find_stats(player_id):
 url='http://stats.nba.com/stats/shotchartdetail?Period=0&VsConference=&LeagueID=00&LastNGames=0&TeamID=0&Position=&Location=&Outcome=&ContextMeasure=FGA&DateFrom=&StartPeriod=&DateTo=&OpponentTeamID=0&ContextFilter=&RangeType=&Season=2015-16&AheadBehind=&PlayerID='+player_id+'&EndRange=&VsDivision=&PointDiff=&RookieYear=&GameSegment=&Month=0&ClutchTime=&StartRange=&EndPeriod=&SeasonType=Regular+Season&SeasonSegment=&GameID=&PlayerPosition='

 data=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', })
 entries=data.json()
 with open('add.csv','w') as foutput:
  csvout=csv.writer(foutput)
  csvout.writerows(entries['resultSets'][0]['rowSet'])
find_stats(num)
os._exit(0)
