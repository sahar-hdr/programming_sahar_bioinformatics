#1) Read substitution matrices from the PAM250.txt and BLOSUM62.txt files.
#2) Store substitution matrices in dictionaries.
#3) If 1) and 2) are too difficult for you, you can import the dictionaries directly from input_data.py 
#4) Read three alignments from the alignments.fasta file or import them directly from input_data.py.
#5) Use the substitution matrices PAM250 and BLOSUM62 to score each alignment and compare the results. 
#   For gap penalty use a linear gap model with d = -2.
#6) Print each alignment with its score
#7) Re-score the alignments using an affine gap penalty model g(n) = -d - (n -1)*e with d = -2 and e = 0.5 
#   (n = number of consecutive gaps) 


import input_data
pam250=input_data.PAM250_dict
blosum62=input_data.BLOSUM62_dict
align1=input_data.align1
align2=input_data.align2
align3=input_data.align3
alignments = [align1, align2, align3]



for a in range(3):
    pairs=[]
    for i in range(len(alignments[a][0])):
        pairs.append(alignments[a][0][i]+alignments[a][1][i])

    spam=0
    sblosum=0
    for p in pairs:
        if p in pam250 and blosum62:
            spam+=pam250[p]
            sblosum+=blosum62[p]
        else:
            spam+=-2
            sblosum+=-2
    print("scores of alignment",a+1)
    print ("PAM250= ",spam)
    print ("BLOSUM62= ",sblosum)



