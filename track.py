import phonenumbers
from phonenumbers import geocoder

phone_numbers1 = phonenumbers.parse("+91__________")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_numbers1,"en"));