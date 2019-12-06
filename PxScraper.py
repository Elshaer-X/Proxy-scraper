import requests

B = str("""
  ______ _     _                     
 |  ____| |   | |                    
 | |__  | |___| |__   __ _  ___ _ __ 
 |  __| | / __| '_ \ / _` |/ _ \ '__|
 | |____| \__ \ | | | (_| |  __/ |   
 |______|_|___/_| |_|\__,_|\___|_|   
 
 TOOL       : [PROXY-SCRAPER]
 CREATED BY : MAHMOUD ELSHAER
 FB         : fb.com/elsha3r.ME                                 
 
 GETTING PROXIES ...                                    
 """)
print(B)

def WebsitesList():
    with open("Px-webs.txt","r") as pxWebs:
        pxWebs = pxWebs.read().split("\n")
    return pxWebs

def GetRawData(WebLink):
    R = requests.get(WebLink)
    webContent = R.content
    return webContent
    
def WriteProxy(proxy):
    with open("Results.txt","a") as p:
        p.write(proxy+"\n")
def AnalyseRawData(RawData):
    RawData = str(RawData)
    toBeReplaced = list("<>!@#$%^&*()+=\ /,|;:'\"-")
    for Sign in toBeReplaced:
        RawData = RawData.replace(Sign," ")
    SplitedRawData = RawData.split(" ")
    searchForPort = False
    for Str in SplitedRawData:
        isProxy = True
        proxy , port = "" , ""
        #print(Str)
        if searchForPort:
            if Str.isdigit():
                port = str(Str)
                Px += port
                searchForPort = False
                WriteProxy(Px)
        elif (Str+"x")[0].isdigit() and Str.count(".") == 3:
            Px = ""
            StrL = Str.split(".")
            for Num in StrL:
                if Num.isdigit():
                    pass
                else:
                    isProxy = False
                    break
            if isProxy == True:
                proxy = str(Str)
                searchForPort = True
                Px += proxy+":"
            
def Run():
    Websites = WebsitesList()
    for website in Websites:
        try:
            RawData = GetRawData(website)
            AnalyseRawData(RawData)
        except:
            pass
                    
                    
Run()
