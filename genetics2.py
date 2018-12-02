'''Lorrayya Williams
Final Project
Computer Science 108'''

#person class that stores general
class Person:
    ''' Intializes Person object'''
    
    #intializes
    def __init__(self,allele="Default", familial="Default"):
        self._allele = allele.split(',')
        self._family = familial
        self._gender = "None"
        
    #accessor for allele
    def get_allele(self):            
        return self._allele
   
    #accessor for gender
    def get_gender(self):
        return self._gender
    
    #accessor for relation
    def get_familial_relation(self):
        return self._family

    #mutator for allele
    def set_allele(self, newval):
        self._allele = newval.split(',')
    
    #mutator for family relationship and gender
    def set_familial(self,newval):
        self._family = newval
        if self._family == 'father':
           self._gender = 'm'
        elif self._family == 'mother':
            self._gender = 'f'
    
    #accessor for relation
    def get_familial_relation(self):
        return self._family

class Prediction:
    '''Predicts the alleles of the children'''
    def __init__(self, allele1 = "Default" , allele2 = "Default"):
        self.allele1 = allele1
        self.allele2 = allele2
        self.kids = []
    
    #mutator for alleles 
    def set_alleles(self,allele1, allele2):
        self.allele1 = allele1
        self.allele2 = allele2
        
        
    #prediction method
    def probablity_kids (self):
        '''Creates a list of possible alleles of the children'''
        for item in self.allele1:
            for i in self.allele2:
                self.kids.append(item +i)
                
    def capital_first(self):         
        '''Makes the capital letter the first letter in the allele'''
        count = 0
        for item in self.kids:
            if item[1] == 'A':
                item = item[1] + item[0]
                self.kids.pop(count)
                self.kids.insert(count, item)
            count +=1
        
    def percent_probability(self):
        self.percent = []
        for item in self.kids:
            self.percent.append(int((self.kids.count(item)/len(self.kids))*100))    
    
    def get_kids(self):
        return self.kids
    
    def get_percent(self):
        return self.percent    
    '''Possibly Add dictionary of allele to count'''

    


p= Prediction("Aa","Aa")
p.probablity_kids()
p.capital_first()
print(p.percent_probability())

class Diseases:
    
    def __init__(self, file):
        self._disease = []
        self._type= []
        with open (file) as file:
            lines = file.readlines()
            for line in lines: #FIX ME MAke it wear each line splits into 2 sections of the list 
                line =line.split(',')
                self._disease.append(line)
        for idx in range(len(self._disease)):
            self._type.append(self._disease[idx])  #FIX ME
            
    def get_disease_list(self):
        return self._disease
    
    def get_type_list(self):
        return self._type
    

                


