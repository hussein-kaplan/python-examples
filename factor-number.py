# ---  Hussein kaplan - حسين قبلان
# --- برنامج بايثون لإيجاد عوامل الرقم


# تحسب هذه الوظيفة عامل الوسيطة التي تم تمريرها
def print_factors(x):
   print("عوامل",x,"هو:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320
# --- طباعة عوامل الرقم
print_factors(num)