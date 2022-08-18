def parse_followers_txt(txt):
    followers = []
    TXT_DATA = open(txt, "r", encoding="utf-8")
    while True:
        USER = TXT_DATA.readline()
        if(USER != ""):
           followers.append(USER.replace('\n', '').replace('\r', '').replace('@', '')) 
        else:
            TXT_DATA.close()
            break
    return followers
