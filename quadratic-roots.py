#  Hussein kaplan - حسين قبلان
# برنامج بايثون لحل المعادلة التربيعية
# حل المعادلة التربيعية ax ** 2 + bx + c = 0

# استيراد وحدة الرياضيات المعقدة
import cmath

a = 1
b = 5
c = 6

# احسب المميز
d = (b**2) - (4*a*c)

# أيجاد حلين
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('الحل {0} و {1}'.format(sol1,sol2))