import json
import pickle
import sys

def save (idx):
    pickle.dump(idx,open("channel.p", "wb"))

def load ():
    return pickle.load(open("channel.p", "rb"))

with open('db/channels.json') as json_data:
    channels = json.load(json_data)
    idx = load()
    if (len(sys.argv) != 1):
        if (sys.argv[1] == "next"):
            idx += 1
        elif (sys.argv[1] == "prev"):
            idx -= 1
        if (idx >= len(channels)) :
            idx = 0
        if (idx < 0) :
            idx = d.length -1
    #print (idx)
    print(channels[idx]['url'])
