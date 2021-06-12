#  Hussein kaplan - حسين قبلان
# 0 برنامج بايثون للتحقق مما إذا كان الرقم موجبًا أم سلبيًا أم 

#  الطريقة الاولى 
num = float(input("ادخل الرقم: "))
if num > 0:
   print("رقم موجب")
elif num == 0:
   print("صفر")
else:
   print("رقم سالب")

# الطريقة الثانية
num = float(input("ادخل الرقم: "))
if num >= 0:
   if num == 0:
       print("صفر")
   else:
       print("رقم موجب")
else:
   print("رقم سالب")