from faker import Faker
import csv
from datetime import date, timedelta
import random

from faker.providers import DynamicProvider

fake = Faker("pl_PL")

def biased_random_int(low, high, bias=0.9):
    if random.random() < bias:
        # generate low number
        return fake.random_int(min=low, max=(low + high) // 8)
    else:
        # generate high number
        return fake.random_int(min=(low + high) // 8 + 1, max=high)

# ilosc_numerow = 1000  # Liczba unikalnych numerów
# zakres = range(100000000, 999999999)
# # Generowanie unikalnych 9-cyfrowych numerów
# unikalne_numery = random.sample(zakres, ilosc_numerow)

dane_pacjenci=[]
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

        writer.writerow([ID_pacjenta, imie, nazwisko, nr_telefonu, miejscowosc, ulica_i_numer_domu, pesel])

dane_recepty=[]
#Recepty
with open("dane_recepty.csv", mode="w", newline="") as recepty_csv:
    writer = csv.writer(recepty_csv)

    for i in range(100):
        ID_recepty = fake.unique.random_int(100000000000000, 999999999999999)
        waznosc = fake.random_int(30, 180, 30)
        czy_wykupiona = fake.boolean()
        data_wystawienia = fake.date_between((date.today() - timedelta(days=180)), date.today())

        writer.writerow([ID_recepty, waznosc, czy_wykupiona, data_wystawienia])

dane_badania=[]
#Badania
with open("dane_badania.csv", mode="w", newline="") as badania_csv:
    writer = csv.writer(badania_csv)

    test_names_provider = DynamicProvider(
        provider_name="test_name",
        elements=[
            "morfologia krwi",
            "tomografia komputerowa",
            "badanie moczu",
            "USG jamy brzusznej",
            "EKG (elektrokardiogram)",
            "EEG (elektroencefalogram)",
            "test na cholesterol",
            "badanie poziomu cukru",
            "badanie wzroku",
            "spirometria",
            "badanie słuchu",
            "próba wysiłkowa",
            "RTG klatki piersiowej",
            "mammografia",
            "test na HIV",
            "badanie poziomu witaminy D",
            "test PSA",
            "badanie TSH (tarczyca)",
            "test na alergie",
            "markery nowotworowe",
            "biopsja skóry",
            "densytometria (gęstość kości)",
            "badanie kału",
            "test wątrobowy",
            "test nerkowy",
            "badanie prostaty",
            "test na anemię",
            "glukoza na czczo",
            "posiew bakteryjny",
            "test na infekcje",
            "badanie hormonów"
        ],
    )

    fake.add_provider(test_names_provider)

    for i in range(100):
        nazwa_badania = fake.test_name()
        czas_trwania = fake.random_int(5, 300, 5)
        koszt = biased_random_int(0, 10000)

        writer.writerow([nazwa_badania, czas_trwania, koszt])

# # Zapis do pliku CSV
# with open("dane.csv", mode="w", newline="") as plik_csv:
#     nazwy_pol = ["id", "nazwa", "cena"]
#     writer = csv.DictWriter(plik_csv, fieldnames=nazwy_pol)
#     writer.writeheader()  # Zapisz nagłówki kolumn
#     writer.writerows(dane)  # Zapisz dane