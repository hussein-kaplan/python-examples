#  Hussein kaplan - حسين قبلان
# برنامج بايثون للعثور على  
# HCF لرقمين

# تحديد وظيفة
def compute_hcf(x, y):

# اختر الرقم الأصغر
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("ال H.C.F. هو", compute_hcf(num1, num2))

# الطريقة الثانية  التقليدية
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("ال HCF هو", hcf)