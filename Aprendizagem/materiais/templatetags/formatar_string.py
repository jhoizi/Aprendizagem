from django import template

register = template.Library()

@register.filter(name='formatar_txt_para_html')
def formatar_txt_para_html(arquivo):
	with open('arquivos/'+str(arquivo), 'r') as f:
		texto = f.read()
		f.close()
		
		return texto

	return "" 