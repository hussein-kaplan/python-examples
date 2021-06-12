# ---  Hussein kaplan - حسين قبلان
# --- برنامج بايثون للعثور على مجموع الأعداد الطبيعية باستخدام العودية


def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# --- قم بتغيير هذه القيمة لنتيجة مختلفة
num = 16

if num < 0:
   print("ادخل عدد موجب")
else:
   print("المجموع",recur_sum(num))
