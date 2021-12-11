import random
import time
names = ["sunny","vinny","chinny","bunny"]
subjects =["pyhthon","java","BlockChain"]
def people_list(num_people):
    results =[]
    for i in range(num_people):
        person ={"id":i,"names":random.choice(names),"sub":random.choice(subjects)}
        results.append(person)
        return results
def gen(num_people):
    for i in range(num_people):
        person ={"id":i,"names":random.choice(names),"sub":random.choice(subjects)}
        yield person
t1 =time.perf_counter()
people =people_list(1000000)
t2 = time.perf_counter()

'''t1 =time.perf_counter()
g =gen(100000)
t2 = time.perf_counter()'''
print(t1)
print(t2)
print(t2-t1)
