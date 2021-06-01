import csv

with open('Student_marks_list.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    names=[]
    mat=[]
    phy=[]
    bio=[]
    chem=[]
    hin=[]
    eng=[]
    for row in my_reader:
        names.append(row[0])
        mat.append(row[1])
        bio.append(row[2])
        eng.append(row[3])
        phy.append(row[4])
        chem.append(row[5])
        hin.append(row[6])
    names.pop(0)
    mat.pop(0)
    bio.pop(0)
    eng.pop(0)
    phy.pop(0)
    chem.pop(0)
    hin.pop(0)
    s1=max(mat)
    s2=max(bio)
    s3=max(eng)
    s4=max(phy)
    s5=max(chem)
    s6=max(hin)
    #print(s1,s2,s3,s4,s5,s6)
    s1_ind=mat.index(s1)
    s2_ind=bio.index(s2)
    s3_ind=eng.index(s3)
    s4_ind=phy.index(s4)
    s5_ind=chem.index(s5)
    s6_ind=hin.index(s6)
    print("Topper in Maths is:{}".format(names[s1_ind]))
    print("Topper in Biology is:{}".format(names[s2_ind]))
    print("Topper in English is:{}".format(names[s3_ind]))
    print("Topper in Physics is:{}".format(names[s4_ind]))
    print("Topper in Chemistry is:{}".format(names[s5_ind]))
    print("Topper in Hindi is:{}".format(names[s6_ind]))
    
    totals=[]
    for i in range(len(names)):
      total=int(mat[i])+int(bio[i])+int(eng[i])+int(phy[i])+int(chem[i])+int(hin[i])
      totals.append(total)
    #print(totals)
    
    best_three=[]
    for i in range(3):
    	first_total=max(totals)
    	first_total_ind=totals.index(first_total)
    	best_three.append(first_total_ind)
    	totals.pop(first_total_ind)
    
    print("Best students  in the class are {0},{1},{2}.".format(names[best_three[0]],names[best_three[1]+1],names[best_three[2]+1]))
    
    
    
