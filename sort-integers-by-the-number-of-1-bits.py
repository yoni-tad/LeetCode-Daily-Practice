def sortByBit():
    arr = [1024,512,256,128,64,32,16,8,4,2,1] #[1,2,4,8,16,32,64,128,256,512,1024]
    
    def count_ones(num):
        bi = bin(num).count('1')
        return (bi, num)
    arr.sort(key=count_ones)

    return arr

print(sortByBit())