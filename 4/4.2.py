def main():
  counter = 0
  result = set()
  lowerbound = 357253
  upperbound = 892942
  for i in range(int(str(lowerbound)[0]), int(str(upperbound)[0]) + 1):
    for j in range(i,10):
      for k in range(j,10):
        for l in range(k,10):
          for m in range(l, 10):
	    for n in range(m, 10):
	      if(i==j or j==k or k==l or l==m or m==n):
	        number = 100000 * i + 10000*j + 1000*k + 100*l + 10*m +n
     		if(number >= lowerbound and number <= upperbound and checkCorrectDoubles(i,j,k,l,m,n)):
		  result.add(number)
  print len(result)
  print(result)


def checkCorrectDoubles(i,j,k,l,m,n):
  return (i==j and j!=k) or (i!=j and j==k and k!=l) or (j!=k and k==l and l!=m) or (k!=l and l==m and m!=n) or (l!=m and m==n)

main()	
