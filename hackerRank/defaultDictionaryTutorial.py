if __name__=="__main__":
    print("enter groupA and groupB number of words, separated by space")
    count_groupA,count_groupB=map(int,input().split(" "))
    groupA_list=[]
    groupB_list=[]
    for i in range(count_groupA):
        groupA_list.append(input())
    for j in range(count_groupB):
        groupB_list.append(input())
    for k in groupB_list:
        groupB_entry_in_groupA=[]
        counter=0
        for l in groupA_list:
            if(k==l):
                found_index=groupA_list.index(l,counter)+1
                groupB_entry_in_groupA.append(found_index)
                counter=found_index
        if(counter==0):
            groupB_entry_in_groupA.append(-1)
        print(*groupB_entry_in_groupA,sep=" ")