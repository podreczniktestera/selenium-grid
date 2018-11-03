# Przykład projektu Selenium - GRID [![Build Status](https://travis-ci.org/podreczniktestera/selenium-grid.svg?branch=master)](https://travis-ci.org/podreczniktestera/selenium-grid)

#### Ustawienie projektu

###### CMD | Terminal
  ```bash
    git clone

    cd selenium-grid

    virtualenv venv --python=python

    venv\Scripts\activate.bat
      # lub na Linuxie
    source venv/Scripts/activate

    pip install -r requirements.txt
```
###### PyCharm CE
* Należy zmienić interpreter Python'a tak aby wskazywał na wirtualne środowisko
* Oraz dodać konfigurację do uruchamiania testów:
  * Script path: ścieżka do aplikacji `pytest` z wirualnego środowiska
  * Parameters:  `-n *liczba_podłączonych_węzełów* tests/test_suite.py`


* Lub w CMD | Terminal
    ```bash
      pytest -n *liczba_podłączonych_węzełów* tests/test_suite.py
    ```

#### Selenium-GRID

  * ###### Połączenie HUB <-> NODE

    Start HUBa
    ```bash
        ./start_hub.sh selenium-server-standalone-3.14.0.jar
    ```

    Start Węzła
    ```bash
        ./start_node.sh selenium-server-standalone-3.14.0.jar IP_HUBa
    ```

  * ###### Docker

      Start GRIDa
      ```bash
        docker-compose up -d
      ```
      Zmiana liczby węzłów
      ```bash
        docker-compose scale chrome=*liczba_węzłów*
      ```
      Zatrzymanie GRIDa    
      ```bash
        docker-compose down
      ```
