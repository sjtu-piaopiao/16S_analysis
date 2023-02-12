# @Time   : 2021/12/21 10:17
# @Author : Piaopiao
# @File   : merge_species.py
def merge(inputfile):
    # inputfile:summary_file 
    # Merge all 16S rRNA gene sequences from each species
    import random
    PATH='/lustre/home/acct-clslt/clslt-pp/RefSeq/'
    with open(PATH+inputfile) as file:
        dic = {}
        # dic.setdefault(key, []).append(value)
        for line in file.readlines()[1:]:
            # key is species_taxid
            key = line.strip().split('\t')[1]
            # print(key)
            # vlaue is accession_id
            value = line.strip().split('\t')[0]
            # Add key-value pair to the dictionary
            dic.setdefault(key,[]).append(value)
        print(dic)
        k = 0 
        n = len(dic) # the number of species
        for i,j in dic.items():
            k += 1
            print("going to extract 16S from species:{}' [Schedule: {}/{}]".format(i,k,n))
            sp_sequence = open(PATH+"merge_species/{}.fasta".format(i),'w')
            for ID in j:
                try:
                    myfile = open(PATH+'RNA_file/{}.16S_fa'.format(ID),'r')
                    content = myfile.read()
                    sp_sequence.write(content)
                    myfile.close()
                except:
                    print('no file found')
            sp_sequence.close()

merge(inputfile)