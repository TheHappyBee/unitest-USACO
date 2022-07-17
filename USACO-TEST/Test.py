import requests
import zipfile
import io
import argparse
import os
import subprocess
from assertpy import testcases
parser = argparse.ArgumentParser(description='Get args')
parser.add_argument("--language", type=str, default="python")
parser.add_argument("--prob")
args = parser.parse_args()
language = args.language
prob = args.prob.lower().split(".")
def setup():
     global zipfile
     urlDomain = "http://www.usaco.org/current/data/"+prob[2]+"_"+prob[0]+"_"+prob[1]+".zip"
     print("Downloading USACO test cases...")
     filename = prob[2]+"_"+prob[0]+"_"+prob[1]+".zip()"
     try:
          req = requests.get(urlDomain)
     except:
          raise ConnectionError("Request not able to be handled")

     print("Download Complete!")
     print("="*20)
     print("Collecting Data...")
     print(urlDomain)
     try:
          zipfile= zipfile.ZipFile(io.BytesIO(req.content))
     except:
          raise Exception("url Domain was not found- 404")
     newpath = r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2]
     if not os.path.exists(newpath):
         os.makedirs(newpath)
     zipfile.extractall(r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2])
def readtestcases(n):
     testcasedic = r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2]
     with open(testcasedic+"\\"+str(n)+".out",'r') as output:
          out = output.read()
     with open(testcasedic+"\\"+str(n)+".in",'r') as input:
          inx = input.read()
     return [inx, out]
def runtestcases(filenames):
     success = 0
     for n in range(len(filenames)//2):
          print("Starting test case "+str(n+1)+" of "+str(len(filenames)//2))
          print("="*50)
          cases = readtestcases(n+1)
          testcase = testcases(prob, cases)
          status = testcase.check(n)
          print("status =", status)
          if status == "OK\n":
               success = success + 1
     print("="*50)
     print("Failed "+str((len(filenames)//2)-success)+" of "+str(len(filenames)//2))
     
          
     
     
     
          
#we must check if we have already setup
if not os.path.exists(r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2]):
     setup()
else:
     print("required testcases were already downloaded")
filenames = []
file_path = []
for root, directories, files in os.walk(r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2]):
     for filename in files:
          filepath = os.path.join(root, filename)
          filenames.append(filename)
          file_path.append(filepath)
print("Starting Test cases("+str(len(filenames)//2)+")...")
filename = prob[0]+"_"+prob[1]+"_"+prob[2]+".py"

#assert python
if (language == "python"):
     runtestcases(filenames)
else:
     print("language has not been implemented yet")

    




