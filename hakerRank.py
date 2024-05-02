# 1
# def timeConversion(s):
#     # Write your code here
#     arr = s.split(':')
#     zone = arr[2][2:4]
#     sec = arr[2][0:2]
#     mint = arr[1]
#     hour = arr[0]
#     if zone == "AM":
#         if int(hour)==12:
#             return "00" + ":" + mint + ":" + sec
#         if int(hour)<12:
#             return hour + ":" + mint + ":" + sec
#     if zone=="PM":
#         if int(hour)==12:
#             return hour + ":" + mint + ":" + sec
#         else: return str(int(hour)+12) + ":" + mint + ":" + sec
#     else:
#         return "error"
# print(timeConversion("1:00:00AM"))
#------------------------------------------------
# 2
# def gradingStudents(grades):
#     # Write your code here
#     roundedGrads = []
#     for i in range(len(grades)):
#             if grades[i]<38:
#                   roundedGrads.insert(i,grades[i])
#             else:
#                   if(5-grades[i]%5<3):
#                      print(5-grades[i]%5)
#                      test= 5-grades[i]%5
#                      roundedGrads.insert(i,grades[i]+test)
#                   else:
#                         roundedGrads.insert(i,grades[i])      
  
#     return roundedGrads      

# print(gradingStudents([75,67,40,33,38]))
#------------------------------------------------
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     # Write your code here
#     applesLocation = []
#     orangesLocation = []
#     applesCount =0
#     orangesCount = 0
#     for i in range(len(apples)):
#         applesLocation.insert(i,apples[i]+a)
#     for v in range(len(oranges)):
#         orangesLocation.insert(v,oranges[v]+b)    
#     for e in range(len(applesLocation)):
#         if applesLocation[e] >= s and applesLocation[e] <= t:  
#          applesCount+=1
#     for f in range(len(orangesLocation)):
#         if orangesLocation[f] >= s and orangesLocation[f] <= t:  
#          orangesCount+=1     
#     print(applesCount)
#     print(orangesCount)

# apples = [-2 ,2 ,1]
# oranges = [5 ,-6]
# countApplesAndOranges(7,11,5,15,apples,oranges)
#------------------------------------------------
# def kangaroo(x1, v1, x2, v2):
#     # Write your code here
#     p1 = x1
#     p2 = x2
#     counter = 0
#     while 1:
#         p1+=v1
#         p2+=v2
#         if p1==p2:
#             return "YES"
#         else: 
#             counter+=1
#             if counter == 10000:
#                 return "No"


# kangaroo(0,2,5,3)
#------------------------------------------------
# def birthday(s, d, m):
#     # Write your code here
#     counter=0
#     for value in range(len(s)-m+1):
#         if len(s[value:value+m]) == m:
#             count=0
#             for item in range(len(s[value:value+m])):
#                 count+=s[value:value+m][item]
#         if count == d:
#             counter+=1  
#     return counter  

# values = [1,2,1,3,2]
# print(birthday(values,3,2))
#------------------------------------------------
# def breakingRecords(scores):
#     # Write your code here
#     min = scores[0]
#     min_counter = 0
#     max_counter = 0
#     max = scores[0]
#     for i in range(len(scores)):
#         if scores[i]<min:
#             min=scores[i]
#             min_counter +=1
#         if scores[i]>max:
#             max = scores[i]  
#             max_counter+=1  
#     print(max_counter,min_counter)

# scores = [3,4,21,36,10,28,35,5,24,42]
# breakingRecords(scores)
#------------------------------------------------
# def divisibleSumPairs(n, k, ar):
#     # Write your code here
#     counter = 0
#     for i in range(len(ar)):
#      for d in range(i+1,len(ar)):
#         if (ar[i]+ar[d])%k == 0:
#            counter+=1
#     return counter   

# n=6
# k=3
# ar = [1, 3, 2, 6, 1, 2]

# divisibleSumPairs(n,k,ar)
#------------------------------------------------
# def migratoryBirds(arr):
#     # Write your code here
#     custome_array = [0] * 5
#     counter_array = [0] * 5
#     for i in range(len(custome_array)):
#         custome_array[i] = i+1
#     for d in range(len(arr)):
#         for c in range(len(custome_array)):
#             print(arr[d],custome_array[c])
#             if arr[d] == custome_array[c]:
#                 counter_array[c]+=1
#     print(counter_array)
#     max = 0
#     for v in range(len(counter_array)):
#         if max<counter_array[v]:
#             max = v
#     return v

# arr = [1,4,4,4,5,3]
# migratoryBirds(arr)
#------------------------------------------------

