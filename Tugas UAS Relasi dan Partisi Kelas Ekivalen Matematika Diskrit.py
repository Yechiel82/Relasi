"""
Anggota Kelompok:
- Yechiel Ardner Arianto (NIM: 212000576)
- Moses Anthony Kwik     (NIM: 212100291)
- Mastri Tasya Napitulu  (NIM: 212100370)
"""

def fungsi_refleksif(list1, list2, counter, node, result, taken):

    for i in range(counter):
        # Untuk menghitung jumlah kesamaan contoh jika 1 ketemu 1 maka result +1
        if list1[i] == list2[i]:
            result += 1


    # Jika hasil result dan node sama maka terprint fungsi reflektif
    if result == node:
        print("Relasi ini bersifat refleksif.")
        return True
    else:
        print("Relasi ini tidak bersifat refleksif.")
        for i in range(counter):
            if list1[i] == list2[i]:
                if list1[i] in taken:
                    taken.remove(list1[i])
                    print(f"Contoh penyangkal: {taken}, karena tidak merefleksikan dirinya sendiri.")
        return False


def fungsi_simetris(list1, list2):
    limiter = 0
    check = []
    # Untuk mengambil a sebagai list 1 dan b sebagai list 2
    for i in range(len(list1)):
        _list1 = list1[i]
        _list2 = list2[i]
        if _list1 != _list2:
            check.append([_list1, _list2])

        # Untuk mengambil c dan d
        for j in range(len(list1)):
            # Untuk memastikan tidak mengambil list dengan angka yang sama berulang kali
            if list1[i] != list1[j] and list2[i] != list2[j]:
                # print(_list1, _list2)
                c = list1[j]
                d = list2[j]

                # Untuk memastikan jika list simetris
                if _list1 == d and _list2 == c:
                    check.remove([_list1, _list2])
                    # print(f'ini len check{len(check)}')
                    if len(check) == 0:
                        print("Relasi ini bersifat simetris.")
                        limiter += 1
                        return True
                    if limiter < 1:
                        print("Relasi ini tidak bersifat simetris.")
                        print(f"Contoh penyangkal tidak simetris: {check}")
                        return False



# Untuk mencatat bilangan dan hanya tercatat hanya 1 kali
def noter(taken, _taken):
    if _taken[0] not in taken:
        taken.append(_taken[0])
    elif _taken[1] not in taken:
        taken.append(_taken[1])
    return taken


if __name__ == '__main__':

    node_relasi = str(input(""))
    _node_relasi = node_relasi.replace(' ', '')
    node = int(_node_relasi[0])
    relasi = int(_node_relasi[1])
    limiter =0
    counter = 0
    result = 0
    list1 = []
    list2 = []
    base = []
    taken = []
    dif_counter = 0
    # Untuk memastikan jika counter di bawah relasi
    while True and counter < relasi:
        data = (input(""))
        _data = data.replace(' ', '')
        _taken = str(_data)
        # Relasi harus 2 pada saat misalnya 1 2 atau 2 3
        if len(_data) == 2:
            for i in range(2):
                noter(taken, _taken)
            counter += 1
            data = _data
            len_count = len(list1)
        else:
            print("invalid data")
        list1.append(data[0])
        list2.append(data[1])
        base.append([_taken[0], _taken[1]])
    #jika if_3_then_equivalent sama dengan 3 berarti relasi tersebut ekuivalent
    if_3_then_equivalent =0
    if len(taken) == node:
        if fungsi_simetris(list1, list2) == True :
            if_3_then_equivalent += 1
        if fungsi_refleksif(list1, list2, counter, node, result, taken) == True:
            if_3_then_equivalent += 1
        

    else:
        #untuk mengecek jika relasi hanya dan hanya 2 relasi contoh 1 2 bukan 1 3 2
        print("Invalid data")
