# ---  Hussein kaplan - حسين قبلان
# --- برنامج بايثون لايجاد مضروب الرقم باستخدام الدالة العودية

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# --- التاكيد من ان الارقام السالبة
if num < 0:
   print("معذرة ، العامل غير موجود للأرقام السالبة")
# --- التاكد من ان الرقم صفر
elif num == 0:
   print("مضروب 0 هو 1")
# --- ايجاد العامل لاعداد الموجبة
else:
   print("عامل", num, "هو", recur_factorial(num))