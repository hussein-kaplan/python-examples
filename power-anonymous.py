#  Hussein kaplan - حسين قبلان
# برنامج بايثون لعرض صلاحيات 2 باستخدام وظيفة مجهولة


terms = 10
#  الغاء تعليق الكود أدناه لأخذ مدخلات من المستخدم
# terms = int(input("كم عدد المصطلحات ؟ "))

# استخدام وظيفة مجهولة
result = list(map(lambda x: 2 ** x, range(terms)))

print("مجموع الشروط:",terms)
for i in range(terms):
   print("2 رفع إلى الاس",i,"هو",result[i])
