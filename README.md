# Symulacje Algorytmów Systemów Operacyjnych

## Opis

Projekt zawiera implementacje dwóch rodzajów algorytmów systemów operacyjnych: **algorytmów przydziału procesora** oraz **algorytmów stronicowania**. W ramach projektu zaimplementowane zostały:

1. **Algorytmy przydziału procesora**:
   - **FCFS (First Come First Served)** – Algorytm przydzielania procesora w kolejności ich nadejścia.
   - **SJF (Shortest Job First)** – Algorytm przydzielania procesora dla procesu o najkrótszym czasie wykonania (niewywłaszczający).

2. **Algorytmy stronicowania**:
   - **FIFO (First-in, First-Out)** – Algorytm zarządzania pamięcią, który usuwa stronę, która najdłużej znajduje się w pamięci.
   - **LRU (Least Recently Used)** – Algorytm, który usuwa stronę, która była najdawniej używana.

Projekt obejmuje zarówno implementację tych algorytmów, jak i przeprowadzenie eksperymentów porównujących ich wydajność. Dodatkowo, pełny przebieg projektu, wraz z wynikami i wykresami szybkości oraz skuteczności działania algorytmów, znajduje się w pliku PDF dołączonym do repozytorium.

## Część I: Algorytmy Przydziału Procesora

### 1. FCFS (First Come First Served)
Algorytm **FCFS** obsługuje procesy w kolejności ich przybycia. Każdy proces otrzymuje procesor na czas jego wykonania, bez preemptive (bez wywłaszczania). Jest to prosty, ale może prowadzić do długich czasów oczekiwania dla krótkich procesów, gdy procesy długie przychodzą wcześniej.

#### Implementacja
- Użytkownik wprowadza dane o procesach: czas trwania oraz liczba procesów.
- Obliczane są czasy oczekiwania oraz realizacji dla każdego procesu.
- Obliczanie średnich czasów oczekiwania i realizacji.

### 2. SJF (Shortest Job First)
Algorytm **SJF** obsługuje procesy zaczynając od najkrótszego czasu wykonania (burst time). Jest to algorytm niewywłaszczający, co oznacza, że procesy nie są przerywane po rozpoczęciu.

#### Implementacja
- Użytkownik wprowadza dane o procesach.
- Procesy są sortowane według czasu trwania, a następnie przypisywane procesorowi.
- Obliczane są czasy oczekiwania oraz realizacji.
- Podobnie jak w przypadku FCFS, obliczane są średnie czasy oczekiwania i realizacji.

#### Porównanie
- W eksperymencie porównano czasy oczekiwania algorytmu **FCFS** i **SJF**. Z wykonanego testu wynika, że **SJF** generalnie przewyższa **FCFS** w kwestii czasów oczekiwania.

## Część II: Algorytmy Stronicowania

### 1. FIFO (First-In, First-Out)
Algorytm **FIFO** usuwa stronę, która znajduje się w pamięci najdłużej. Nowe strony są dodawane na końcu kolejki, a strona na początku jest usuwana.

#### Implementacja
- Algorytm realizowany w jednej funkcji.
- Pokazuje liczbę błędów stron (page faults) oraz sposób, w jaki strony są dodawane do listy.

### 2. LRU (Least Recently Used)
Algorytm **LRU** usuwa stronę, która była używana najdawniej, zakładając, że strony używane niedawno mają większe prawdopodobieństwo ponownego użycia.

#### Implementacja
- Wymaga dodatkowej listy, aby śledzić, które strony były używane najdawniej.
- Pokazuje liczbę błędów stron oraz sposób działania algorytmu.

#### Porównanie
- W eksperymencie porównano algorytmy **FIFO** i **LRU** w różnych scenariuszach, zarówno losowych, jak i manualnie określonych wzorcach dostępu do pamięci.
- **LRU** zazwyczaj skutkuje mniejszą liczbą błędów stron, ale wyniki zależą od konkretnego wzorca dostępu.

## Dokumentacja i Analiza

Pełny przebieg projektu, w tym implementacja algorytmów, analiza wyników oraz wykresy porównujące szybkość i skuteczność algorytmów, znajduje się w załączonym pliku PDF. 

Plik PDF zawiera szczegółowe opisy, wyniki eksperymentów oraz wykresy przedstawiające wydajność różnych algorytmów. Jest to niezbędne w celu prawidłowego stwierdzenia skuteczności danych algorytmów.
