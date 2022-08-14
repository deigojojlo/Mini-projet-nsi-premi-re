def affiche(lst:list) -> None:               #fonction qui nous permet d'afficher des liste à deux dimension de manière plus lisible
    for i in lst:
        print(i)




def codons(adn:list) -> list:               #fonction qui divise en trio les nucleotides
    lst = []
    lst_temp = ''
    for i in range(len(adn)):
        lst_temp += adn[i]
        if len(lst_temp) == 3:
            lst.append(lst_temp)
            lst_temp = ''
    return lst                              #return la liste des trios 





def traduire(adn:list) -> list:
    lst_codons = codons(adn)                #appelle de la fonction codons et initialise la variable lst_codons 
    Table_codonAA = [['Ph','TTT','TTC'],['Le','TTA','TTG','CTA','CTC','CTT','CTG'],['Iso','ATT','ATC','ATA'],['Me','ATG'],['Va','GTA','GTG','GTC','GTT'],['Se','TCA','TCG','TCT','TCC','AGT','AGC'],['Pr','CCA','CCG','CCC','CCT'],['Th','ACA','ACG','ACC','ACT'],['Al','GCA','GCG','GCC','GCT'],['Ty','TAT','TAC'],['Hi','CAT','CAC'],['Gl','CAA','CAG'],['As','AAT','AAC'],['Ly','AAA','AAG'],['Aa','GAT','GAC'],['Ag','GAA','GAG'],['Cy','TGT','TGC'],['Tr','TGG'],['Ar','CGA','CGG','CGC','CGT','AGA','AGG'],['Gy','GGA','GGG','GGC','GGT'],['STOP','TAA','TAG','TGA']]
    lst_acide = []                          #nore liste final de la fonction
    for loop in range(len(lst_codons)):     # tourne autant de fois que la taille de la list
        for i in range(len(Table_codonAA)): #tourne pour la longueur de la liste des AA
            for k in range(1,len(Table_codonAA[i])):    #tourne pour le nombre d'element dans la liste des AA [i]
                if lst_codons[loop] == Table_codonAA[i][k]: #si notre codon est égale à un des codons de la table AA
                    lst_acide.append(Table_codonAA[i][0])   # on ajoute l'AA a notre liste final
    return lst_acide                                        #return la liste de tout les AA




def LireGene(adn:list) -> tuple: #sépare nos gènes et les comptes
    lst_acide = traduire(adn)
    lst_genes = []
    lst_temp = []
    for i in range(len(lst_acide)):                                 #tourne pour la longueur de la liste des AA
        lst_temp = []
        if lst_acide[i] == 'Me' and lst_acide[i-1] == "STOP":       #verifie si me correspond au debue d'une sequence ou si il compose le gène
            for k in range(i,len(lst_acide)):                       
                if lst_acide[k] != 'STOP':                          #si il est different de stop alors
                    lst_temp.append(lst_acide[k])                   #ajoute a la liste temp la totalité du gène
                else:                                               # si l'acide corespond à stop il casse la boucle
                    break
            lst_genes.append(lst_temp)                              # on ajoute le gènes a la liste final
            lst_temp = []                                           # on reinitialise lst_temp
    nb_genes = len(lst_genes)                                       # calcul la nombre de gènes
    return nb_genes , lst_genes                                     # return le nombre de gènes et la liste des gènes ²





def lire_ADN(ADN:list) -> None:
    if len(ADN) % 3 == 0:                                                       #verifie si la longueur de la liste est multiple entier de 3
        nb_genes , lst_genes = LireGene(ADN)                                    #lance le calcul
        if nb_genes == 1:                                                      #si on a un seul gène alors
            print(f"La séquence contient 1 gène : \n")                          #affiche phrase resultat 1 gènes
        else:
            print(f"La séquence contient {nb_genes} gènes : \n")                #affiche phrases pour plusieur gènes 
        affiche(lst_genes)                                                      #affiche la liste des gènes
    else:
        print("la longueur de votre séquence n'est pas multiple entier de trois")#dans le cas où la liste est pas multiple entier de 3



# ''' designe une ligne longue
ADN_1='''ATGCAAGTAGCGAATGATGTTTGCTAAATGTGTCCTGATCGGCTATTACTGTTTCTGTGAATGAACCGGATGCTGCCTAAGATTTCACTGACAGGCTTTACTGTTCATAACTAAATGCAACGGCGTAAGGCAAGAGAAAAGAAACGACCGTAGATGGAAGTCTGTCACTGTTTGACGAAGCATGGCGGTACAGTGAATCACTAAATGTGGGAGTTGACTGGATGAATGAACCGACGAGGAAGGATGTGAATGCCAGACCATTGCATTGTCAGAACTTCACATTGCTGAATGCCTTATGTACGAACAGCACCACTACACTCATGAATGTTCAAAGTTATTGGAGCTCCCCCAAACTTGGGATCTAGTATGGACCTTCATTGGCGTTAAATGAACCCAGGCTCCTCAATATAAATGACCGACACGGAAGAATGCTCTTCTTGA'''
lire_ADN(ADN_1)
