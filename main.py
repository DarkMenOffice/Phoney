#!/usr/bin/env python3
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init

# تهيئة مكتبة colorama
init(autoreset=True)

def analyze_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid phone number."}

        # استخراج البيانات
        country = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)

        number_type = phonenumbers.number_type(parsed_number)
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            number_type_str = "Mobile"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            number_type_str = "Fixed line"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            number_type_str = "Fixed line or Mobile"
        else:
            number_type_str = "Other"

        # إعادة البيانات كقائمة منسقة
        return {
            "valid": True,
            "country": country,
            "service_provider": service_provider,
            "timezones": list(timezones),
            "type": number_type_str
        }

    except phonenumbers.NumberParseException as e:
        return {"error": str(e)}

def main():
    # عرض شعار الأداة واسمها مع ألوان
    print(Fore.CYAN + """
    =============================
        Welcome to Phoney!
    =============================
    """ + Fore.GREEN + "A simple tool to analyze phone numbers Made by Dark Men Office.\n")
    time.sleep(2)

    while True:
        # إدخال الرقم من المستخدم
        phone_number = input(Fore.YELLOW + "Enter a phone number with the country code (e.g., +1XXXXXXXXXX): ")

        # إظهار رسالة تحميل مع ألوان
        print(Fore.BLUE + "\nAnalyzing phone number...")
        for i in range(1):
            time.sleep(1)
            print(Fore.MAGENTA + "Loading" + "." * (i + 1))
        
        # تحليل الرقم وإظهار النتائج مع ألوان
        result = analyze_phone_number(phone_number)
        print(Fore.CYAN + "\nResults:")
        print(Fore.LIGHTBLUE_EX + "====================================")
        for key, value in result.items():
            color = Fore.GREEN if key != "error" else Fore.RED
            print(color + f"{key.capitalize()}: {value}")
        print(Fore.LIGHTBLUE_EX + "====================================")

        # خيارات للمستخدم مع ألوان
        print(Fore.YELLOW + "\nOptions:")
        print(Fore.LIGHTGREEN_EX + "1. Analyze another number")
        print(Fore.LIGHTRED_EX + "2. Exit")
        choice = input(Fore.WHITE + "Enter your choice (1 or 2): ")

        if choice == "2":
            print(Fore.LIGHTCYAN_EX + "Thank you for using Phoney! Goodbye!")
            break
        elif choice != "1":
            print(Fore.RED + "Invalid choice! Exiting.")
            break

if __name__ == "__main__":
    main()
