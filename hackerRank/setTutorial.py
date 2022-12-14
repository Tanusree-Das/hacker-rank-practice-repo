"""A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order."""

if __name__=="__main__":
    user_choice=int(input("press 1 to run basic set operation to find average of distinct values in a given array"
                          "\npress 2 to run add functionality of sets"
                          "\npress 3 to perform remove, pop and discard methods on a given set and print sum of"
                          "the remaining elements, make sure the inputs should be >0 and <9\n"))
    if (user_choice==1):

        size_of_array = int(input("size of array?")) #N, the size of arr
        #N space-separated integers,arr[i]
        plant_heights = map(int, input("provide numbers of space separated intergers").split())
        plant = set()
        plant.update(plant_heights)
        avg_of_plant = sum(plant) / len(plant)
        print("avg_height=", avg_of_plant)

    elif(user_choice==2):

        N = int(input("no of stamp?"))
        s = set([])
        for i in range(N):
            country_name = input("Which country stamp is this?")
            s.add(country_name)
        v_count = len(s)
        print("we have total ",v_count, " country's stamp")

    elif(user_choice==3):

        n = int(input("how many elements are present in the set?"))
        s = set(map(int, input("enter space separated positive numbers, to be entered in the set").split()))
        N= int(input("how many commands will be performed on the set?"))
        print("enter commands")
        for i in range(N):
            command_to_be_performed,*numbers=input().split()
            try:
                if(command_to_be_performed.lower()=="pop"):
                    s.pop()
                elif(command_to_be_performed.lower()=="remove"):
                    s.remove(int(numbers[0]))
                elif (command_to_be_performed.lower() == "discard"):
                    s.discard(int(numbers[0]))
            except Exception as e:
                pass
        print("sum of remaining items are= ",sum(s))

