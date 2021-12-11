
def compareStrings(s1, s2, s3):
    # Write your code here
        d = []
        s=""
        d.append(s1)
        d.append(s2)
        d.append(s3)
        d.sort()
        for i in d:
            s=s+i
        return s



print(compareStrings('eiweo','ghueb','dvhbeibviw'))