# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import openpyxl
from faker import Faker
import random
import string

from faker.providers import DynamicProvider

stanowisko_provider = DynamicProvider(
    provider_name="position",
    elements=["recepcja", "lekarz", "personel medyczny", "pielęgniarka"]
)
fake = Faker("pl_PL")
fake.add_provider(stanowisko_provider)


def generate_unique_identifier(existing_ids, length):
    """Generuje unikalny identyfikator o podanej długości."""
    while True:
        identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if identifier not in existing_ids:  # Sprawdzenie, czy identyfikator jest unikalny
            existing_ids.add(identifier)
            return identifier


# stworzenie excela i aktywacja arkusza
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Pracownicy"

naglowki = ["Identyfikator", "PESEL", "Imie", "Nazwisko", "Data urodzenia", "Stanowisko", "Data zatrudnienia",
            "Data zwolnienia"]
sheet.append(naglowki)

existing_ids = set()

for _ in range(1000):
    ID = generate_unique_identifier(existing_ids, 12)
    PESEL = fake.unique.random_int(10000000000, 99999999999)
    imię = fake.first_name()
    nazwisko = fake.last_name()
    data_urodzenia = fake.date_between(start_date=datetime.strptime('1955-01-01', '%Y-%m-%d').date(),end_date=datetime.strptime('2000-01-01', '%Y-%m-%d').date())
    stanowisko = fake.position()
    data_zatrudnienia = fake.date_between(data_urodzenia + timedelta(days=8760),end_date=datetime.strptime('2024-01-01', '%Y-%m-%d'))
    data_zwolnienia = fake.date_between(data_zatrudnienia, end_date=datetime.strptime('2024-01-01', '%Y-%m-%d'))

    wiersz = [ID, PESEL, imię, nazwisko, data_urodzenia, stanowisko,data_zatrudnienia, data_zwolnienia]
    sheet.append(wiersz)
workbook.save("pracownicy.xlsx")
