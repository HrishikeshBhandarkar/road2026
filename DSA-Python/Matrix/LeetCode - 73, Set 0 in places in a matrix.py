
def tra(nums):
        n=len(nums)
        m=len(nums[0])
        save=list()
        for i in range(n):
            for j in range(m):
                if nums[i][j]==0:
                    save.append([i,j])
        for i in save:
                    k=i[0]
                    j=i[1]
                    nums[k]=[0]*m
                    for p in range (n):
                        nums[p][j]=0
        return nums


nums=[[7,10,29,2],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
print(nums)
u=tra(nums)
print(u)



