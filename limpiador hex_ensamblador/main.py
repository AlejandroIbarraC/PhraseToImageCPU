def ASCIItoHEXline(a_string):
    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(ASCII_values)
    HEX_values = []
    for i in ASCII_values:
        HEX_values.append(hex(i))

    while (len(HEX_values)<64):
        HEX_values.append('0x20')

    a="".join(HEX_values).split("0x")
    for i in range(len(a)):
        if len(a[i])==1:
            a[i]="0"+a[i]

    lista_a_txt(a[1:],"ROM")


def lista_a_txt(lista,nombre):
    file = open(nombre+".txt", "w")
    file.write("\n".join(lista))
    file.close()


ASCIItoHEXline("BECAUSE I COULD NOT STOP FOR DEATH, HE KINDLY STOPPED FOR ME. THE CARRIAGE HELD BUT JUST OURSELVES. AND IMMORTALITY. WE SLOWLY DROVE, HE KNEW NO HASTE, AND I HAD PUT AWAY MY LABOR, AND MY LEISURE TOO, FOR HIS CIVILITY. WE PASSED THE SCHOOL, WHERE CHILDREN STROVE AT RECESS, IN THE RING. WE PASSED THE FIELDS OF GAZING GRAIN, WE PASSED THE SETTING SUN. OR RATHER, HE PASSED US. THE DEWS GREW QUIVERING AND CHILL, FOR ONLY GOSSAMER MY GOWN, MY TIPPET ONLY TULLE. WE PAUSED BEFORE A HOUSE THAT SEEMED. A SWELLING OF THE GROUND. THE ROOF WAS SCARCELY VISIBLE, THE CORNICE BUT A MOUND. SINCE THEN TIS CENTURIES, AND YET EACH FEELS SHORTER THAN THE DAY. I FIRST SURMISED THE HORSES HEADS. WERE TOWARD ETERNITY. EMILY DICKINSON")


