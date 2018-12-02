
'''class find_gene:
    def __init__(self,file):
        self.file = file
        with open(self.file) as file:
            line.find('ATG')
            
#empty lists for beginning gene and ending gene
            
f = find_gene("dnacrap")'''
index_beginning_gene = []
index_end_gene= []
#Adds indexes of beginning and end genes to seperate lists 
for idx in range(len(genome)):
    if genome[idx] == "T":
        if (genome[idx: idx +3] == 'TAG') or (genome[idx:idx + 3] == 'TAA') or (genome[idx:idx+3] == 'TGA'):
            index_end_gene.append(idx)
    if genome[idx] == 'A':
        if genome[idx:idx+3] == "ATG":
            index_beginning_gene.append(idx)

#adds genes to a list
gene_lst = [] 
for beg_in in index_beginning_gene:
    for end_in in index_end_gene:
        if beg_in < end_in:
            if ((end_in - beg_in) %3) == 0:
                gene_lst.append(genome[beg_in +3 : end_in])
                break
#prints genes 
count = 0
for gene in gene_lst:
    count +=1
    print("Gene %d : %s"%(count,gene))
    
#print this if the genome is not an actual genome 
if gene_lst == []:
    print("no gene is found")
