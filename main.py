def show_kursi(kursi):
    for i in kursi:
        print(f'''no kursi: {i['no_kursi']}
kode kursi: {i['kode_kursi']}
status kursi: {i['status_kursi']}
''')
        
def input_order_kursi(ket, quest):
    order_kursi = []
    while True:
        kode_kursi = input(ket)
        order_kursi.append(kode_kursi)
        question = input(quest)
        if question == 'n':
            break
    return order_kursi

def proccess_order(order_kursi, kursi):
    for i in kursi:
        if i['kode_kursi'] in order_kursi:
            i['status_kursi'] = 'terisi'
    return kursi

def update_order(order_kursi, order_kursi_update ,kursi):
    for i in kursi:
        if i['kode_kursi'] in order_kursi:
            i['status_kursi'] = 'kosong'
        if i['kode_kursi'] in order_kursi_update:
            i['status_kursi'] = 'terisi'
    return kursi

def print_struk(kursi, order_kursi_update):
    print('struk kursi: ')
    for i in kursi:
        if i['kode_kursi'] in order_kursi_update and i['status_kursi'] == 'terisi':
            print(f'''no kursi: {i['no_kursi']}
kode kursi: {i['kode_kursi']}
status kursi: {i['status_kursi']}
''')

if __name__ == '__main__':
    kursi = [
        {
            'no_kursi': 1, 
            'kode_kursi': 'A1', 
            'status_kursi': 'kosong'
        },
        {
            'no_kursi': 2, 
            'kode_kursi': 'A2', 
            'status_kursi': 'kosong'
        },
        {
            'no_kursi': 3, 
            'kode_kursi': 'A3', 
            'status_kursi': 'kosong'
        },
    ]
    order_kursi = []
    order_kursi_update = []
    # program booking tiket bioskop
    # informasi kursi => no kursi, kode kursi, status kursi
    # pesan kursi
    # ubah pilihan kursi
    # cetak kode kursi
    while True:
        print('''Menu E-Bioskop
1. Tampilkan Kursi
2. Pesan Kursi
3. Ubah Pesanan Kursi
4. Cetak Struk Pesanan
5. Keluar''')
        x = int(input('Pilih menu: '))
        if x == 1:
            show_kursi(kursi)
        if x == 2:
            order_kursi = input_order_kursi('Masukan kode kursi: ', 'Apakah anda ingin memesan kursi lagi? (y/n) ')
            # proses pesan kursi
            kursi = proccess_order(order_kursi, kursi)
        if x == 3:
            # semisal ingin mengubah kursi
            order_kursi_update = input_order_kursi('Masukan kode kursi yang ingin diubah: ', 'Apakah anda ingin mengubah kursi lagi? (y/n)')
            # update pesan kursi
            kursi = update_order(order_kursi, order_kursi_update, kursi)
        if x == 4:
            # cetak struk pesanan
            if len(order_kursi_update) != 0:
                print_struk(kursi, order_kursi_update)
            print_struk(kursi, order_kursi)
        if x == 5:
            print('Terima kasih telah menggunakan layanan kami')
            break
    # sampai jumpa di tutorial berikutnya