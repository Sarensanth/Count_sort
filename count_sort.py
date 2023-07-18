def count_sort(array):

    maxi=max(array)
    count=[0]*(maxi+1)

    for i in array:
        count[i]+=1

    result=[]
    for i in range(len(count)):
        result.extend(count[i]*[i])
    return result

array=list(map(int,input().split()))
print(count_sort(array))

