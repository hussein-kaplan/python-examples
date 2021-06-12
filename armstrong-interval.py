#  Hussein kaplan - حسين قبلان
#   برنامج بايثون للتحقق من رقم ارمسترونج بين رقمين


lower = 100
upper = 2000

for num in range(lower, upper + 1):

  # ترتيب رقم
   order = len(str(num))
    
 # تهيئة المجموع
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
