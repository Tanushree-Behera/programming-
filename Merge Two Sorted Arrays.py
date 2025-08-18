def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    mergedList = arr1 + arr2
    arrlen = len(mergedList)
    
    for i in range(arrlen):
        for j in range(i+1 , arrlen):
            if mergedList[i] > mergedList[j]:
                temp = mergedList[i]
                mergedList[i] = mergedList[j]
                mergedList[j] = temp
                
    print(mergedList)          

if __name__ == "__main__":
    arr1 = [9, 2, 1, 6]
    arr2 = [3, 7, 0, 4]
    
    merge(arr1,arr2)
