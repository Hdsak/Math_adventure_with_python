A = [[2,3],[5,8]]
B = [[1,4],[8,6]]


def addMatrices(a,b):
    C = [[a[0][0]+b[0][0],a[0][1]+b[0][1]],[a[1][0]+b[1][0],a[1][1]+b[1][1]]]
    return C


def multmatrix(a,b):
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])
    return output

def gauss(A):
    m = len(A)
    n = len(A[0])
    for j,row in enumerate(A):
        if row[j] != 0:
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor
        for i in range(m):
            if i != j:
                addinv = -1*A[i][j]
                for ind in range(n):
                    A[i][ind] += addinv*A[j][ind]
    return A
print(multmatrix([[1,2,-3,-1]], [[4,-1],[-2,3],[6,-3],[1,0]]))

B = [[2,1,-1,8],[-3,-1,2,-1],[-2,1,2,-3]]
print(gauss(B))