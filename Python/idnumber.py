id=input("Please input your ID number: ")
id_list=list(id)
id.split()
sum_l=[]
if len(id_list)!=8:
    print('Invalid')
else:
    for j in range(0,len(id_list)):
        id_sum=int(id_list[j])*(len(id_list)-j)
        sum_l.append(id_sum)
    total_sum=sum(sum_l)
    if total_sum%11==0:
        print("You're a real lasallian!")
    else:
        print("You are not a real lasallian dude pare chong")
      
    

