from requests import get
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m' 

def ReverseIP():
    host=input("Enter host >> ")
    lookup = f'https://api.hackertarget.com/reverseiplookup/?q={host}' 
    #lookup = f'-----your hackertarget api url here-----?q={host}'
    try:
        result = get(lookup).text
        print(cyan+"[+]"+result)
    except:
        print(red+'Invalid IP address')
if __name__=="__main__":
    ReverseIP()