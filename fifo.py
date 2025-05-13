import random

# Funkcja implementująca algorytm zastępowania stron FIFO
def fifo_page_replacement(pages, frame_size):
    memory_frames = []
    page_faults = 0  # Licznik błędów stron

    # Przechodzenie przez każdą stronę w liście
    for page in pages:
        if page not in memory_frames:  # Sprawdzenie, czy strona nie jest już w liście ramek pamięci
            if len(memory_frames) == frame_size:  # Sprawdzenie, czy ramki są pełne
                memory_frames.pop(0)  # Usunięcie najstarszej strony (FIFO)
            memory_frames.append(page)  # Dodanie nowej strony do listy ramek pamięci
            page_faults += 1  # Zwiększenie licznika błędów stron
            print(f"Strona {page} została dodana, ramki: {memory_frames}")
        else:
            print(f"Strona {page} jest juz w ramce: {memory_frames}")

    return page_faults  # Zwrócenie liczby błędów stron

frame_size = 3  # Rozmiar ramki pamięci

num_pages = 10  # Liczba stron do wygenerowania

# Wygenerowanie losowego ciągu stron
pages = [random.randint(0, 9) for i in range(num_pages)]

print("Wygenerowane strony:", pages)

# Wywołanie funkcji zastępowania stron FIFO i zapisanie liczby błędów stron
faults = fifo_page_replacement(pages, frame_size)

print("Liczba błędów stron: ", faults)  # Wyświetlenie liczby błędów stron