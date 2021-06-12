# ---  Hussein kaplan - حسين قبلان
# --- برنامج بلغة البايثون لتحويل الرقم العشري إلى رقم ثنائي باستخدام دالة تكرارية 

# --- انشاء الفانكشن 
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# عدد عشري
dec = 34
# --- طباعة الناتج
print(convertToBinary(dec))
