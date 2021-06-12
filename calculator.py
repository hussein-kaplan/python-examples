# ---  Hussein kaplan - حسين قبلان
# --- برنامج بايثون لعمل آلة حاسبة بسيطة


# --- نستخدم هذه الوظيفة لجمع رقمين
def add(x, y):
    return x + y

# --- نستخدم هذه الوظيفة لطرح بين الرقمين
def subtract(x, y):
    return x - y

# --- نستخدم هذه الوظيفة لعملية الضرب بين الرقمين
def multiply(x, y):
    return x * y

# --- نستخدم هذه الوظيفة لعملية القسمة بين الرقمين
def divide(x, y):
    return x / y


print("اختر احد الخيارات.")
print("1.جمع")
print("2.طرح")
print("3.ضرب")
print("4.قسمة")

while True:
    # --- اخد الاختيار من المستخدم
    choice = input("اختر احد الارقام(1/2/3/4): ")

    # --- التاكيد من ان الاختيار هو من احد هذا الارقام
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("ادخل الرقم الاول: "))
        num2 = float(input("ادخل الرقم الثاني: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("اختيار خاطى")