from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime, timedelta
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

def generate_unique_identifier(existing_ids, length):
    """Generuje unikalny identyfikator o podanej długości."""
    while True:
        identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if identifier not in existing_ids:  # Sprawdzenie, czy identyfikator jest unikalny
            existing_ids.add(identifier)
            return identifier

def generate_random_time_within_range(start_hour=7, end_hour=19):
    """Generuje losowy czas w przedziale od start_hour do end_hour."""
    hour = random.randint(start_hour, end_hour)
    minute = random.choice([0, 10, 20, 30, 40, 50])
    return f"{hour:02d}:{minute:02d}"


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
        Identyfikator = generate_unique_identifier(existing_ids,12)
        imie = fake.first_name()
        nazwisko = fake.last_name()
        specjalizacja = fake.medical_specialization()
        writer.writerow([Identyfikator, imie, nazwisko,specjalizacja])

#Wizyty
start_date = datetime.strptime('2020-01-01','%Y-%m-%d').date()
end_date = datetime.strptime('2024-01-01', '%Y-%m-%d').date()

recepcjonistki=[]
for i in range(20):
    recepcjonistki.append(generate_unique_identifier(existing_ids,12))

with open("dane_wizyty.csv", mode="w", newline="") as wizyty_csv:
    writer = csv.writer(wizyty_csv)
    for i in range(1000):
        ID_wizyty = generate_unique_identifier(existing_ids,10)
        data_umówienia = fake.date_between(start_date=start_date,end_date=end_date)
        data_rozpoczęcia = fake.date_between(start_date= data_umówienia,end_date=data_umówienia + timedelta(days=180))
        dolegliwosci=""
        kwota=round(random.uniform(40, 600), 2)
        godzina = generate_random_time_within_range()
        czy_odbyta = random.choices(["TAK", "NIE"], weights=[0.7, 0.3], k=1)[0]
        ID_recepcjonistki= random.choice(recepcjonistki)
        writer.writerow([ID_wizyty, data_umówienia,data_rozpoczęcia,dolegliwosci, kwota, godzina,czy_odbyta,ID_recepcjonistki])