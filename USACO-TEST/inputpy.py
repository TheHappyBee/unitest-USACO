

class inputpy:
     def __init__(self, n, prob):
          testcasedic = r'C:\Users\Liu Home Desktop\Documents\USACO-TEST\Data-'+prob[0]+"_"+prob[1]+"_"+prob[2]
          with open(testcasedic+"\\"+str(n)+".in",'r') as input:
               inx = input.read()
          self.data =inx
     def inputpy(self):
          input = self.data.split('\n')[0:-1] # end element is '' we don't want that
          return input
     
          
          
