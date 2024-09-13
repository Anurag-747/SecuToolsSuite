import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from iplocator import iplocate
from TraceIP import read_multiple_ip
from webscrap import Links
from number import number

R = '\033[1;31;40m' 
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m' 

def reconinput():
    inp=(input("Info>> "))
    if(inp == '1'):
        iplocate()
    elif (inp=='2'):
        read_multiple_ip()
    elif(inp=='3'):
        urlinfo()
    elif(inp =='4'):
        pdfinfo()
    elif (inp=='5'):
        Links()
    elif(inp=='6'):
        number()
    elif(inp=='exit'):
        exit()
    elif(inp=='tools'):
        print(G+"""Tools available 
    
            1.Trace Single IP
            2.Heatmap
            3.URL redirection checker
            4.PDF meta data analysis
            5.URL lookup in webpages
            6.Phonenumber verifier
            
            usage : type exit to stop
            """)
    else:
        print(R+"Enter an valid option")
    while True:
        reconinput()    
        
if __name__=="__main__":
   reconinput()
     
    
