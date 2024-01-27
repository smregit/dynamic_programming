def kmpsearch(t,p):
    n=len(t)
    m=len(p)
    pi=computelps(p)
    q=0
    for i in range(n):
        while q>0 and p[q+1]!=t[i]:
            q=pi[q]
        if p[q+1]==t[i]:
            q=q+1
        if q==m:
            print("pattern found")
            q=pi[q]
def computelps(p):
    m=len(p)
    pi=[0]*m
    pi[0]=0
    k=0
    for q in range(2,m):
        while k>0 and p[k+1]!=p[q]:
            k=pi[k]
        if p[k+1]==p[q]:
            k=k+1
            pi[q]=k
    return pi
kmpsearch("ababcabcabababd",'ababd')