import datetime
import time
from urllib.request import urlopen

isGame = True

#get all games for the day
url = 'http://live.nhle.com/GameData/GCScoreboard/'+str(datetime.date.today())+'.jsonp'
#url = 'http://live.nhle.com/GameData/GCScoreboard/2015-10-08.jsonp'
socket = urlopen(url)
html = socket.read().decode()
socket.close()
if '"id"' not in html:
    print("No Games")
    isGame = False
else:
    if '"CHI"' not in html: #abbr
        isGame = False
        print("No Blackhawks Game")
    lines = html.split("},{")
    i = 0

    while i < len(lines):
        if '"CHICAGO"' in lines[i]:
            iid = lines[i].index('"id":')
            id = lines[i][iid+5:iid+15]
            print("GID: " + id)
            break
        else:
            i = i+1

#import pyglet
#sound = pyglet.media.load('gh.mp3', streaming=False)
#sound.play()
#pyglet.app.run()

while isGame:
#get scoreboard for selected game
    url = 'http://live.nhle.com/GameData/20152016/'+id+'/gc/gcsb.jsonp'
    socket = urlopen(url)
    html = socket.read().decode()
    socket.close()
    print(html)
#get box score for selected game
    url = 'http://live.nhle.com/GameData/20152016/'+id+'/gc/gcbx.jsonp'
    socket = urlopen(url)
    html = socket.read().decode()
    socket.close()
    print(html)

    url = 'http://live.nhle.com/GameData/GCScoreboard/'+str(datetime.date.today())+'.jsonp'
    #url = 'http://live.nhle.com/GameData/GCScoreboard/2015-10-08.jsonp'
    socket = urlopen(url)
    html = socket.read().decode()
    socket.close()
    print(html)
#refresh delay
    time.sleep(30)
