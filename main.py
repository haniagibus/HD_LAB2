from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime, timedelta
import csv
from datetime import date, timedelta
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

my_sentence_list = [
    'Pacjenta boli brzuch.',
    'Pacjent skarży się na ból głowy.',
    'Pacjent ma gorączkę i dreszcze.',
    'Pacjent odczuwa osłabienie.',
    'Pacjent ma duszności i kaszel.',
    'Pacjent zgłasza katar i ból gardła.',
    'Pacjent ma zawroty głowy.',
    'Pacjent skarży się na wymioty.',
    'Pacjent ma biegunkę.',
    'Pacjent zgłasza ból mięśni i stawów.',
    'Pacjent odczuwa pieczenie oczu.',
    'Pacjent ma problemy z trawieniem.',
    'Pacjent zgłasza opuchliznę nóg.',
    'Pacjent odczuwa swędzenie skóry.',
    'Pacjent ma wysokie ciśnienie krwi.',
    'Pacjent ma problemy ze wzrokiem.',
    'Pacjent odczuwa zmęczenie i senność.',
    'Pacjent ma ból zęba.',
    'Pacjent skarży się na bóle kręgosłupa.',
    'Pacjent zgłasza łzawienie oczu.',
    'Pacjent odczuwa drżenie rąk.',
    'Pacjent ma objawy przeziębienia.',
    'Pacjent skarży się na ból zatok.',
    'Pacjent odczuwa bóle brzucha po jedzeniu.',
    'Pacjent zgłasza trudności w oddychaniu.',
    'Pacjent ma swędzenie i zaczerwienienie skóry.',
    'Pacjent skarży się na szumy uszne.',
    'Pacjent odczuwa silne bóle w klatce piersiowej.',
    'Pacjent ma problem z pamięcią.',
    'Pacjent zgłasza uczucie niepokoju.',
    'Pacjent ma problemy ze snem.',
    'Pacjent skarży się na ból w stawie kolanowym.',
    'Pacjent ma zgagę.',
    'Pacjent odczuwa dreszcze bez gorączki.',
    'Pacjent ma wrażliwość na światło.',
    'Pacjent skarży się na bóle w odcinku szyjnym kręgosłupa.',
    'Pacjent zgłasza bóle głowy przy wysiłku.',
    'Pacjent ma problemy z równowagą.',
    'Pacjent odczuwa sztywność mięśni.',
    'Pacjent ma objawy alergii pokarmowej.',
    'Pacjent zgłasza trudności w przełykaniu.',
    'Pacjent odczuwa ból w klatce piersiowej przy głębokim wdechu.',
    'Pacjent ma mrowienie w kończynach.',
    'Pacjent zgłasza częste bóle głowy związane z migreną.',
    'Pacjent skarży się na kłopoty z koncentracją.',
    'Pacjent ma napady paniki.'
]

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

def biased_random_int(low, high, bias=0.9):
    if random.random() < bias:
        # generate low number
        return fake.random_int(min=low, max=(low + high) // 8)
    else:
        # generate high number
        return fake.random_int(min=(low + high) // 8 + 1, max=high)        

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
        dolegliwosci=fake.sentence(ext_word_list=my_sentence_list)
        assert len(dolegliwosci) <= 1000
        kwota=round(random.uniform(40, 600), 2)
        godzina = generate_random_time_within_range()
        czy_odbyta = random.choices(["TAK", "NIE"], weights=[0.7, 0.3], k=1)[0]
        ID_recepcjonistki= random.choice(recepcjonistki)
        writer.writerow([ID_wizyty, data_umówienia,data_rozpoczęcia,dolegliwosci, kwota, godzina,czy_odbyta,ID_recepcjonistki])


# Oświadczamy, że treści wygenerowane przy pomocy z GenAI poddałyśmy krytycznej analizie i zweryfikowałyśmy.
# Korzystałyśmy za zgodą prowadzącego z następujących narzędzi o potencjalnie wysokim stopniu ingerencji:
# ChatGPT - wygenerowanie danych dla: my_sentence_list, specjalization_provider