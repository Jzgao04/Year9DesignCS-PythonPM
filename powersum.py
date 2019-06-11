num1,num2 = int(input()),int(input())
def power_sum(num,count,total,pair_count):
    powered_num = num**num2
    if powered_num==total:
        return pair_count+1
    if powered_num < total:
        return power_sum(num+1,count-1,total-powered_num,pair_count) + power_sum(num+1,count,total,pair_count)
    return pair_count
limit=(num1**(1/float(num2)))
print(power_sum(1,limit,num1,0))