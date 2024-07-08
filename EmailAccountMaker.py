from seleniumbase import SB
import random

przejdz_do_serwisu = 'body > div.rodo-popup > div.rodo-popup-buttons > button.rodo-popup-agree.rodo-popup-main-agree'
imie = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[2]/input'
nazwisko = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[3]/input'
dzien = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[4]/div[1]/input'
miesiac = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[4]/div[2]/'
rok = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[4]/div[3]/input'
plec = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[5]'
nazwa_konta = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[6]/div[1]/label'
zajeta_dla_tej_domeny = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[6]/div[1]/ul/li'
nazwa_konta = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[6]/div[1]/input'
domena_klik = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[6]/div[2]/div/div[1]'
domena_lista = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[6]/div[2]/div/ul'
haslo1 = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[7]/div/input'
haslo2 = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div[8]/div/input'
checkbox = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/label/div'
zaloz_btn = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button'
przejdz_btn = '/html/body/div[4]/div/div/div/div/div[2]/button[2]'
kolko_email = '/html/body/div[2]/section[4]/div/div[1]/div[1]/div[2]/div/div'
adres_email_xpath = '/html/body/div[2]/section[4]/div/div[1]/div[2]/div/div[4]'

def check_and_click_elements(sb, zajeta_dla_tej_domeny, domena_klik, domena_lista):
     if sb.is_element_visible(zajeta_dla_tej_domeny):
            sb.click(domena_klik)
            sb.sleep(5)
            sb.click(domena_klik)
                    
            element_paths = [
                        f"{domena_lista}/li[2]",
                        f"{domena_lista}/li[3]",
                        f"{domena_lista}/li[4]",
                        f"{domena_lista}/li[5]",
                        f"{domena_lista}/li[6]",
                        f"{domena_lista}/li[7]",
                        f"{domena_lista}/li[8]",
                        f"{domena_lista}/li[9]",
                        f"{domena_lista}/li[10]",
                        f"{domena_lista}/li[11]"
                    ]

            for path in element_paths:
                try:
                    element = sb.find_element(path)
                    class_attribute = element.get_attribute('class')
                    if 'unavailable' in class_attribute.split():
                                print(f"Element of path a {path} has class 'unavailable'.")
                    else:
                        print(f"Element of path a {path} hasn't class 'unavailable'.")
                        sb.click(path)
                        break
                except:
                        print(f"Cannot  find element of path a {path}")

with open('names.txt', 'r', encoding='utf-8') as file:
    imiona = [line.strip() for line in file]

with open('surnames.txt', 'r', encoding='utf-8') as file:
    nazwiska = [line.strip() for line in file]

num_accounts = int(input("Enter the number of accounts to be created:  "))

for _ in range(num_accounts):

    indeks_miesiaca = random.randint(1, 12)
    dzien_i = random.randint(1, 28)
    imie_i = random.choice(imiona)
    nazwisko_i = random.choice(nazwiska)
    rocznik = str(random.randint(1970, 2005))
    nazwa_konta_i = f"{imie_i}.{nazwisko_i}"
    ####################################################
    haslo_i = 'PASSWORD'
    ####################################################
    
    with SB(uc=True, incognito=True) as sb:
        sb.driver.uc_open_with_reconnect("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe")
        sb.maximize_window()
        sb.click(przejdz_do_serwisu)
        sb.sleep(2)
        sb.click(imie)
        sb.type(imie, imie_i)
        sb.sleep(2)
        sb.click(nazwisko)
        sb.type(nazwisko, nazwisko_i)
        sb.sleep(2)
        sb.click(dzien)
        sb.type(dzien, dzien_i)
        sb.sleep(1)
        sb.click(f"{miesiac}/label")
        sb.click(f"{miesiac}ul/li[{indeks_miesiaca}]")
        sb.click(rok)
        sb.type(rok, rocznik)
        sb.sleep(1)
        sb.click(f"{plec}/div[1]")
        sb.click(f"{plec}/ul/li[1]")
        sb.sleep(1)
        sb.click(nazwa_konta)
        sb.input(nazwa_konta, nazwa_konta_i)
        sb.sleep(1)
        check_and_click_elements(sb, zajeta_dla_tej_domeny, domena_klik, domena_lista)
        sb.sleep(10)
        if sb.is_element_visible(zajeta_dla_tej_domeny):
            sb.click(nazwa_konta)
            sb.input(nazwa_konta, nazwa_konta_i + str(rocznik)[-2:])
            sb.sleep(10)
        sb.sleep(5)
        check_and_click_elements(sb, zajeta_dla_tej_domeny, domena_klik, domena_lista)
        sb.click(haslo1)
        sb.type(haslo1, haslo_i)
        sb.sleep(1)
        sb.click(haslo2)
        sb.sleep(1)
        sb.type(haslo2, haslo_i)
        sb.sleep(5)
        sb.click(checkbox)
        sb.click(zaloz_btn)
        sb.sleep(6)
        sb.click(przejdz_btn)
        sb.click(przejdz_btn)
        sb.sleep(4)
        sb.click(kolko_email)

        adres_email = sb.wait_for_element_visible(adres_email_xpath).text

        with open("emails.txt", "a") as file:
            file.write(adres_email + "\n")
