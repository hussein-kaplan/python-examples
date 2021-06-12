#  Hussein kaplan - حسين قبلان
#  برنامج بايثون للعثور على أكبر ثلاثة أرقام 


# قم بتغيير قيم num1 و num2 و num3
# لنتيجة مختلفة
num1 = 10
num2 = 14
num3 = 12
# الغاء تعليق  الأسطر التالية  لأخذ ثلاثة أرقام من المستخدم
#num1 = float(input("اكتب الرقم الاول: "))
#num2 = float(input("اكتب الرقم الثاني: "))
#num3 = float(input("اكتب الرقم الثالث: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("الرقم الاكبر هو", largest)
