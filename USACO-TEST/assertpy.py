import subprocess
import shutil
import shlex
import os
import time
class testcases():
     def __init__(self, prob, unitcases):
          self.prob = prob
          self.incase = unitcases[0]
          self.outcase = unitcases[1]

     def check(self,n):
          command = 'py {} --n {}'.format(self.prob[0]+"_"+self.prob[1]+"_"+self.prob[2]+".py", n+1)
          proc = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          indata= self.incase
          stdout, stderr = proc.communicate(input=indata)
          if stdout.strip().decode('utf-8') == self.outcase.strip('\n'):
               return "OK\n"
          elif stdout.strip().decode('utf-8') != self.outcase.strip('\n'):
               return "\nExpected {} Got {}\n".format(self.outcase.strip('\n'),stdout.strip().decode('utf-8'))

          else:
               return "\nGot Error:\n"+stderr
     def checkj(self, n):
          os.system("javac"+self.prob[0]+"_"+self.prob[1]+"_"+self.prob[2]+".java")#FIX:file not compiled
          command = 'java {} {}'.format(self.prob[0]+"_"+self.prob[1]+"_"+self.prob[2]+".java", n+1)
          proc = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          indata= self.incase
          stdout, stderr = proc.communicate(input=indata)
          if stdout.strip().decode('utf-8') == self.outcase.strip('\n'):
               return "OK\n"
          elif stdout.strip().decode('utf-8') != self.outcase.strip('\n'):
               return "\nExpected {} Got {}\n".format(self.outcase.strip('\n'),stdout.strip().decode('utf-8'))

          else:
               return "\nGot Error:\n"+stderr
          
          
          
     
