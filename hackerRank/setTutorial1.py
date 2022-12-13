"""A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

->The first line contains the integer, N, the size of arr.
->The second line contains the N space-separated integers,arr[i] .
->find average=(sum of distinct heights)/(Total number of distinct heights)"""

if __name__=="__main__":
    size_of_array=int(input("size of array?"))
    plant_heights=map(int,input("provide numbers of space separated intergers").split())
    plant=set()
    plant.update(plant_heights)
    avg_of_plant=sum(plant)/len(plant)
    print("avg_height=",avg_of_plant)

