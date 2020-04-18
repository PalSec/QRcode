import os
import keyboard
from PIL import Image
import zpl
import zpl2
import qrcode
import zpllibrary
import simple_zpl2
import socket
import RPi.GPIO as GPIO



mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.115"
port = 9100

while True:
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   test_input = GPIO.input(15)
   if keyboard.is_pressed('q'):
     print("Koniec programu")
     break

   elif test_input == 1 :

        print(test_input)


        product = 'A  Q7LP2020'


        file_product = open("product.txt", "r")
        file_product_number = open("product_number.txt", "r")
        product_f = file_product.readline()
        product_number = file_product_number.readline()
        file_product_number.close()
        file_product.close()

        number = int(product_number) + 1
        label_product = product + str(number)

        file_product_number = open("product_number.txt","w")
        file_product_number.write(str(number))
        file_product_number.close()

        file_product = open("product.txt","w")
        file_product.write(str(label_product))
        file_product.close()

        l = zpl.Label(30,100)
        height = 0

        l.origin(0,0)
        l.write_text("Nazov produktu", char_height=3, char_width=3, line_width=20, justification='C')
        l.endorigin()

        l.origin(0,5)
        l.write_text("Cislo produktu", char_height=3, char_width=3, line_width=20, justification='C')
        l.endorigin()

        l.origin(50,4)
        dm = simple_zpl2.QR_Barcode(data=product_f,model=2,magnification=7,error_correction='H',mask_value=1)
        l.write_text(dm)

        l.origin(70,4)
        l.write_graphic(Image.open(os.path.join(os.path.dirname(zpl.__file__), 'trollface-large.png')),10)
        print(l.dumpZPL())
        l.preview()
        try:
            mysocket.connect((host, port)) #connecting to host
            mysocket.send(b"^XA^FO0,0^A0N,36,36^FB240,1,0,C,0^FDNazov produktu^FS^FO0,60^A0N,36,36^FB240,1,0,C,0^FDCislo produktu^FS^FO600,48^FD^BQN,2,7,H,1^FDA  Q7LP202052^FS^FO840,48^GFA,2880,1440,15,0000000002AAAAAAA00000000000000000000BFFFFFFFFFF8000000000000000003F580000002DFFE800000000000000700000AAA80012FFC0000000000001C000075557A00007FE00000000000180001800002D54941FE000000000070000E000000092A000F000000000060002800568000000001C000000000C0014007407C000007C0F000000001800500B00003FFF6F8303C0000000300180B000000000000000E0000000700203016FF8000000000030000000600C180D000000005EC00018000000C0086030001800034038000C000000C01080C0000400080006000C00000180210100000400000001000600000180220600000200010000800600000100040800000200020000800600000300043000000200020000400600000700004002A8040002000040020000060000007FFF0000020000000700000C000001FFD7C0000200000003000018000007FFC0F0000202A8000180003800000E7FC03800003FFE0001C0007FF0051C7FC00E0000FE070000E001F554383FFFF0060001FCDF96A03801D000141FD57E070003FFFE005C180720000308000786003FFB0000030C06C02A02000001FE003F80000000CE0E80FFC000060078000F00000018261D03C0F8000C0000000600000002223A07003E00380000000600000541233A060007C1700000000200001FF113640C0001FFC0000000060000783892681803001400000000060018E00897D4180700000000000003001FE00012541007800000000000038007800093D43007E0000004000000E00002008650101E3C0000027C00007000020113D430FC1E000002E000003C000602166418FC03C00FF98000001E0003022674180600F010008000003F0007884E621806003E000187F0003EC007808C3A0C07003FC000C37800603807831C350003001AF800C0000060040FCA181C8003C0183F40400001C0021FC8181A4001F01803F000002780007FC0300D3001FC18005F00003E0000F7C03006CC00FF38000FE000000003E7C06007200073FE000FBF0000001FE3C06001D80060FE00060FFA8002FC23E04001C000303F800C007FFFFFF031C0C0006000181FF80C000C5FE83021C0C00070001C1FFE0C000C03801833E0C00018000C18FFF8000801801873C0C000180006083FFC000C0180187FC080000C00031807FF400C01801CFFC0C000060001F800FFF03C03C1FFFFE0C000060001F0003FFFFFFFFFFFFFC0C000060000700019FFFFFFFFFFFFC080000300003000307FFFFFFFFFFFC0C0000300001C001007FFFFFFFFFFC0C0000180000E003000FFFFFFFFFFC0C00001C0000700600073FFFFFFFD80800000600001C06000200FFFEF9980C00000700000F0C000600303833B80C0000038000038C000200301861B00C000000C20800FC000600603063F004000000E183007C0002006030C1E00C0000003040801F0006006020E3C00C0000001C306003F006006071FF000C0000001E0C18007F9E00E0F7F80004000000070306000BFFD5F7FEA0000C00000001C081800003FFFF2000000600000000F060700000000000004006000000003C180D0000000000018006000000000F07014000000160020202000000000380603A03EADD000402060000000000F01E01A801000018040200000000007E01E815A8000160080600000000000F80070017FFFE801002000000000001E000F4000000006006000000000000780003A000000700020000000000001E00001F6AAB70000600000000000007800000011000000600000000000001F00000000000000C00000000000000780000000000000C000000000000000F000000000000180000000000000007D80000000000300000000000000000FF000000000070000000000000000017F000000001C00000000000000000007F000000078000000000000000000007F800001E00000000000000000000007FC925F8000000000000000000000003FFFFC0000000000000000000000000149200000^XZ")#using bytes
            mysocket.close () #closing connection
        except:
            print("Error with the connection")

   else:
        #print("Vstup je 0")
