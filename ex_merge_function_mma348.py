def merge(listA, listB):

    merg = []
    indA = 0
    indB = 0
    lstAn = int(len(listA))
    lstBn=int(len(listB))
    while indA < lstAn and indB < lstBn:

        if listB[indB] < listA[indA]:
            merg.append(listB[indB])
            indB = indB + 1

        else:
            merg.append(listA[indA])
            indA = indA + 1

    while indA == lstAn and indB < lstBn:
        merg.append(listB[indB])
        indB = indB + 1

    while indB == lstBn and indA < lstAn:
        merg.append(listA[indA])
        indA = indA + 1


    return merg


    
listA =[1,2,5]
listB =[3, 4, 6, 8 ]

print("A:", listA, "", "B:", listB)

pear = merge(listA,listB)

print(pear)
