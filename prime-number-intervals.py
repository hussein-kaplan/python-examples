#  Hussein kaplan - حسين قبلان
#  برنامج بايثون لطباعة جميع الأرقام الأولية بين رقمين محددين  


lower = 900
upper = 1000

print("الأعداد الأولية بين", lower, "و", upper, "هو:")

for num in range(lower, upper + 1):
   # جميع الأعداد الأولية أكبر من 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)