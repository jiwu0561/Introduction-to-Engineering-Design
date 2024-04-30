def sumNum(*number):
    hap=0
    for num in number:
        hap += num
    return hap
hap = sumNum(1,5)
print("{},{}의 합은 {}이고 ".format(1,5,hap), end="")
hap=sumNum(1,2,3,5)
print("{},{},{},{}의 합은 {}이다.".format(1,2,3,5,hap))