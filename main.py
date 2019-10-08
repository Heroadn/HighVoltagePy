import VoltagePy
import helper

#setup
VoltagePy.setup('webdrivers/Chrome/76/linux_76',["--disable-gpu"])
browser = VoltagePy.open("http://localhost:8082/usuario/registrar")#https://www.duckduckgo.com

#usuario form
data = helper.fileToJson('usuario.json')
VoltagePy.fillForm(data,"form")
#form.submit()
#inputElement.send_keys(Keys.ENTER)

