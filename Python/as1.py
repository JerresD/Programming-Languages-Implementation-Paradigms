import urllib.request,urllib.error 
import gzip
import time


url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"

head = {
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'cf_chl_2=7f5d6ebff7a8097; cf_chl_prog=x12; cf_clearance=dbVaVl2ZZ3T6f25nPOboGnjOni.Pl8t8wp7MUQhCVEM-1636683975-0-250; bq_sd=%7B%22abg%22%3A%22a%22%2C%22bqPvd%22%3A1%7D',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}


def askURL(url):                    # get the web text
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html=ungzip(response.read()).decode()
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    print("Open success.")
    return html

def ungzip(data):                   # decode the gzip
    try:
        data=gzip.decompress(data)
    except:
        pass
    return data

def output(url):                   # Open the web and save the data
    print("Opening the web......")
    html = askURL(url)
    title = input("The word list will save as a txt file, please input the txt file's name: \n")
    if title[-4:] != ".txt":
        title=title+".txt"
    try:
        with open(title, 'w') as f:
            f.write(html)
        print("The word list save as {}.".format(title))
    except:
        print("Save failed.")

def saveNewList(list):             # Save the file
    title = input("Please input the new txt file's name: \n")
    if title[-4:] != ".txt":
        title=title+".txt"
    try:
        l = len(list)
        with open(title, 'w') as f:
            for i in range(0,l):
                f.write(list[i]+"\n")
        print("The word list save as {}.".format(title))
    except:
        print("Save failed.")

def readtext():                #Read the file 
    while 1:
        title = input("Please input the txt file's name: \n")
        if title[-4:] != ".txt":
            title=title+".txt"
        if title == "0":
            break
        try:
            with open(title, 'r') as f:
                data = [line.strip('\n') for line in f.readlines()]
            break
        except:
            print("Open failed.")
    return data

def sort(list,wordLength):  # The LSD sorting algo 
    asciiNum = 128          # The number of the ascii
    wordNum = len(list)     # The number of the word
    newList = ["" for i in range(0,wordNum)]        # a list for the word after sorting

    for letter in range((wordLength-1),-1,-1):        # The main cycle of sorting from the last letter to the first

        count = [0 for i in range(0,asciiNum+1)]    # a list for the frequency of letters

        for i in range(0,wordNum):                  # The frequency
            count[ord(list[i][letter])+1] += 1
        
        for i in range(0, asciiNum):                # The first position of each letter
            count[i+1] += count[i]

        for i in range(0, wordNum):                 # sorting of the word by the letter  
            newList[count[ord(list[i][letter])]] = list[i]
            count[ord(list[i][letter])]+=1
        
        for i in range(0, wordNum):                 # copy the new word list
            list[i] = newList[i]   

    return list         

def menu():             # the option
    print("0.Quit.")
    print("1.Start the LSD sorting.")


def process():          # The main process
    input("Enter any key to get text:")
    output(url)         # Read the data 
    while 1:
        
        menu()
        choose = input("Please input a number(0-1):\n")
        if choose == "0":
            break
        elif choose == "1":
            list = readtext()          # get the word list
            start_time = time.time()		# execution starts
            newList = sort(list,5)          # get the word list after the sorting 
            end_time = time.time()			# execution ends
            print('Duration: {}'.format(end_time - start_time))		# print execution time 

            saveNewList(newList)            # save the file
        else :
            print("Invalid inputs, please try again:")


if __name__ == '__main__':
    process()

    
