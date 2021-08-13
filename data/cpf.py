import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cpf = ui.dialog1()
		r = requests.get(f'https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/cpf.php?consulta={cpf}')
			msg='A consulta está funcionando normalmente, porém o CPF não foi encontrado.'
		else:
			msg=r.replace('''"''', '').replace(',','\n').replace('}', '').replace('{', '')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
