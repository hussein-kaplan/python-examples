#  Hussein kaplan - حسين قبلان
# برنامج بايثون للتحقق مما إذا كان السنة كبيسة ام لا

year = 2000

# للحصول على السنة (الرقم) من المستخدم
# year = int(input("ادخل السنة: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} هي سنة كبيسة".format(year))
       else:
           print("{0} ليست سنة كبيسة".format(year))
   else:
       print("{0} هي سنة كبيسة".format(year))
else:
   print("{0} ليست سنة كبيسة".format(year))
