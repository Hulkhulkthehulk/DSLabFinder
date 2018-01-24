import urllib.request
url = 'http://www.cs.rpi.edu/academics/courses/fall17/csci1200/labs/12_order_notation/'
while(True):
    try:
        page = urllib.request.urlopen( url + 'lab_post.pdf')
    except:
        print("LAB POST DOESNT WORK")
    else:
        print("LAB POST WORKS")
        break
 
for newline in open('words.txt','r'):
    try:
        page = urllib.request.urlopen( url + str(newline[:-1] + '.pdf'))
    except:
        continue
    else:
        print( url + str(newline[:-1] + '.pdf' ))
        break
        #fixed a parenthesis that was throwing a syntax error
