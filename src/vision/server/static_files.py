#
#   Serving static files for the web version
#   Author: Yotam Salmon
#   Last Edited: 02/03/18
#

import os
import re

def get(path):
    p = os.path.abspath("web" + path.split("?")[0].split("#")[0])
    print(os.path.exists(p))
    if os.path.exists(p):
        with open(p, "r") as f:
            page = f.read()

        return page
    
    #r = re.findall("<%include(.+?)%>", page)
    #while r.
        
    return None