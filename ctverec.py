def closest(lst, K):

    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

# Driver code
lst = [10, 15, 20, 40, 100, 1000]
K = 120
test= (closest(lst, K))
print(test)




