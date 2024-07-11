def menu():
    print('رمز نگاری : [1]')
    print('رمز گشایی : [2]')
    print('خروج از برنامه : [3]')
    print('_' * 40)

    try:
        choice = int(input('درخواست خود را ارسال نمایید :    '))
        if choice in [1, 2, 3]:
            print('_' * 40)
            return choice
        else:
            print('لطفاً یک عدد معتبر بین 1 و 3 وارد کنید.')
    except ValueError:
        print('ورودی نامعتبر است. لطفاً یک عدد وارد کنید.')


while True:

    choice = menu()

    match choice:
        case 1:
            plain_Text = input("متن : ")  # ورودی متن رمز گذاری
            encrypted_Text = ""  # ذخیره کننده متن رمز گذاری شده
            for index in plain_Text:
                formula = chr(ord(index) * 2 + 5)
                encrypted_Text += formula

            print(encrypted_Text)
        case 2:
            encrypted_Text = input('متن رمز گذاری شده را وارد نمایید : ')
            plain_Text = ""
            for index in encrypted_Text:
                formula = (ord(index) - 5) // 2
                plain_Text += chr(formula)

            print(plain_Text)

        case 3:
            print('برنامه بسته شد')
            break

        case _:
            print('مقدار وارد شده خارج از بازه عدد 1 تا 3 است')
