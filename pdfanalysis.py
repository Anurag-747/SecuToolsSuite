from PyPDF2 import PdfReader
R = '\033[1;31;40m' 
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'

def pdfinfo():
    filep = input("File path >> ")
    try:
        with open(filep, 'rb') as f:
            pdf = PdfReader(f)
            info = pdf.metadata  # Use pdf.metadata instead of getDocumentInfo()
            number_of_pages = len(pdf.pages)  # Use len(pdf.pages) instead of getNumPages()
        
        try:
            author = info.author if info.author else "Unknown"
            creator = info.creator if info.creator else "Unknown"
            producer = info.producer if info.producer else "Unknown"
            print(C + "[+] Author        : ", author)
            print(C + "[+] Creator       : ", creator)
            print(C + "[+] Producer      : ", producer)
            
            cdate = info.get('/CreationDate', 'Unknown')
            if cdate != 'Unknown':
                cyear = cdate[2:6]
                cmonth = cdate[6:8]
                cd = cdate[8:10]
                print(C + "[+] Creation Date : ", cd, ":", cmonth, ":", cyear)
            
            mdate = info.get('/ModDate', 'Unknown')
            if mdate != 'Unknown':
                myear = mdate[2:6]
                mmonth = mdate[6:8]
                md = mdate[8:10]
                print(C + "[+] Modified Date : ", md, ":", mmonth, ":", myear)
        
        except KeyError:
            print(R + "[-] Meta data not available")
    except Exception as e:
        print(R + f"[-] Error occurred: {e}")

if __name__ == "__main__":
    pdfinfo()
