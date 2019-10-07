import VoltagePy

#setup
VoltagePy.setup('webdrivers/Chrome/76/linux_76',["--disable-gpu"])
browser = VoltagePy.open("http://localhost:8082/usuario/registrar")#https://www.duckduckgo.com

VoltagePy.fillForm(
    {
    'nome': 'HUNTER', 
    'email': 'HUNTER@EMAIL.COM',
    'senha': '!@#',
    'descricao': '!@#'
    },
    "form"
).submit()
#inputElement.send_keys(Keys.ENTER)

