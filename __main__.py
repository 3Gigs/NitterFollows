def txt_to_list(txt):
    followers = []
    TXT_DATA = open(txt, "r", encoding="utf-8")
    while True:
        USER = TXT_DATA.readline()
        if(USER != ""):
           followers.append(USER.replace('\n', '').replace('\r', '').replace('@', '')) 
        else:
            break
    return followers

def main():
    print(txt_to_list("FOLLOWERS.txt"))

main()
