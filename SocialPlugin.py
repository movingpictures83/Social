import numpy
import PyPluMA

class SocialPlugin:
   def input(self, filename):
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      corfile = open(PyPluMA.prefix()+"/"+self.parameters["corfile"], 'r')
      clusterfile = open(PyPluMA.prefix()+"/"+self.parameters["clusterfile"], 'r')
       

      self.taxa = corfile.readline().strip().split(',')

      self.clusters = []
      cluster = -1
      for line in clusterfile:
         contents = line.strip().split(',')
         if (contents[1] == '\"x\"'):
            self.clusters.append([])
            cluster += 1
         else:
            self.clusters[cluster].append(self.taxa.index(contents[1]))

      self.cors = []
      self.cors.append(self.taxa)
      for line in corfile:
          self.cors.append(line.strip().split(','))

   def run(self):
       pass

   def output(self, filename):
       outfile = open(filename, 'w')

       for i in range(len(self.clusters)):
           #for j in range(i+1, len(self.clusters)):
                outfile.write("CLUSTER "+str(i)+"\n")
                vec = []
                for k in range(0, len(self.clusters[i])):
                   for l in range(k+1, len(self.clusters[i])):
                       node1 = self.clusters[i][k]
                       node2 = self.clusters[i][l]
                       outfile.write(self.taxa[node1]+" "+self.taxa[node2]+" "+self.cors[node1][node2]+"\n")
                       value = float(self.cors[node1][node2])
                       if (value != 0):
                          vec.append(value)
                outfile.write(str(numpy.mean(vec))+"\n")
                outfile.write(str(numpy.std(vec))+"\n")
       outfile.write(str(vec))
   
