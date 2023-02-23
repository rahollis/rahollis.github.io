#%%
import numpy as np
import random
#%%
def GenerateRandomREF(m,n):
    ref = np.random.randint(-10,11,(m,n))
    ref[0,0] = 1
    ref[1:,:1] = np.zeros((m-1,1))
    k = min(m,n)
    for i in range(1,k):
        if random.random() < 1-(1/k)**1.3:
            ref[i,i] = 1
            ref[i+1:,i:i+1] = np.zeros((m-i-1,1))
        else:
            ref[i:,i:i+1] = np.zeros((m-i,1))
    return ref
#%%
def PrintSystem(system,num_decimal):
    m,n = np.shape(system)
    rounded_system = np.round_(system,num_decimal)
    display = ' _' + ' '*((5+num_decimal)*n) + '  _\n'
    for i in range(m):
        display += '|'
        for j in range(n-1):
            entry = str(rounded_system[i,j])
            display += ' '*((5+num_decimal)-len(entry)) + entry
        entry = str(rounded_system[i,n-1])
        display += ' |' + ' '*((5+num_decimal)-len(entry)) + entry + '  |\n'
    display = display[:-(5+num_decimal)*n-6] + '_' + display[-(5+num_decimal)*n-5:-3] + '_' + display[-2:]
    print(display)
#%%
def GaussianElimination(m,n):
    system = 1.0*np.matmul(np.random.randint(-3,4,(m,m)),GenerateRandomREF(m,n))
    PrintSystem(system,1)
    while True:
        user_input = input('Type a row operation.  Use the syntax type,row operation, e.g.: 3,-8*R1+R3->R3. ')
        if user_input == '':
            break
        try:
            op_type,row_op = user_input.split(',')
            op,target_row = row_op.split('->')
            target_row = int(target_row.replace('R',''))-1
            if op_type == '3':
                coeff,rest = op.split('*')
                if '/' in coeff:
                    coeff = coeff.strip('()')
                    numerator,denominator = coeff.split('/')
                    coeff = round(float(numerator)/float(denominator),2)
                coeff = float(coeff)
                pivot_row,rest = rest.split('+')
                pivot_row = int(pivot_row.replace('R',''))-1
                system[target_row] += coeff*system[pivot_row]
                PrintSystem(system,1)
            elif op_type == '2':
                coeff,rest = op.split('*')
                if '/' in coeff:
                    coeff = coeff.strip('()')
                    numerator,denominator = coeff.split('/')
                    coeff = float(numerator)/float(denominator)
                coeff = float(coeff)
                system[target_row] = coeff*system[target_row]
                PrintSystem(system,1)
            elif op_type == '1':
                pivot_row = int(op.replace('R',''))-1
                temp = np.copy(system[target_row])
                system[target_row] = system[pivot_row]
                system[pivot_row] = temp
                PrintSystem(system,1)
            else:
                print('Please indicate the row operation type.')
        except:
            print('Check your input format and try again.')