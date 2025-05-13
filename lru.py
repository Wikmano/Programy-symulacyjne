import random

# Funkcja implementująca algorytm zastępowania stron LRU (Least Recently Used)
def lru_page_replacement(pages, frame_size):
    memory_frames = []  # Lista reprezentująca ramki pamięci
    last_used = []  # Lista przechowująca indeksy użycia stron
    page_faults = 0  # Licznik błędów stron

    # Przejście przez każdą stronę w liście
    for i, page in enumerate(pages):
        if page in memory_frames:  # Sprawdzenie, czy strona jest już w liście ramek
            last_used_index = memory_frames.index(page)  # Pobranie indeksu strony
            last_used[last_used_index] = i  # Aktualizacja indeksu ostatniego użycia strony
            print(f"Strona {page} została odświeżona, ramki: {memory_frames}")
        else:
            if len(memory_frames) < frame_size:  # Sprawdzenie, czy są wolne ramki
                memory_frames.append(page)  # Dodanie nowej strony do listy ramek
                last_used.append(i)  # Dodanie indeksu użycia nowej strony
                print(f"Strona {page} została dodana, ramki: {memory_frames}")
            else:
                oldest_page_index = last_used.index(min(last_used))  # Znalezienie strony najdawniej używanej
                removed_page = memory_frames.pop(oldest_page_index)  # Usunięcie najdawniej używanej strony z listy ramek
                last_used.pop(oldest_page_index)  # Usunięcie indeksu najdawniej używanej strony
                memory_frames.append(page)  # Dodanie nowej strony do ramek
                last_used.append(i)  # Dodanie indeksu użycia nowej strony
                print(f"Usunięto stronę {removed_page}, a dodano stronę {page}, ramki: {memory_frames}")
            page_faults += 1  # Zwiększenie licznika błędów stron
            
    return page_faults  # Zwrócenie liczby błędów stron

frame_size = 3  # Rozmiar ramek pamięci

num_pages = 10  # Liczba stron do wygenerowania

# Wygenerowanie losowego ciągu stron
pages = [random.randint(0, 9) for i in range(num_pages)]

print("Wygenerowane strony:", pages)

# Wywołanie funkcji zastępowania stron LRU i zapisanie liczby błędów stron
faults = lru_page_replacement(pages, frame_size)

# Wyświetlenie liczby błędów stron
print("Liczba błędów stron: ", faults)