import os
import json

from pyarrow.pandas_compat import dataframe_to_arrays
from streamlit.elements import write


#写入文件逻辑
def initJson(jsonfile):
    if os.path.exists(jsonfile):
        with open(jsonfile,"r") as f:
            try:
                datajson = json.load(f)
            except json.decoder.JSONDecodeError:
                datajson={}
    else:
        datajson = {}
    return datajson

def writeJson(jsonfile,username,password):
    datareturn2=initJson(jsonfile)
    datareturn2[username] = password
    with open(jsonfile,"w") as f:
        json.dump(datareturn2,f,indent=4)


username=input("username:")
password=input("password:")
initJson("Database/username.json")
writeJson("Database/username.json",username,password)