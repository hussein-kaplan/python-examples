#  Hussein kaplan - حسين قبلان
# برنامج بايثون لتحويل الكيلومترات إلى أميال

# أخذ مدخلات الكيلومترات من المستخدم
kilometers = float(input("أدخل القيمة بالكيلومترات: "))

# عامل التحويل
conv_fac = 0.621371

# احسب الأميال
miles = kilometers * conv_fac
print('%0.2f كيلومترات يساوي %0.2f اميال' %(kilometers,miles))
