import requests

# Links to ECB-course

currencies_dict = {
    1: ("EUR", "placeholder"),
    2: ("USD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html"),
    3: ("JPY", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-jpy.en.html"),
    4: ("GBP", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-gbp.en.html"),
    5: ("CHF", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-chf.en.html"),
    6: ("CNY", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-cny.en.html"),
    7: ("CAD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-cad.en.html"),
    8: ("AUD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-aud.en.html"),
    9: ("NZD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-nzd.en.html"),
    10: ("SEK", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-sek.en.html"),
    11: ("NOK", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-nok.en.html"),
    12: ("DKK", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-dkk.en.html"),
    13: ("HKD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-hkd.en.html"),
    14: ("SGD", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-sgd.en.html"),
    15: ("KRW", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-krw.en.html"),
    16: ("INR", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-inr.en.html")
}

printable_currencies_dict = (
    "(1)  EUR - European Euro\n"
    "(2)  USD - United States Dollar\n"
    "(3)  JPY - Japanese Yen\n"
    "(4)  GBP - British Pound Sterling\n"
    "(5)  CHF - Swiss Franc\n"
    "(6)  CNY - Chinese Yuan Renminbi\n"
    "(7)  CAD - Canadian Dollar\n"
    "(8)  AUD - Australian Dollar\n"
    "(9)  NZD - New Zealand Dollar\n"
    "(10) SEK - Swedish Krona\n"
    "(11) NOK - Norwegian Krone\n"
    "(12) DKK - Danish Krone\n"
    "(13) HKD - Hong Kong Dollar\n"
    "(14) SGD - Singapore Dollar\n"
    "(15) KRW - South Korean Won\n"
    "(16) INR - Indian Rupee"
)


# Get the link for the given currency (to expand, just add new dict entry and add to the printable currencies dict)

def get_given_currency():
    print(printable_currencies_dict)

    try:
        user_choice = int(input("Select the currency you want to convert FROM: "))
        if user_choice in currencies_dict:
            currency_name, currency_link = currencies_dict[user_choice]
            return currency_name, currency_link
        else:
            print(f"\n - Invalid choice. Please select a number between 1 and {len(currencies_dict)}. - \n")
            return get_given_currency()
    except:
        print("\n - Invalid input. Please enter the number corresponding to your currency choice! - \n")
        return get_given_currency()


def get_desired_currency():
    print(printable_currencies_dict)

    try:
        user_choice = int(input("Select the currency you want to convert TO: "))
        if user_choice in currencies_dict:
            currency_name, currency_link = currencies_dict[user_choice]
            return currency_name, currency_link

        else:
            print(f"\n - Invalid choice. Please select a number between 1 and {len(currencies_dict)}. - \n")
            return get_desired_currency()
    except:
        print("\n - Invalid input. Please enter the number corresponding to your currency choice! - \n")
        return get_desired_currency()


def get_conversion_rate(link):
    # ECB-Kurs

    response = requests.get(link)

    if response.status_code == 200:
        if "rateLatestInverse" in response.text:
            phrase_start1 = response.text.find("rateLatestInverse")
            phrase_end1 = response.text.find(";", phrase_start1)
            extracted_text = response.text[phrase_start1:phrase_end1].strip()
            clean_extracted_text = extracted_text.replace("rateLatestInverse=", "").replace("'", "")
            conversion_value = float(clean_extracted_text)
            if "dateLatestInverse" in response.text:
                phrase_start2 = response.text.find("dateLatestInverse")
                phrase_end2 = response.text.find(";", phrase_start2)
                extracted_date = response.text[phrase_start2:phrase_end2].strip()
                clean_extracted_date = extracted_date.replace("dateLatestInverse=", "").replace("'", "")

                return conversion_value, clean_extracted_date
        else:
            print("\n - Could not retrieve the currency conversion rate from the website. - \n")
    else:
        print(f"\n - Website is not responding. Error code: {response.status_code} - \n")


def conversion(conversion_rate_to_EUR, conversion_rate_to_desired_currency, given_currency_name, desired_currency_name):

    try:
        original_amount = float(input(f"Enter the amount in {given_currency_name}: ").replace(",", "."))
        new_amount = (original_amount * conversion_rate_to_EUR) * conversion_rate_to_desired_currency
        output = f"{original_amount:.2f} {given_currency_name} is equivalent to {new_amount:.2f} {desired_currency_name}"
        print("\n " + "-" * (len(output) + 2) + " ")
        print(f"| {output} |")
        print(" " + "-" * (len(output) + 2) + " \n")

    except:
        print("\n - Invalid amount entered! Please try again. - \n")
        conversion(conversion_rate_to_EUR, conversion_rate_to_desired_currency, given_currency_name, desired_currency_name)


# Program structure

# Ask for both currencies

given_currency_name, given_currency_link = get_given_currency()
desired_currency_name, desired_currency_link = get_desired_currency()

if given_currency_name != "EUR":
    conversion_rate_to_EUR, rate_date1 = get_conversion_rate(given_currency_link)
else:
    conversion_rate_to_EUR = 1
if desired_currency_name != "EUR":
    tmp_conversion_rate, rate_date2 = get_conversion_rate(desired_currency_link)
    conversion_rate_to_desired_currency = 1 / tmp_conversion_rate

else:
    conversion_rate_to_desired_currency = 1

conversion(conversion_rate_to_EUR, conversion_rate_to_desired_currency, given_currency_name, desired_currency_name)
