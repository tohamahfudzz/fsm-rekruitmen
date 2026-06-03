from enum import Enum,auto
#from soal import soal
class State(Enum):
    
    Start=auto()
    Input_profesi_dipilih=auto()#pilih profesi juga disini
    Input_data_diri_nama=auto()
    Input_data_diri_alamat=auto()
    Input_data_diri_gender=auto()
    Input_data_diri_alasan=auto()
    Input_data_pendidikan_terakhir=auto()#input pengalaman juga disini
    Input_data_pendidikan_mean_nilai=auto()
    Input_data_pendidikan_ijazah=auto()#no ijazah
    Input_data_pendidikan_pengalaman=auto()
    
    Test=auto()
    Hasil=auto()
    End=auto()

class Rekrutmen:
    def __init__(self):
        self.state=State.Start #ada di state start
        #self.state=State.Test#untuk uji tiap state
        self.respon=""
        self.nama=""
        self.alamat=""
        self.gender=""
        self.alasan=""
        self.profesi=""#profesi yang dipilih
        self.pendidikan=""#pendidikan terakhir
        self.nilai_mean=""
        self.ijazah=""#no ijazah
        self.pengalaman=""
        self.jawaban=[]
        self.score=""

    def proses(self,text):
        if(self.state==State.Start):
            self.respon=("selamat datang/n"
            "pilih profesi:/n"
            "1.frontend developer/n"
            "2.backend developer")
            self.state=State.Input_profesi_dipilih#ada di state memilih profesi
        elif(self.state==State.Input_profesi_dipilih):
            self.profesi=text
            self.respon="masukkan nama anda:"
            self.state=State.Input_data_diri_nama
        elif(self.state==State.Input_data_diri_nama):
            self.nama=text
            self.respon="masukkan alamat anda:"
            self.state=State.Input_data_diri_alamat
        elif(self.state==State.Input_data_diri_alamat):
            self.alamat=text
            self.respon="gender anda:"
            self.state=State.Input_data_diri_gender
        elif(self.state==State.Input_data_diri_gender):
            self.gender=text
            self.respon="alasan anda memilih profesi ini:"
            self.state=State.Input_data_diri_alasan
        elif(self.state==State.Input_data_diri_alasan):
            self.alasan=text
            self.respon="pendidikan terakhir:"
            self.state=State.Input_data_pendidikan_terakhir
        elif(self.state==State.Input_data_pendidikan_terakhir):
            self.pendidikan=text
            self.respon="nilai rata-rata:"
            self.state=State.Input_data_pendidikan_mean_nilai
        elif(self.state==State.Input_data_pendidikan_mean_nilai):
            self.nilai_mean=text
            self.respon="Masukkan nomor ijazah:"
            self.state=State.Input_data_pendidikan_ijazah
        elif(self.state==State.Input_data_pendidikan_ijazah):
            self.ijazah=text
            self.respon="Masukkan pengalaman anda jika ada:"
            self.state=State.Input_data_pendidikan_pengalaman
        elif(self.state==State.Input_data_pendidikan_pengalaman):
            self.pengalaman=text
            self.respon=""
            self.state=State.Test
        elif(self.state==State.Test):#test
            pass
            # for i in range(0,len(soal[self.profesi])):
            #     print(pertanyaan=soal[self.profesi][i]["pertanyaan"])#sementara memakai print
            #     for j in range(0,len(soal[self.profesi][i]["opsi"])):
            #         print(soal[self.profesi][i]["opsi"][j])
            #     self.jawaban.append(input("jawaban"))
           # print(self.jawaban)

            #apakah soal harus ditaruh direspon atau tempat sendiri???????
            #masih belum terpikirkan

            




        
        
