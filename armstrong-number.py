#  Hussein kaplan - حسين قبلان
# برنامج بايثون للتحقق من رقم ارمسترونج


# أخذ المدخلات من المستخدم
num = int(input("اكتب  رقم: "))

# تهيئة المجموع
sum = 0

# أوجد مجموع مكعب كل رقم
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# عرض النتيجة
if num == sum:
   print(num,"هو رقم ارمسترونج")
else:
   print(num,"ليس رقم ارمسترونغ")