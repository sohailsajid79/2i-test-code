# Task:
# - Iterates in multiples of A until X
# - Then in multiples of A + 1 until 2X
# - Then multiples of A + 2 until 3X

# Assumptions:
    
# In the first phase:
    # A = 1
    # X = 10
    # We're multiplying by 1 and iterating 10 times to reach X
    
# In the second phase:
    # A = the previous A + 1
    # X2 = 20
    # We're multiplying by 2 and iterating 10 times to reach X2
    
# In the third phase:
    # A = the previous A + 2
    # X2 = 40
    # We're multiplying by 2 and iterating 10 times to reach X3

# Code: 
A = 1
X = 10

for i in range (1,4):
    for j in range (1,11):
        print(f"{A}*{j} = {A*j}")
    A += A
    print("----")

# Output:
    # 1*1 = 1
    # 1*2 = 2
    # 1*3 = 3
    # 1*4 = 4
    # 1*5 = 5
    # 1*6 = 6
    # 1*7 = 7
    # 1*8 = 8
    # 1*9 = 9
    # 1*10 = 10
    # ---
    # 2*1 = 2
    # 2*2 = 4
    # 2*3 = 6
    # 2*4 = 8
    # 2*5 = 10
    # 2*6 = 12
    # 2*7 = 14
    # 2*8 = 16
    # 2*9 = 18
    # 2*10 = 20
    # ---
    # 4*1 = 4
    # 4*2 = 8
    # 4*3 = 12
    # 4*4 = 16
    # 4*5 = 20
    # 4*6 = 24
    # 4*7 = 28
    # 4*8 = 32
    # 4*9 = 36
    # 4*10 = 40
    #---
