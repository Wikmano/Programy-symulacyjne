# Funkcja do wprowadzania danych o procesach
def insert_procces_data():
    procesy = [] 
    liczba_procesow = int(input("Podaj liczbe procesow: "))  # Pobranie liczby procesów od użytkownika

    # Pętla do wprowadzania czasu trwania dla każdego procesu
    for i in range(1, liczba_procesow + 1):
        burst_time = int(input(f"Podaj czas trwania procesu {i}: "))
        procesy.append({'numer_procesu': i, 'czas_trwania': burst_time })  # Dodanie procesu do listy

    return procesy

procesy = insert_procces_data() 

# Funkcja pomocnicza do sortowania procesów po czasie trwania
def sort_key(proces):
    return proces['czas_trwania']

# Funkcja do sortowania procesów według czasu trwania
def sort_proccesses(procesy):
    procesy.sort(key=sort_key) 
    return procesy

procesy_posortowane = sort_proccesses(procesy)  

# Funkcja do obliczania czasu oczekiwania dla posortowanych procesów
def waiting_time(procesy_posortowane):
    czasy_oczekiwania = [0] * len(procesy_posortowane)  # Inicjalizacja listy czasów oczekiwania
    for i in range(1, len(procesy_posortowane)):
        czasy_oczekiwania[i] = czasy_oczekiwania[i - 1] + procesy_posortowane[i - 1]['czas_trwania']  # Obliczanie czasu oczekiwania
    return czasy_oczekiwania

czasy_oczekiwania = waiting_time(procesy_posortowane)  

# Funkcja do obliczania czasu realizacji dla posortowanych procesów
def exec_time(procesy_posortowane, czasy_oczekiwania):
    czasy_wykonania = []  
    for i in range(len(procesy_posortowane)):
        czas_realizacji = czasy_oczekiwania[i] + procesy_posortowane[i]['czas_trwania']  # Obliczanie czasu realizacji
        czasy_wykonania.append(czas_realizacji)  # Dodanie czasu realizacji do listy
    return czasy_wykonania

czasy_wykonania = exec_time(procesy_posortowane, czasy_oczekiwania)  

# Funkcja do obliczania średniego czasu oczekiwania
def average_waiting_time(czasy_oczekiwania):
    sredni_czas_oczekiwania = sum(czasy_oczekiwania) / len(czasy_oczekiwania)  # Obliczanie średniego czasu oczekiwania
    return sredni_czas_oczekiwania

sredni_czas_oczekiwania = average_waiting_time(czasy_oczekiwania)  

# Funkcja do obliczania średniego czasu realizacji
def average_realization_time(czasy_wykonania):
    sredni_czas_wykonania = sum(czasy_wykonania) / len(czasy_wykonania)  # Obliczanie średniego czasu realizacji
    return sredni_czas_wykonania

sredni_czas_realizacji = average_realization_time(czasy_wykonania)  

# Wyświetlanie wyników dla każdego procesu
for i, proces in enumerate(procesy_posortowane):
    print(f"Proces {proces['numer_procesu']} ma czas oczekiwania : {czasy_oczekiwania[i]} i czas realizacji: {czasy_wykonania[i]}")

# Wyświetlanie średniego czasu oczekiwania
print("Średni czas oczekiwania:", sredni_czas_oczekiwania)

# Wyświetlanie średniego czasu realizacji
print("Średni czas wykonania:", sredni_czas_realizacji)