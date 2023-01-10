'''There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
 The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j]>=sideLength[i].
 When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is
 possible to stack the cubes. Otherwise, print No.
 Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.'''

if __name__=="__main__":
    test_case_count=int(input("Number of Test Cases?"))
    counter=2**31
    for i in range(test_case_count):
        no_of_cubes=int(input("Number of Cubes?"))
        cube_sides=[int(x) for x in input("Mention the size of each cube separated by a space.").split(" ")]
        cube_side_length=len(cube_sides)
        flag = "Y"
        if(cube_side_length==no_of_cubes):
            for i in range(cube_side_length):
                if (flag=="Y"):
                    left_item=cube_sides[0]
                    right_item=cube_sides[no_of_cubes-1]
                    item_to_be_popped=max(left_item,right_item)
                    print("previos left popped=", left_item, "previous right popped=", right_item, "and counter=", counter)
                    if(counter>=item_to_be_popped):
                        counter=item_to_be_popped
                        cube_sides.remove(counter)
                        no_of_cubes=no_of_cubes-1
                        print("now counter=", counter,"list=",cube_sides)
                    else:
                        flag="N"
            if(flag=="N"):
                print("No")
            else:
                print("Yes")
        else:
            print("You have mentioned" ,no_of_cubes , "cubes are present where gave details about" , cube_side_length , "cube/s. Please check !!!")
