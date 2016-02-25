import os.path
import json
import sunlight

def get_state_legislators(s):
    filestring = 'data/' + s + '.json'
    if os.path.isfile(filestring):
        pass
    else:
        build_legislators(s, filestring)
    return return_legislators(filestring)
        
def return_legislators(filestring):
    with open(filestring, 'r') as f:
        output = f.read()
        return json.loads(output)
    
def build_legislators(s, filestring):
    output = sunlight.openstates.legislators(state=s)
    with open(filestring, 'w+') as f:
        json.dump(output, f)