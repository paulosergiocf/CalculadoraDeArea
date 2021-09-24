def convHatoAlq(n):
	alq = n / 2.42
	return alq


def convHatoM2(n):
	m2 = n * 10000
	return m2


def convAlqtoHa(n):
	ha = n * 2.42
	return ha


def convAlqtoM2(n):
	m2 = n * 24200
	return m2


def convM2toHa(n):
	ha = n / 10000
	return ha


def convM2toAlq(n):
	alq = n / 24200
	return alq


def M2Format(n):
	res = f'{n:_.2f} m²'.replace(".",",")
	return res.replace("_",".")


def HaFormat(n):
	return f'{n:.4f} Ha'.replace(".",",")


def AlqFormat(n):
	return f'{n:.2f} Alq. Pta.'.replace(".",",")
