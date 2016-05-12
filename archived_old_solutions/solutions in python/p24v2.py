
import time

def GetNthPerm(n):	
    count = 0
    r1 = range(10)
    for i1 in r1:
        r2 = range(10)
        r2.remove(i1)
        for i2 in r2:
            r3 = r2[:]
            r3.remove(i2)
            for i3 in r3:
                r4 = r3[:]
                r4.remove(i3)
                for i4 in r4:
                    r5 = r4[:]
                    r5.remove(i4)
                    for i5 in r5:
                        r6 = r5[:]
                        r6.remove(i5)
                        for i6 in r6:
                            r7 = r6[:]
                            r7.remove(i6)
                            for i7 in r7:
                                r8 = r7[:]
                                r8.remove(i7)
                                for i8 in r8:
                                    r9 = r8[:]
                                    r9.remove(i8)
                                    for i9 in r9:
                                        r10 = r9[:]
                                        r10.remove(i9)
                                        for i10 in r10:
                                            count += 1
                                            if count >= n:
                                                return str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(i10)

print('start')
start = time.time()
print(GetNthPerm(1000000))
print('end')
print(time.time()-start)
