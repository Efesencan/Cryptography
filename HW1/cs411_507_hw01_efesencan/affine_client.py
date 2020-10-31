# coding=utf8
import requests # if this lib isn't installed yet --> pip install requests or pip3 intall requests
import collections
from sympy import *
from hw01_helper import *
#Dont forget to open vpn
API_URL = 'http://10.36.52.109:5000' # ATTN: This is the current server (do not change unless being told so) 

if __name__ == '__main__':
    my_id = 25083	# ATTN: change this to your id number. it should be 5 digit number
    
    cipher_text = None
    letter = None

    endpoint = '{}/{}/{}'.format(API_URL, "affine_game", my_id )
    response = requests.get(endpoint) 	#get your ciphertext and most freq. letter
    if response.ok:	#if you get your ciphertext succesfully
        c = response.json()
        cipher_text = c[0]    #this is your ciphertext
        letter = c[1] 	#the most frequent letter in your plaintext
        print(letter)
        print("***********************")
        print(cipher_text)
############ write decryption code for affine cipher here ##########
        print(collections.Counter(cipher_text).most_common(1)[0])
        # most frequent letter in the cipher text is 'D', so A is mapped to D 
        alpha = [i for i in range(1,29)]
        beta =  []
        pairs = []
        for i in alpha:
            beta_val = ((turkish_alphabet['D']) - ((ord('A') - ord('A')) * i)) % 29
            beta.append(beta_val)
        for i,j in zip(alpha,beta):
            pairs.append([i,j])
        print(beta)
        print("********")
        non_alpha = [' ','?','!','.']
        for i in pairs:
            print(i)
            plain =  ""
            for j in cipher_text:
                if j not in non_alpha:
                    alpha = i[0]
                    beta  = i[1]
                    y = turkish_alphabet[j]
                    number = (((y - beta) % 29) * (mod_inverse(alpha, 29))) % 29
                    plain += str(inv_turkish_alphabet[number])
                else:
                    plain += j
            print(plain)




####################################################################

    elif(response.status_code == 404):
        print("We dont have a student with this ID. Check your id num")
    else:
        print("It was supposed to work:( Contact your TA")


#CHECK YOUR ANSWER HERE
    query = "HAYVAN ÇİFTLİĞİNDEKİ AŞAĞI KESİMLERDEN HAYVANLARIN ÜLKENİN BÜTÜN HAYVANLARINDAN DAHA ÇOK ÇALIŞIP DAHA AZ YEDİKLERİNİ SÖYLEMEK HERHALDE YANLIŞ OLMAYACAKTI BUGÜN GERÇEKTEN DE KENDİSİ VE DOSTLARI HAYVAN ÇİFTLİĞİNDE ÖYLE ŞEYLER GÖRMÜŞLERDİ Kİ BUNLARI KENDİ ÇİFTLİKLERİNDE DE HEMEN UYGULAMAYA KOYMAYI DÜŞÜNÜYORLARDI SÖZLERİNİ HAYVAN ÇİFTLİĞİ İLE KOMŞULARI ARASINDA VAR OLAN VE SÜRMESİ GEREKEN DOSTLUK DUYGULARINI BİR KEZ DAHA VURGULAYARAK BİTİRMEK İSTİYORDU DOMUZLAR İLE İNSANLAR ARASINDA EN KÜÇÜK BİR ÇIKAR ÇATIŞMASI YOKTU OLMASI İÇİN BİR NEDEN DE GÖREMİYORDU VERDİKLERİ UĞRAŞLAR DA KARŞILAŞTIKLARI GÜÇLÜKLER DE BİRDİ İŞÇİ SORUNU HER YERDE AYNI DEĞİL MİYDİ BAY PİLKİNGTON TAM ÖNCEDEN HAZIRLADIĞI ANLAŞILAN ZEKİCE BİR ESPRİ YAPACAKTI Kİ GÜLMESİNİ TUTAMAYINCA KONUŞMASINI KESMEK ZORUNDA KALDI TOMBUL YANAKLARI MOSMOR KESİLİNCEYE KADAR KAHKAHALAR ATTIKTAN SONRA ESPRİYİ PATLATTI SİZLER AŞAĞI KESİMLERDEN HAYVANLARINIZLA UĞRAŞMAK ZORUNDAYSANIZ DEDİ BİZLER DE BİZİM AŞAĞI SINIFLARDAN İNSANLARIMIZLA UĞRAŞMAK ZORUNDAYIZ ESPRİ MASAYI KAHKAHAYI BOĞDU"	# ATTN: change this into the decrypted plaintext to be checked by the server. should be a string
    # Below is the sample code for sending your response back to the server
    endpoint = '{}/{}/{}/{}'.format(API_URL, "affine_game", my_id, query)
    response = requests.put(endpoint)
    if response.ok:
        c = response.json()
        print(c)
    elif (response.status_code == 404):
        print("check paramater types")
    elif(response.status_code == 406):
        print("Nope, Try again")
    elif(response.status_code == 401):
        print("Check your ID number")
    else:
        print("How did you get in here? Contact your TA")
