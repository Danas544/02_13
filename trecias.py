
# 1. Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.

dalyba = [x for x in range(1,1001) if x % 6 == 0] 
print(f"dalyba: {dalyba}")

# 1. Raskite visus skaičius iš 1-1000, kuriuose yra 9.
find = [x for x in range(1,1001) if "9" in str(x)]
print(f"find: {find}")

# 1. Sukurkite stringą iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę "e".
string = ["Vienarūšiai šalutiniai dėmenys, sujungti nekartojamais sudedamaisiais ar skiriamaisiais jungtukais ir, ar, arba, neatskiriami. Atsidėjęs aiškino broliui, kaip pagal medžių šakas nustatyti kryptį ir kaip pagal jų rieves metus skaičiuoti. Kai prisistačiau, jie šiltai mane priėmė ir apgailestavo, kad Broniaus nėra ir kad turėtų kaip tik tą dieną parvažiuoti. Kodėl nesakei, jog tai be galo kenksmingas darbas ar kad tu norėtum jį mesti. SUDĖTINIŲ BEJUNGTUKIŲ SAKINIŲ SKYRYBOS TAISYKLĖS Bejungtukių sakinių dėmenys, kuriais reiškiamas išvardijimas, gretinimas ar priešprieša, paprastai atskiriami kableliu ar kabliataškiu: Nuvytusios rožės nepražydės, neišdainuotos dainos taip ir liks neišdainuotos. Brolis greit šoko į vandenį, jo įdegęs kūnas išsitempė ir paniro gilyn. Reiškiant apibendrinimą, sąlygą, laiką, nuolaidą, neatitikimą sudėtiniame bejungtukiame sakinyje dažniau vartojamas brūkšnys: Sodininkas jis buvo ir mokykloje – geresnį palyginimą sunku rasti. Pasimaišytų jam žvėris ar priešas – bemat patiestų. Jis ne toks žmogus – niekas jam neįsakinės. Bejungtukių sakinių dėmenys, kuriais reiškiamas aiškinimas, priežastis ir pasekmė, atskiriami dvitaškiu ar brūkšniu: Už lango girdėjosi triukšmas: ūžė mašinos, šūkavo vaikai. Viskas čia buvo natūralu ir tikra: šviežias ožkos pienas kvepėjo ožka, dūmai – gryno medžio anglimi, oras – visais gyvosios gamtos aromatais... Sudėtinio bejungtukio sakinio dėmens atitikmeniu einantys teigimo, neigimo, sutikimo ir kitų panašių reikšmių žodžiai atskiriami kableliu: Taip, taisykles dar turėtų pakartoti."]

find_e = [x.count("e") for x in string ]
print(f"Radom e raidziu tiek -> {find_e}")



# 1. Naudodami tą patį stringą, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.
# Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.
string = str(string).split(" ")

find_more_fife_cha = [x.count(x) for x in string if len(x) > 5]
print(f"Kiek žodziu yra kuriuose daugiau negu 5 raidės: {sum(find_more_fife_cha)}")

