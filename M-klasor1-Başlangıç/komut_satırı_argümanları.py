# Gerekli paketleri içe aktarın
import argparse
# Argümanı oluşturun Argümanları ayrıştırın ve ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())

# Kullanıcıya dostça bir mesaj görüntüleyin
print("Hi there {}, it's nice to meet you!".format(args["name"]))

# C:\Users\sude nur toprak\Desktop\Algoritma\model_eğitme>python komut_satırı_argümanları.py --name Sude