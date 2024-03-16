# To print the first and last letters as Capitals
'''
s1=("hello world")
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)


n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
        print("yes")
else:
    print("no")


# l1 = [1, 2, 3, 4] , l2 = [5, 6, 7, 8,]
# Add both l and l2 , ans ---> [6, 8, 10, 12]


l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
#print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])
l3=[]
for val in range(len(l1)):
    ans=(l1[val]+l2[val])
    l3.append(ans)
print(l3)


# ----> set

# Characteristics of set

1) Set can be created using {}.
2) The elements inside the set are not indexed.
3) Set does not allow duplicate values.
4) It is unordered.
5) Heterogenous.
6) Mutable or changable.


# Eg:1

s1={9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)

#Eg:2
s2={5,8,98,[9,0]}
print(s2)  ----> list


#Eg:3
# min(), max(), len()

# Eg

# To add element inside set

s1={8,78,67,'u'}
s1.add(43)
print(s1)


# update()
s1={8,78,67,'u'}
s1.update([9,0])
print(s1)


# To delete element inside set
s1={8,78,67,'u'}
s1.pop()
print(s1) ---> deletes randomly


# Remove ---> to delete specific value
s1={8,78,67,'u'}
s1.remove(78)
print(s1)  ---> deleted specific value(78)


# Discard
s1={8,78,67,'u'}
s1.discard('u')
print(s1)


# Clear
l1={}
print(type(l1)) --> Datatype is dictionary


s1=set()
print(type(s1)) --> Datatype is set


s1={9,0,8}
s2={9.90,"card",'t',56}
# union() ---> to combine 2 sets
s3=s1.union(s2)
print(s3)


s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2)) --> prints the similar values in both the sets


s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))


# isdisjoint(), issubset(),issuperset()

s1={8,9,0}
s2={6,7,5,8,9,0}
#print(s1.issubset(s2))
print(s1.issuperset(s2))


# Problem 1

s1={1,2,3,4,5}
s2={3,2,7,8,9}

#n={1,2,3} --> s1

for val in s1:
    if val in s2:
        str1="Its joint set"
print(str1)
       


#  ! --->  dictionary

# Eg:1
d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))




# Characteristics of dictionary  ---->

1) Have to be surrounded by{}.
2) It have to be in the form of key, value pair.
3) It is mutable.
4) Duplicate keys are notb allowed, duplicate values are allowed.
5) It is unindexed.
6) It is ordered.
7) Keys does not allow mutable datatypes, values allow mutable datatype. 



d1={1:100,2:200,3:300,4:400}
# to access the elements in the dictionary
#print(d1)
# OR
# To access the values, have to use key
print(d1[1]) # o/p ---> 100



# Some common functions

d1={1:100,2:200,3:300,4:400}
#len (), min, max()
print(min(d1))
print(max(d1))



# Dictionary based functions
# To add element(key and value pair) in dict

d1 = {1:100, 2:200, 3:300, 4:400}
d1[5]=500
print(d1)



# To replace a value in dictionary
d1={1:100, 2:200, 3:300, 4:400}
d1[2]= "mango"
print(d1)



# Delete element from dictionary 

d1={1:100, 2:200, 3:300, 4:400}
d1.popitem() # --> which is used to delete the last elements
print(d1)



d1={1:100, 2:200, 3:300, 4:400}
d1.pop(2)
print(d1)  # ---> 2 is the key in the dictionary



# join two dictionary

d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)


# get()  ---> used to get a value from a key
d1={1:100, 2:200, 3:300, 4:400}
print(d1[2])
print(d1.get(2))



# To print all the keys

d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys()))


# Iterating dictionary

d1={1:100, 2:200, 3:300, 4:400}
for val1 in d1:  ---> To iterate keys alone
    print(val1)



d1={1:100, 2:200, 3:300, 4:400}
for val in d1.values():  ---> To iterate values alone
    print(val)



# To get both key and values

d1={1:100, 2:200, 3:300, 4:400}
for key, val in d1.items():
    print(key, val)



# ! Problem:1

n = int(input("Enter num of times: "))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value=eval(input("Enter the values: "))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
        
'''

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}














































































'''
#mech_name=["name1","name2","name3"]
#mech_age=[23,22,24]
#mech_mark=[89, 78, 60]
#mech_email=["name@gmail.com","name@gmail.com"]


mech = {
    "student1":{
        "name":"name1"
        "age":24,
        "mark":89,
  },
   "student2":{
        "name":"name2"
        "age":24,
        "mark":89,

  },
   "student3":{
        "name":"name3"
        "age":24,
        "mark":89,
'''        
































