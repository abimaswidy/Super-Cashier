class Produk():
    def __init__(self):
        self.nama_item = input('masukan nama item:')
        self.jumlah_item = int(input('masukan jumlah item:'))
        self.harga_item = int(input('masukan harga item:'))
        self.total_harga = self.jumlah_item * self.harga_item
        
    def total_item():
        print('Total Produk : ', Produk.total_item)

    def detail_produk(self):
        print("Nama : ", self.nama_item)
        print("jumlah: ", self.jumlah_item)
        print("Harga: ", self.harga_item)
        print("total : ",self.total_harga)
        print()
    def displayItem(self):  
        print("Nama item:", self.nama_item, "Jumlah item:", self.jumlah_item)
# membuat simulasi pembelian pertama
produk1 = Produk()
produk1.detail_produk()

# membuat simulasi pembelian pertama ketika customer salah memasukan nama item atau jumlah item


