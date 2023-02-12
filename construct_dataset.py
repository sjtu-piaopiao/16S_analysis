def construct_dataset(inputfile,outputfile):
    # inputfile:summary file
    # outputfile:dataset name
    # A genome was randomly selected from each species and 16S gene sequences were combined to create the dataset.
    import random
    PATH='/lustre/home/acct-clslt/clslt-pp/RefSeq/'
    with open(PATH+inputfile) as file:
        dic = {}
        # dic.setdefault(key, []).append(value)
        for line in file.readlines()[1:]:
            # key is species_taxid
            key = line.strip().split('\t')[1]
            # print(key)
            # value is accession_id
            value = line.strip().split('\t')[0]
            # Add key-value pair to the dictionary
            dic.setdefault(key,[]).append(value)
        print(dic)
        k = 0 
        n = len(dic)
        rRNA_dataset = open(PATH+outputfile,'w') 
        for i,j in dic.items():
            k += 1
            print("going to extract 16S from species:{}' [Schedule: {}/{}]".format(i,k,n))
            index= random.randint(0,len(j)-1) #Returns randomly any integer from 0 and len(j)-1
            try:
                # j[index] represents an accession_id
                myfile = open(PATH+'RefSeq/RNA_file/{}.16S_fa'.format(j[index]),'r')
                content = myfile.read()
                rRNA_dataset.write(content)
                myfile.close()
            except:
                print('no file found')
        rRNA_dataset.close()

construct_dataset(inputfile,outputfile)
