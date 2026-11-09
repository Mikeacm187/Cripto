

import itertools, re,sys
import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False # if set to True, program doesn't print attempts
NUM_MOST_FREQ_LETTERS = 26 # attempts this many letters per subkey
MAX_KEY_LENGTH = 10 # will not attempt keys longer than this
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def cripto(chave):
	ciphertext = """WMP BRHEMGQJ JD YSZ RWTBGQ ZA RZC QHAPMYO OJKHXEDA WLXCV QMMP DZTHWLGDGZMGJNYVJ XEJANX, FDX WCHS XYUWTZB YZ YQ LWQXWO CAYCZKH MT VTXZDZECMUX. RKJJ ZHQTZTH ECYW PQCUD MYFJ RFLHS ZUJPYQ YCPC, WZR YSZGNDOGQHEDTH NCYUFNOCUX WC JGZP XZ QONRCR, SVQ MLY LYD ULQO NUTEJRBUP.DY OFLX MYWJ OFHWP KXXE FDAP CANDOCG LO OJLNR F NARWP MI DKCFNPN RKRGOI XYWYWZ, FD KDSJ QKJPK, FYY VJGZPDQ BMDYD, LS ZSUTAZ DQZIC, LIBXPQCUFW CYJY ULYSDL LCZYW MMGWFTI. TYZ DZECMU MZJLJGZQ YSVR YSZPHQJPPJCGW JIDQWJO COJGZL BTGB XAZALJD MI DCCHU KCFZWDYU EJ JWPVRGCDRDNY! ZMPI ZJ WCDW DL RTIB YSVR GCDRDNY FDX IMZ YJR TYZ SJNPJLFCKDRXVJ, LIB KCVLFJ WSW QZU ITNRLSNO IWZH WMZNC TQ EHWXVLB, VLG DJ ZNECKZYBYUD, QSFTI, JEX., MPR YSVR JLXF TQ RKJDZ NNYBBRRD NRXDZQVJDQHAPMYO AZAXQTVP GCZCGX JD HLOROJ, QKJPK, JEX., HZ PZDO DIXDR YSVRRLIW IZHCVYTX EWPZBV XPQW SVTH ZMGJNYVRHI DL JFMMSJ; DRW RFHSNZRYSZPZNDZ FTFGB YSZW MLQC GPZL IPMGYJO? VT DR ND GQ TIBLF. CYJY GQ ECCHLNC TQ RKJ WPHJON RK OFH OJKHXEDA IZB WMCJSJMZPR YSZ ZTCGB, HCGFM DDIXDR FCZ GJDXCQIPY IWZH VJGZPDQ RGOI NNHHTZQ, TO FFYIMW MZ GTFWRHIOFDY OFHWP FDX WCHS VL NXHCQXP YPTFIR TQ GQMPMGWJO TDWTVRLTY; ITC UKTRGOQ WCONPQC YSVR FYDKDQD AOTDZJB CZQHRMGGQL OFH TOYONLI JWPTFRZYY,YSZ EQZJBKTFIB, ECC GFGJ-IZB, UFB-GTR, RW WJHSSZGP DKYQNPG, JEX.—XZSQQTFC FWG ZNWY FFYDBDJ—ZTHW ZVLXEZB NY Y XEVRH ZA QFEPPH? DR MLNRKEZL GPZL QZJQHQJ QDNO RKFE YOQ JSU CVAHX JD IZBQ MLQC GPZL UCJBXHPYED OFH NMMVXTIE TQ Y KPR DGZMGJNYVJ XAZALJD; EZE ZB NMMVXTIE BP ADSJLOD BCW QJPPX DL XZHC IPBPHJ DLWJCHCGNLOC GPOUHJY RKJTM SFCZLWX; YQIDD BP YFHZPLW QJP TFM VJGZPDQ YMPJDOGF CVAHX WW YSDQ UCJAHXD, ZJ HSVYVBPNE RKJ AMURPM HCTNRHSNZ RK OFH XJQW PSRUJXZ ITCHQ, LN WMP GWFWDYQRMCBMZPLG, WJRTOCMXSO, EZWG-GTR, HYN., NY RKJ RGOI NRDYP. PTCZMYJC,WMP NRXDDZLQTOW TQ KDPTIE ITNRLSNO UFNZQ GJ AUTDNGQL CYV MZCQ RMCDYWTHCLBEHWLOCG. HYQD XYVJD YUJ JL WPXMUI NFRBTIE YSVR F MYFJ HYB MZPTODDLJO ZB ZXADXTJLDQ XPRXDZQ NQ YLIPY ED OFH NVPHKFG VJWZAWNZI RKOFH TIBLATYSDQD UKNNC SWPNCQY OFH OZQLWPY FMLMYFYPM; GFO WT JZWFTI DCVAH TIRHWXZBLFEZ EJERCHS OUR BPGWJ YGVYTIAW CVAHX RMXQO ZH GZPBODDINNPJW. NGU U. VJMMGJME CAUCZQVQJ CAUPMGPJYOCG HDRK ECGV ZWHHHE YQIAYLQPY. YSZ RKQNNUNYB IWZH WMP DLWDO FWZNQ GPOUHJY RZT KSUJ WPHJON LXOMOJCVZOD VLG DJKHYTHCV (VQ N CYYJ AMXSO ULYS NLLPJLV) LSLYP SQNQJPPTI FMLMYFYPM, FYY HAPMW YSDLJ DZCPX NGPUWZ HSZPEK; WSW HCCQ ECCVJHMQLCZJV LMC HCJQVJO MQJ RGWM VLRYSZP KZM VJGZPDQ BCQJCVRLTYN, MLMBODOUR ZA WMPH DWP YONVZ, FYY WMPI WMP BLKQDAXQET RK OFH EVQN MZARRPNPFYDDHXE"""
	
	print(vigenereCipher.decryptMessage(key, ciphertext))

def decryptor():
	#prefix="DFLV"  (why we know this? because we knew by advance that the key started with DFLV, by running the OTPdecryptor)
	guess=       "the xxxxxxxx xa the"
	prefix="DFLV"
	ciphertext = """WMP BRHEMGQJ JD YSZ RWTBGQ ZA RZC""" # QHAPMYO OJKHXEDA WLXCV QMMP DZTHWLGDGZMGJNYVJ XEJANX, FDX WCHS XYUWTZB YZ YQ LWQXWO CAYCZKH MT VTXZDZECMUX. RKJJ ZHQTZTH ECYW PQCUD MYFJ RFLHS ZUJPYQ YCPC, WZR YSZGNDOGQHEDTH NCYUFNOCUX WC JGZP XZ QONRCR, SVQ MLY LYD ULQO NUTEJRBUP.DY OFLX MYWJ OFHWP KXXE FDAP CANDOCG LO OJLNR F NARWP MI DKCFNPN RKRGOI XYWYWZ, FD KDSJ QKJPK, FYY VJGZPDQ BMDYD, LS ZSUTAZ DQZIC, LIBXPQCUFW CYJY ULYSDL LCZYW MMGWFTI. TYZ DZECMU MZJLJGZQ YSVR YSZPHQJPPJCGW JIDQWJO COJGZL BTGB XAZALJD MI DCCHU KCFZWDYU EJ JWPVRGCDRDNY! ZMPI ZJ WCDW DL RTIB YSVR GCDRDNY FDX IMZ YJR TYZ SJNPJLFCKDRXVJ, LIB KCVLFJ WSW QZU ITNRLSNO IWZH WMZNC TQ EHWXVLB, VLG DJ ZNECKZYBYUD, QSFTI, JEX., MPR YSVR JLXF TQ RKJDZ NNYBBRRD NRXDZQVJDQHAPMYO AZAXQTVP GCZCGX JD HLOROJ, QKJPK, JEX., HZ PZDO DIXDR YSVRRLIW IZHCVYTX EWPZBV XPQW SVTH ZMGJNYVRHI DL JFMMSJ; DRW RFHSNZRYSZPZNDZ FTFGB YSZW MLQC GPZL IPMGYJO? VT DR ND GQ TIBLF. CYJY GQ ECCHLNC TQ RKJ WPHJON RK OFH OJKHXEDA IZB WMCJSJMZPR YSZ ZTCGB, HCGFM DDIXDR FCZ GJDXCQIPY IWZH VJGZPDQ RGOI NNHHTZQ, TO FFYIMW MZ GTFWRHIOFDY OFHWP FDX WCHS VL NXHCQXP YPTFIR TQ GQMPMGWJO TDWTVRLTY; ITC UKTRGOQ WCONPQC YSVR FYDKDQD AOTDZJB CZQHRMGGQL OFH TOYONLI JWPTFRZYY,YSZ EQZJBKTFIB, ECC GFGJ-IZB, UFB-GTR, RW WJHSSZGP DKYQNPG, JEX.—XZSQQTFC FWG ZNWY FFYDBDJ—ZTHW ZVLXEZB NY Y XEVRH ZA QFEPPH? DR MLNRKEZL GPZL QZJQHQJ QDNO RKFE YOQ JSU CVAHX JD IZBQ MLQC GPZL UCJBXHPYED OFH NMMVXTIE TQ Y KPR DGZMGJNYVJ XAZALJD; EZE ZB NMMVXTIE BP ADSJLOD BCW QJPPX DL XZHC IPBPHJ DLWJCHCGNLOC GPOUHJY RKJTM SFCZLWX; YQI
#DD BP YFHZPLW QJP TFM VJGZPDQ YMPJDOGF CVAHX WW YSDQ UCJAHXD, ZJ HSVYVBPNE RKJ AMURPM HCTNRHSNZ RK OFH XJQW PSRUJXZ ITCHQ, LN WMP GWFWDYQRMCBMZPLG, WJRTOCMXSO, EZWG-GTR, HYN., NY RKJ RGOI NRDYP. PTCZMYJC,WMP NRXDDZLQTOW TQ KDPTIE ITNRLSNO UFNZQ GJ AUTDNGQL CYV MZCQ RMCDYWTHCLBEHWLOCG. HYQD XYVJD YUJ JL WPXMUI NFRBTIE YSVR F MYFJ HYB MZPTODDLJO ZB ZXADXTJLDQ XPRXDZQ NQ YLIPY ED OFH NVPHKFG VJWZAWNZI RKOFH TIBLATYSDQD UKNNC SWPNCQY OFH OZQLWPY FMLMYFYPM; GFO WT JZWFTI DCVAH TIRHWXZBLFEZ EJERCHS OUR BPGWJ YGVYTIAW CVAHX RMXQO ZH GZPBODDINNPJW. NGU U. VJMMGJME CAUCZQVQJ CAUPMGPJYOCG HDRK ECGV ZWHHHE YQIAYLQPY. YSZ RKQNNUNYB IWZH WMP DLWDO FWZNQ GPOUHJY RZT KSUJ WPHJON LXOMOJCVZOD VLG DJKHYTHCV (VQ N CYYJ AMXSO ULYS NLLPJLV) LSLYP SQNQJPPTI FMLMYFYPM, FYY HAPMW YSDLJ DZCPX NGPUWZ HSZPEK; WSW HCCQ ECCVJHMQLCZJV LMC HCJQVJO MQJ RGWM VLRYSZP KZM VJGZPDQ BCQJCVRLTYN, MLMBODOUR ZA WMPH DWP YONVZ, FYY WMPI WMP BLKQDAXQET RK OFH EVQN MZARRPNPFYDDHXE"""
	hackedMessage = hackVigenere(ciphertext,prefix)

	if hackedMessage != None:
		print('Copying hacked message to clipboard:')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Failed to hack encryption.')


def test():
    #teste
	message = "the sky is blue and porto is the best and vitoria is fine and chelsea is good also"
	chave = "DIDI"
	cipher = vigenereCipher.encryptMessage(key,message)
	print(cipher)
	hackedMessage = hackVigenere(cipher)

	if hackedMessage != None:
		print('Copying hacked message to clipboard:')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Failed to hack encryption.')
	#original = vigenereCipher.decryptMessage(chave,criptograma)
	#print(original == mensagem)


def main():
	ciphertext = """WMP BRHEMGQJ JD YSZ RWTBGQ ZA RZC QHAPMYO OJKHXEDA WLXCV QMMP DZTHWLGDGZMGJNYVJ XEJANX, FDX WCHS XYUWTZB YZ YQ LWQXWO CAYCZKH MT VTXZDZECMUX. RKJJ ZHQTZTH ECYW PQCUD MYFJ RFLHS ZUJPYQ YCPC, WZR YSZGNDOGQHEDTH NCYUFNOCUX WC JGZP XZ QONRCR, SVQ MLY LYD ULQO NUTEJRBUP.DY OFLX MYWJ OFHWP KXXE FDAP CANDOCG LO OJLNR F NARWP MI DKCFNPN RKRGOI XYWYWZ, FD KDSJ QKJPK, FYY VJGZPDQ BMDYD, LS ZSUTAZ DQZIC, LIBXPQCUFW CYJY ULYSDL LCZYW MMGWFTI. TYZ DZECMU MZJLJGZQ YSVR YSZPHQJPPJCGW JIDQWJO COJGZL BTGB XAZALJD MI DCCHU KCFZWDYU EJ JWPVRGCDRDNY! ZMPI ZJ WCDW DL RTIB YSVR GCDRDNY FDX IMZ YJR TYZ SJNPJLFCKDRXVJ, LIB KCVLFJ WSW QZU ITNRLSNO IWZH WMZNC TQ EHWXVLB, VLG DJ ZNECKZYBYUD, QSFTI, JEX., MPR YSVR JLXF TQ RKJDZ NNYBBRRD NRXDZQVJDQHAPMYO AZAXQTVP GCZCGX JD HLOROJ, QKJPK, JEX., HZ PZDO DIXDR YSVRRLIW IZHCVYTX EWPZBV XPQW SVTH ZMGJNYVRHI DL JFMMSJ; DRW RFHSNZRYSZPZNDZ FTFGB YSZW MLQC GPZL IPMGYJO? VT DR ND GQ TIBLF. CYJY GQ ECCHLNC TQ RKJ WPHJON RK OFH OJKHXEDA IZB WMCJSJMZPR YSZ ZTCGB, HCGFM DDIXDR FCZ GJDXCQIPY IWZH VJGZPDQ RGOI NNHHTZQ, TO FFYIMW MZ GTFWRHIOFDY OFHWP FDX WCHS VL NXHCQXP YPTFIR TQ GQMPMGWJO TDWTVRLTY; ITC UKTRGOQ WCONPQC YSVR FYDKDQD AOTDZJB CZQHRMGGQL OFH TOYONLI JWPTFRZYY,YSZ EQZJBKTFIB, ECC GFGJ-IZB, UFB-GTR, RW WJHSSZGP DKYQNPG, JEX.—XZSQQTFC FWG ZNWY FFYDBDJ—ZTHW ZVLXEZB NY Y XEVRH ZA QFEPPH? DR MLNRKEZL GPZL QZJQHQJ QDNO RKFE YOQ JSU CVAHX JD IZBQ MLQC GPZL UCJBXHPYED OFH NMMVXTIE TQ Y KPR DGZMGJNYVJ XAZALJD; EZE ZB NMMVXTIE BP ADSJLOD BCW QJPPX DL XZHC IPBPHJ DLWJCHCGNLOC GPOUHJY RKJTM SFCZLWX; YQI
DD BP YFHZPLW QJP TFM VJGZPDQ YMPJDOGF CVAHX WW YSDQ UCJAHXD, ZJ HSVYVBPNE RKJ AMURPM HCTNRHSNZ RK OFH XJQW PSRUJXZ ITCHQ, LN WMP GWFWDYQRMCBMZPLG, WJRTOCMXSO, EZWG-GTR, HYN., NY RKJ RGOI NRDYP. PTCZMYJC,WMP NRXDDZLQTOW TQ KDPTIE ITNRLSNO UFNZQ GJ AUTDNGQL CYV MZCQ RMCDYWTHCLBEHWLOCG. HYQD XYVJD YUJ JL WPXMUI NFRBTIE YSVR F MYFJ HYB MZPTODDLJO ZB ZXADXTJLDQ XPRXDZQ NQ YLIPY ED OFH NVPHKFG VJWZAWNZI RKOFH TIBLATYSDQD UKNNC SWPNCQY OFH OZQLWPY FMLMYFYPM; GFO WT JZWFTI DCVAH TIRHWXZBLFEZ EJERCHS OUR BPGWJ YGVYTIAW CVAHX RMXQO ZH GZPBODDINNPJW. NGU U. VJMMGJME CAUCZQVQJ CAUPMGPJYOCG HDRK ECGV ZWHHHE YQIAYLQPY. YSZ RKQNNUNYB IWZH WMP DLWDO FWZNQ GPOUHJY RZT KSUJ WPHJON LXOMOJCVZOD VLG DJKHYTHCV (VQ N CYYJ AMXSO ULYS NLLPJLV) LSLYP SQNQJPPTI FMLMYFYPM, FYY HAPMW YSDLJ DZCPX NGPUWZ HSZPEK; WSW HCCQ ECCVJHMQLCZJV LMC HCJQVJO MQJ RGWM VLRYSZP KZM VJGZPDQ BCQJCVRLTYN, MLMBODOUR ZA WMPH DWP YONVZ, FYY WMPI WMP BLKQDAXQET RK OFH EVQN MZARRPNPFYDDHXE"""
	hackedMessage = hackVigenere(ciphertext)

	if hackedMessage != None:
		print('Copying hacked message to clipboard:')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Failed to hack encryption.')


def findRepeatSequencesSpacings(message):
	# Goes through the message and finds any 3 to 5 letter sequences
	# that are repeated. Returns a dict with the keys of the sequence and
	# values of a list of spacings (num of letters between the repeats).

	# Use a regular expression to remove non-letters from the message.
	message = NONLETTERS_PATTERN.sub('', message.upper())

	# Compile a list of seqLen-letter sequences found in the message.
	seqSpacings = {} # keys are sequences, values are list of int spacings
	for seqLen in range(3, 6):
		for seqStart in range(len(message) - seqLen):
			# Determine what the sequence is, and store it in seq
			seq = message[seqStart:seqStart + seqLen]

			# Look for this sequence in the rest of the message
			for i in range(seqStart + seqLen, len(message) - seqLen):
				if message[i:i + seqLen] == seq:
					# Found a repeated sequence.
					if seq not in seqSpacings:
						seqSpacings[seq] = [] # initialize blank list

					# Append the spacing distance between the repeated
					# sequence and the original sequence.
					seqSpacings[seq].append(i - seqStart)
	return seqSpacings


def getUsefulFactors(num):
	# Returns a list of useful factors of num. By "useful" we mean factors
	# less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
	# returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]

	if num < 2:
		return [] # numbers less than 2 have no useful factors

	factors = [] # the list of factors found

	# When finding factors, you only need to check the integers up to
	# MAX_KEY_LENGTH.
	for i in range(2, MAX_KEY_LENGTH + 1): # don't test 1
		if num % i == 0:
			factors.append(i)
			factors.append(int(num / i))
	if 1 in factors:
		factors.remove(1)
	return list(set(factors))


def getItemAtIndexOne(x):
	return x[1]


def getMostCommonFactors(seqFactors):
	# First, get a count of how many times a factor occurs in seqFactors.
	factorCounts = {} # key is a factor, value is how often if occurs

	# seqFactors keys are sequences, values are lists of factors of the
	# spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
	# 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
	for seq in seqFactors:
		factorList = seqFactors[seq]
		for factor in factorList:
			if factor not in factorCounts:
				factorCounts[factor] = 0
			factorCounts[factor] += 1

	# Second, put the factor and its count into a tuple, and make a list
	# of these tuples so we can sort them.
	factorsByCount = []
	for factor in factorCounts:
		# exclude factors larger than MAX_KEY_LENGTH
		if factor <= MAX_KEY_LENGTH:
			# factorsByCount is a list of tuples: (factor, factorCount)
			# factorsByCount has a value like: [(3, 497), (2, 487), ...]
			factorsByCount.append( (factor, factorCounts[factor]) )

	# Sort the list by the factor count.
	factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

	return factorsByCount


def kasiskiExamination(ciphertext):
	# Find out the sequences of 3 to 5 letters that occur multiple times
	# in the ciphertext. repeatedSeqSpacings has a value like:
	# {'EXG': [192], 'NAF': [339, 972, 633], ... }
	repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

	# See getMostCommonFactors() for a description of seqFactors.
	seqFactors = {}
	for seq in repeatedSeqSpacings:
		seqFactors[seq] = []
		for spacing in repeatedSeqSpacings[seq]:
			seqFactors[seq].extend(getUsefulFactors(spacing))

	# See getMostCommonFactors() for a description of factorsByCount.
	factorsByCount = getMostCommonFactors(seqFactors)

	# Now we extract the factor counts from factorsByCount and
	# put them in allLikelyKeyLengths so that they are easier to
	# use later.
	allLikelyKeyLengths = []
	for twoIntTuple in factorsByCount:
		allLikelyKeyLengths.append(twoIntTuple[0])

	return allLikelyKeyLengths


def getNthSubkeysLetters(n, keyLength, message):
	# Returns every Nth letter for each keyLength set of letters in text.
	# E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
	#      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
	#      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
	#      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

	# Use a regular expression to remove non-letters from the message.
	message = NONLETTERS_PATTERN.sub('', message.upper())

	i = n - 1
	letters = []
	while i < len(message):
		letters.append(message[i])
		i += keyLength
	return ''.join(letters)


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength,prefix=""):
	# Determine the most likely letters for each letter in the key.
	ciphertextUp = ciphertext.upper()
	# allFreqScores is a list of mostLikelyKeyLength number of lists.
	# These inner lists are the freqScores lists.
	mostLikelyKeyLength = mostLikelyKeyLength - len(prefix)
	allFreqScores = []
	for nth in range(1, mostLikelyKeyLength + 1):
		nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

		# freqScores is a list of tuples like:
		# [(<letter>, <Eng. Freq. match score>), ... ]
		# List is sorted by match score. Higher score means better match.
		# See the englishFreqMatchScore() comments in freqAnalysis.py.
		freqScores = []
		for possibleKey in LETTERS:
			possiblek =  possibleKey
			decryptedText = vigenereCipher.decryptMessage(possiblek, nthLetters)
			keyAndFreqMatchTuple = (possiblek, freqAnalysis.englishFreqMatchScore(decryptedText))
			freqScores.append(keyAndFreqMatchTuple)
		# Sort by match score
		freqScores.sort(key=getItemAtIndexOne, reverse=True)

		allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

	if not SILENT_MODE:
		for i in range(len(allFreqScores)):
			# use i + 1 so the first letter is not called the "0th" letter
			print('Possible letters for letter %s of the key: ' % (i + 1), end='')
			for freqScore in allFreqScores[i]:
				print('%s ' % freqScore[0], end='')
			print() # print a newline

	# Try every combination of the most likely letters for each position
	# in the key.
	
	for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
		# Create a possible key from the letters in allFreqScores
		possibleKey = ''
		for i in range(mostLikelyKeyLength):
			possibleKey += allFreqScores[i][indexes[i]][0]

		if not SILENT_MODE:
			print('Attempting with key: %s' % (prefix + possibleKey))

		decryptedText = vigenereCipher.decryptMessage(prefix + possibleKey, ciphertextUp)

		if detectEnglish.isEnglish(decryptedText, wordPercentage=60, ):
			# Set the hacked ciphertext to the original casing.
			origCase = []
			for i in range(len(ciphertext)):
				if ciphertext[i].isupper():
					origCase.append(decryptedText[i].upper())
				else:
					origCase.append(decryptedText[i].lower())
			decryptedText = ''.join(origCase)

			# Check with user to see if the key has been found.
			print('Possible encryption hack with key %s:' % (possibleKey))
			print(decryptedText[:200]) # only show first 200 characters
			print()
			print('Enter D for done, or just press Enter to continue hacking:')
			response = input('> ')

			if response.strip().upper().startswith('D'):
				return decryptedText

	# No English-looking decryption found, so return None.
	return None


def hackVigenere(ciphertext,prefix=""):
	# First, we need to do Kasiski Examination to figure out what the
	# length of the ciphertext's encryption key is.
	allLikelyKeyLengths = kasiskiExamination(ciphertext)
	allLikelyKeyLengths.sort()
	allLikelyKeyLengths = list(filter( lambda x : x> len(prefixo) ,allLikelyKeyLengths ))# map( lambda z : z-len(prefixo), allLikelyKeyLengths )  ))
	
	hackedMessage=None
	if not SILENT_MODE:
		keyLengthStr = ''
		for keyLength in allLikelyKeyLengths:
			keyLengthStr += '%s ' % (keyLength)
		print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')

	for keyLength in allLikelyKeyLengths:
		if not SILENT_MODE:
			print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
		hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength,prefixo)
		if hackedMessage != None:
			break

	
	# If none of the key lengths we found using Kasiski Examination
	# worked, start brute-forcing through key lengths.
	if hackedMessage == None:
		if not SILENT_MODE:
			print('Unable to hack message with likely key length(s). Brute forcing key length...')
		lll = 1 + len(prefix)
		for keyLength in range(lll, MAX_KEY_LENGTH + 1):
			# don't re-check key lengths already tried from Kasiski
			if keyLength not in allLikelyKeyLengths:
				if not SILENT_MODE:
					print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
				hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength,prefix)
				if hackedMessage != None:
					break
	return hackedMessage


# the main() function.
if __name__ == '__main__':
	#main()
	#test()

	if len(sys.argv)>2 and  sys.argv[1] == "cripto":
		cripto(sys.argv[2])
	else:
		decryptor()
