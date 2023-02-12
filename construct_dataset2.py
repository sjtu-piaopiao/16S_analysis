def construct_dataset2(inputfile,outputfile):
    # inputfile:summary file
    # outputfile:dataset name
    # A 16S gene sequence was randomly selected from each species and 16S gene sequences were combined to create the dataset.
    import random
    PATH='/lustre/home/acct-clslt/clslt-pp/RefSeq/'
    with open(PATH+inputfile) as file:
        dic = {}
        # dic.setdefault(key, []).append(value)
        for line in file.readlines()[1:]:
            key = line.strip().split('\t')[1]
            value = line.strip().split('\t')[4]
            # key is species_taxid, value is 16S_copy
            dic.setdefault(key,[]).append(value)
        k = 0 
        n = len(dic)
        rRNA_dataset = open(PATH+outputfile,'w')
        for i,j in dic.items():
            k += 1
            print("going to extract 16S from species:{}' [Schedule: {}/{}]".format(i,k,n))
            l = [int(num) for num in j]
            index= random.randint(1,sum(l)) # Returns randomly any integer from 1 and sum(l)
            print(index)
            try:
                myfile = open(PATH+'merge_species/{}.fasta'.format(i),'r')
                content = myfile.readlines()
                rRNA_dataset.write(content[index*2-2])
                rRNA_dataset.write(content[index*2-1])
            except:
                print('no file found')
        rRNA_dataset.close()

construct_dataset2(inputfile,outputfile)
