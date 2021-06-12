#  Hussein kaplan - حسين قبلان
# برنامج بايثون لإيجاد مجموع الأعداد الطبيعية


num = 16

if num < 0:
   print("أدخل رقمًا موجبًا")
else:
   sum = 0
   # استخدم while loop للتكرار حتى الصفر
   while(num > 0):
       sum += num
       num -= 1
   print("المجموع", sum)
