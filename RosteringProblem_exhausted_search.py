import numpy as np

f = open("5_3_1_2.txt", "r")
data = f.readlines()
temp = data[0].split(" ")
N = int(temp[0])
D = int(temp[1])
a = int(temp[2])
b = int(temp[3])

min_target = 10000000
Off = np.zeros([N,D],dtype=int)

for i in range(N) :
    temp = data[i+1].split(" ")
    for j in range(len(temp) - 1) :
        Off[i,int(temp[j]) - 1] = 1

Schedule = np.zeros([N,D], dtype= int)
num_nv = np.zeros(4*D, dtype=int)

def check (d) :
    global num_nv
    for i in range(4) :
        if num_nv[4*d+i] < a or num_nv[4*d+i] > b : 
            return False
    return True
def update() :
    global min_target
    temp = []
    for i in range(N) :
        sum_tmp = 0
        for j in range(D) :
            if Schedule[i,j] == 4 :
                sum_tmp += 1
        temp.append(sum_tmp)
    min_target = min (min_target, max(temp))
            
def Try (n, d) :
    if Off[n,d] == 1 or Schedule[n,max(d-1,0)] == 4 : 
        Schedule[n,d] = 0
        if n == N-1 :
            if check (d) :
                if d < D-1 :
                    Try(0,d+1)
                else :
                    update()
        else :
            Try(n+1, d)

    else :
        for j in range(5) : 
            Schedule[n,d] = j
            if j > 0 :
                num_nv[4*d + j-1] += 1

            if n == N-1 :
                if check (d) :
                    if d < D-1 :
                        Try(0,d+1)
                    else :
                        update()
            else :
                Try(n+1, d)

            if j > 0 :
                num_nv[4*d + j-1] += -1
            Schedule[n,d] = 0

Try (0,0)
print(min_target)
f.close()


