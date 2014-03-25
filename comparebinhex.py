def convertnumtobase (num, base) :
	len=len(num)
        dec = 0;
	for i in range (0,len):
		dec=dec+int(s[len-i-1])*(base**i)
	return dec

def compare(bin_num, hex_num)
	bin_val=convertnumtobase(bin_num,2)
	hex_val=convertnumtobase(hex_num,16)
	print ('value of ' + bin_num + '= ' + `bin_val`)
	print ('value of ' + hex_num + '= ' + `hex_val`)

print compare(1011, b)
