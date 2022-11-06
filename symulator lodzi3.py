# symulator Łodzi - wyprawa po przedmiesciach łodzi podczas ktorej spotykasz mityczne stwory z ktorymi mozesz walczyc, wybierac co zrobisz rozmawiac 

from random import randint


# print('Wybierz plec: m - chlopak, k - dziewczyna')
# plec = str(input())
# while plec != 'k' or 'm':
#     if plec == 'k':
#         break
#     elif plec == 'm':
#         break
#     plec = str(input())
#     print('Wybierz plec: m - chlopak, k - dziewczyna', plec)


# print('wybierz nazwe swojego podroznika: ')
# imie = str(input())
# imie = randint(1,7)
# nazwy_m = ['Sebastian', 'Antoni', 'Jan','Jakub','Aleksander','Franciszek']
# nazwy_k = ['Hanna', 'Zofia','Julia','Maja','Zuzanna','Honorata']

# rand = randint(0,6)

# if plec == 'k':
#     los = nazwy_k[rand]
#     print('gratulacje twoje imie to: ',los,'(przeciez sama nie wybieralas swojego imienia - podziekuj rodzicom)')
# elif plec == 'm':
#     los2 = nazwy_m[rand]
#     print('Gratulacje twoje imie to: ',los2,'(przeciez sam nie wybierales swojego imienia - podziekuj rodzicom)')

print('Witaj na przedmiesciach Lodzi, na które zdarzyło ci się trafic przez przenikanie sie swiatow, zwane koniunkcja sfer.')
print('Twoim zadaniem w tej ciemnej i nieprzyjaznej krainie jest przezyc dopoki efekty koniunkcji sie nie ustatkuja','\n','Podroz przez rozne swiaty bardzo cie zmeczyla - ruszasz przed siebie zeby znalezc cos do jedzenia')
print('W twoja strone zmierza 𝐬𝐳𝐥𝐚𝐜𝐡𝐞𝐭𝐧𝐲 rycerz dosiadajacy dzika: czy chcesz go zatrzymac','\n','i poprosic o jedzenie i informacje?')
szlachcic = str(input('chcesz?'))

while szlachcic != 'nie' and 'tak':
    szlachcic = str(input('chcesz?'))
    if szlachcic == 'nie':
        print('Boisz sie czlowieka z dzikiem - wolisz go nie zatrzymywac')
        break
    elif szlachcic == 'tak' and 'jeszcze jak':
        print('na pewno?')
        szlachcic = str(input('chcesz?'))
        if szlachcic == 'tak' and 'jak najbardziej':
            print('probujesz zatrzymac szlachcica galopujacego w twoja strone')
            break
        elif szlachcic == 'nie':
            print('latwo zmieniasz zdanie...')
            break
print('uwu')
