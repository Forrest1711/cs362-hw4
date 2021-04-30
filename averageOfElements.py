def avgElem(arr):
    count = 0
    avg = 0
    for i in arr:
        count = count+1
        avg = avg + i
    if count == 0:
        return 0
    else:
        return avg/count
