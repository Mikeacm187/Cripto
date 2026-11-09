
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = """WMP BRHEMGQJ JD YSZ RWTBGQ ZA RZC QHAPMYO OJKHXEDA WLXCV QMMP DZTHWLGDGZMGJNYVJ XEJANX, FDX WCHS XYUWTZB YZ YQ LWQXWO CAYCZKH MT VTXZDZECMUX. RKJJ ZHQTZTH ECYW PQCUD MYFJ RFLHS ZUJPYQ YCPC, WZR YSZGNDOGQHEDTH NCYUFNOCUX WC JGZP XZ QONRCR, SVQ MLY LYD ULQO NUTEJRBUP.DY OFLX MYWJ OFHWP KXXE FDAP CANDOCG LO OJLNR F NARWP MI DKCFNPN RKRGOI XYWYWZ, FD KDSJ QKJPK, FYY VJGZPDQ BMDYD, LS ZSUTAZ DQZIC, LIBXPQCUFW CYJY ULYSDL LCZYW MMGWFTI. TYZ DZECMU MZJLJGZQ YSVR YSZPHQJPPJCGW JIDQWJO COJGZL BTGB XAZALJD MI DCCHU KCFZWDYU EJ JWPVRGCDRDNY! ZMPI ZJ WCDW DL RTIB YSVR GCDRDNY FDX IMZ YJR TYZ SJNPJLFCKDRXVJ, LIB KCVLFJ WSW QZU ITNRLSNO IWZH WMZNC TQ EHWXVLB, VLG DJ ZNECKZYBYUD, QSFTI, JEX., MPR YSVR JLXF TQ RKJDZ NNYBBRRD NRXDZQVJDQHAPMYO AZAXQTVP GCZCGX JD HLOROJ, QKJPK, JEX., HZ PZDO DIXDR YSVRRLIW IZHCVYTX EWPZBV XPQW SVTH ZMGJNYVRHI DL JFMMSJ; DRW RFHSNZRYSZPZNDZ FTFGB YSZW MLQC GPZL IPMGYJO? VT DR ND GQ TIBLF. CYJY GQ ECCHLNC TQ RKJ WPHJON RK OFH OJKHXEDA IZB WMCJSJMZPR YSZ ZTCGB, HCGFM DDIXDR FCZ GJDXCQIPY IWZH VJGZPDQ RGOI NNHHTZQ, TO FFYIMW MZ GTFWRHIOFDY OFHWP FDX WCHS VL NXHCQXP YPTFIR TQ GQMPMGWJO TDWTVRLTY; ITC UKTRGOQ WCONPQC YSVR FYDKDQD AOTDZJB CZQHRMGGQL OFH TOYONLI JWPTFRZYY,YSZ EQZJBKTFIB, ECC GFGJ-IZB, UFB-GTR, RW WJHSSZGP DKYQNPG, JEX.—XZSQQTFC FWG ZNWY FFYDBDJ—ZTHW ZVLXEZB NY Y XEVRH ZA QFEPPH? DR MLNRKEZL GPZL QZJQHQJ QDNO RKFE YOQ JSU CVAHX JD IZBQ MLQC GPZL UCJBXHPYED OFH NMMVXTIE TQ Y KPR DGZMGJNYVJ XAZALJD; EZE ZB NMMVXTIE BP ADSJLOD BCW QJPPX DL XZHC IPBPHJ DLWJCHCGNLOC GPOUHJY RKJTM SFCZLWX; YQIDD BP YFHZPLW QJP TFM VJGZPDQ YMPJDOGF CVAHX WW YSDQ UCJAHXD, ZJ HSVYVBPNE RKJ AMURPM HCTNRHSNZ RK OFH XJQW PSRUJXZ ITCHQ, LN WMP GWFWDYQRMCBMZPLG, WJRTOCMXSO, EZWG-GTR, HYN., NY RKJ RGOI NRDYP. PTCZMYJC,WMP NRXDDZLQTOW TQ KDPTIE ITNRLSNO UFNZQ GJ AUTDNGQL CYV MZCQ RMCDYWTHCLBEHWLOCG. HYQD XYVJD YUJ JL WPXMUI NFRBTIE YSVR F MYFJ HYB MZPTODDLJO ZB ZXADXTJLDQ XPRXDZQ NQ YLIPY ED OFH NVPHKFG VJWZAWNZI RKOFH TIBLATYSDQD UKNNC SWPNCQY OFH OZQLWPY FMLMYFYPM; GFO WT JZWFTI DCVAH TIRHWXZBLFEZ EJERCHS OUR BPGWJ YGVYTIAW CVAHX RMXQO ZH GZPBODDINNPJW. NGU U. VJMMGJME CAUCZQVQJ CAUPMGPJYOCG HDRK ECGV ZWHHHE YQIAYLQPY. YSZ RKQNNUNYB IWZH WMP DLWDO FWZNQ GPOUHJY RZT KSUJ WPHJON LXOMOJCVZOD VLG DJKHYTHCV (VQ N CYYJ AMXSO ULYS NLLPJLV) LSLYP SQNQJPPTI FMLMYFYPM, FYY HAPMW YSDLJ DZCPX NGPUWZ HSZPEK; WSW HCCQ ECCVJHMQLCZJV LMC HCJQVJO MQJ RGWM VLRYSZP KZM VJGZPDQ BCQJCVRLTYN, MLMBODOUR ZA WMPH DWP YONVZ, FYY WMPI WMP BLKQDAXQET RK OFH EVQN MZARRPNPFYDDHXE"""
    myKey = 'ASIMOV'
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
