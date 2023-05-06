import os
import shutil

from_dir='C:/Users/arthur/Downloads'
to_dir='C:/Users/arthur'
file_name="/github.com_byjusbrazil_pro_1-1_c78_templatedoprojeto.zip"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    arquivo = os.path.splitext(i)
    print(arquivo)

path1 = from_dir + "/github.com_byjusbrazil_pro_1-1_c78_templatedoprojeto.zip"
path2 = "C:/Users/arthur/Documents/Byjus/Arquivos_Documentos"
path3 = to_dir+"Arquivos_Documentos"+'/'+file_name

if os.path.exists(path2):
    print("Movendo " + file_name + "......")

    shutil.move(path1,path3)

else:
    os.makedirs(path2)
    print("Movendo " + file_name + "......")
    shutil.move(path1, path3)