#---  Hussein kaplan - حسين قبلان
#---  برنامج بايثون للعثور على المضاعف المشترك الأصغر لرقمين وعرضه

def compute_lcm(x, y):

# --- اختر الرقم الأكبر
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("المضاعف المشترك الاصغر للرقمين هو", compute_lcm(num1, num2))