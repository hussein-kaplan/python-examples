#  Hussein kaplan - حسين قبلان
# برنامج بايثون لطباعة تسلسل فيبوناتشي


#  n برنامج لعرض تسلسل فيبوناتشي حتى الحد
nterms = int(input("كم عدد المصطلحات? "))

# أول فترتين
n1, n2 = 0, 1
count = 0

# تحقق مما إذا كان عدد المصطلحات صالحًا
if nterms <= 0:
   print("الرجاء إدخال عدد صحيح موجب")
elif nterms == 1:
   print("تسلسل فيبوناتشي يصل",nterms,":")
   print(n1)
else:
   print("متتالية فيبوناتشي:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # قيم التحديث
       n1 = n2
       n2 = nth
       count += 1