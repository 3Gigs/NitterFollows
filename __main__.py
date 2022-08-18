from socket import NI_DGRAM
from NitterFollows import parse_followers_txt as parse_txt

def main():
    print(parse_txt("FOLLOWERS.txt"))


main()
