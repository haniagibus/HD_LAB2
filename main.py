from faker import Faker
from faker.providers import DynamicProvider
import csv
import random
import string

specjalization_provider = DynamicProvider(
     provider_name="medical_specialization",
     elements=[ "Kardiolog", "Pediatra", "Ginekolog", "Dermatolog", "Neurolog",
    "Ortopeda", "Chirurg", "Psychiatra", "Endokrynolog", "Onkolog",
    "Okulista", "Laryngolog", "Reumatolog",
    "Urolog", "Chirurg plastyczny", "Chirurg naczyniowy", "Medycyna rodzinna",
    "Medycyna pracy", "Medycyna sportowa", "Pneumolog", "Immunolog",
    "Patolog", "Radiolog", "Nefrolog", "Ginekolog-onkolog",
    "Ortopeda dziecięcy", "Medycyna ratunkowa"],
)

fake = Faker("pl_PL")
fake.add_provider(specjalization_provider)

def generate_unique_identifier(existing_ids, length=12):
    """Generuje unikalny identyfikator o podanej długości."""
    while True:
        identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if identifier not in existing_ids:  # Sprawdzenie, czy identyfikator jest unikalny
            existing_ids.add(identifier)
            return identifier

existing_ids = set()

#Pacjenci
with open("dane_pacjenci.csv", mode="w", newline="") as pacjenci_csv:
    writer = csv.writer(pacjenci_csv)

    for i in range(100):
        ID_pacjenta = fake.unique.random_int(100000000, 999999999)
        imie = fake.first_name()
        nazwisko = fake.last_name()
        nr_telefonu = fake.phone_number()
        miejscowosc = fake.city()
        ulica_i_numer_domu = fake.street_address()
        pesel = fake.unique.random_int(10000000000, 99999999999)

        writer.writerow([ID_pacjenta, imie, nazwisko, nr_telefonu, miejscowosc,ulica_i_numer_domu,pesel])


#Lekarze
with open("dane_lekarze.csv", mode="w", newline="") as lekarze_csv:
    writer = csv.writer(lekarze_csv)
    for i in range(100):
        Identyfikator = generate_unique_identifier(existing_ids)
        imie = fake.first_name()
        nazwisko = fake.last_name()
        specjalizacja = fake.medical_specialization()
        writer.writerow([Identyfikator, imie, nazwisko,specjalizacja])