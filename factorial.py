#  Hussein kaplan - حسين قبلان
# برنامج بايثون لإيجاد عاملي الرقم 


# قم بتغيير القيمة لنتيجة مختلفة
num = 7

# لأخذ المدخلات من المستخدم
#num = int(input("اكتب الرقم: "))

factorial = 1

# تحقق مما إذا كان الرقم سالبًا أم موجبًا أم صفرًا
if num < 0:
   print("معذرة ، العامل غير موجود للأرقام السالبة")
elif num == 0:
   print("مضروب 0 هو 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("عامل",num,"هو",factorial)