# Funkcja do wprowadzania danych o procesach
def insert_processes():
    procesy = [] 
    liczba_procesow = int(input("Podaj liczbe procesow: "))  # Pobranie liczby procesów od użytkownika

    # Pętla do wprowadzania czasu trwania dla każdego procesu
    for i in range(1, liczba_procesow + 1):
        burst_time = int(input(f"Podaj czas trwania procesu {i}: "))
        procesy.append({'numer_procesu': i, 'czas_trwania': burst_time})  # Dodanie procesu do listy

    return procesy

procesy = insert_processes()  

# Funkcja do obliczania czasu oczekiwania dla procesów
def waiting_time(procesy):
    czas_oczekiwania = [0] * len(procesy)  # Inicjalizacja listy czasów oczekiwania
    for i in range(1, len(procesy)):
        czas_oczekiwania[i] = czas_oczekiwania[i - 1] + procesy[i - 1]['czas_trwania']  # Obliczanie czasu oczekiwania
    return czas_oczekiwania

czasy_oczekiwania = waiting_time(procesy)  

# Funkcja do obliczania czasu realizacji dla procesów
def realization_time(procesy, czasy_oczekiwania):
    czasy_realizacji = []  
    for i, proces in enumerate(procesy):
        czas_realizacji = czasy_oczekiwania[i] + proces['czas_trwania']  # Obliczanie czasu realizacji
        czasy_realizacji.append(czas_realizacji)  # Dodanie czasu realizacji do listy
    return czasy_realizacji

czasy_realizacji = realization_time(procesy, czasy_oczekiwania)  

# Funkcja do obliczania średniego czasu oczekiwania
def average_waiting_time(czasy_oczekiwania):
    suma_czasow = sum(czasy_oczekiwania)  
    liczba_procesow = len(czasy_oczekiwania)  
    sredni_czas_czekania = suma_czasow / liczba_procesow  # Obliczanie średniego czasu oczekiwania
    return sredni_czas_czekania

# Funkcja do obliczania średniego czasu realizacji
def average_realization_time(czasy_realizacji):
    suma_czasow = sum(czasy_realizacji)  
    liczba_procesow = len(czasy_realizacji)  
    sredni_czas_realizacji = suma_czasow / liczba_procesow  # Obliczanie średniego czasu realizacji
    return sredni_czas_realizacji

# Wyświetlanie wyników dla każdego procesu
for i, proces in enumerate(procesy):
    print(f"Proces {proces['numer_procesu']} ma czas oczekiwania : {czasy_oczekiwania[i]} i czas realizacji: {czasy_realizacji[i]}")

# Obliczanie i wyświetlanie średniego czasu oczekiwania
średni_czas_oczekiwania = average_waiting_time(czasy_oczekiwania)
print(f"Średni czas oczekiwania jest równy: {średni_czas_oczekiwania} sekund/y")

# Obliczanie i wyświetlanie średniego czasu realizacji
średni_czas_realizacji = average_realization_time(czasy_realizacji)
print(f"Średni czas realizacji jest równy: {średni_czas_realizacji} sekund/y")