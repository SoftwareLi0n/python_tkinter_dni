import requests
import json
import tkinter
from tkinter import messagebox as mb

ventana = tkinter.Tk()
ventana.title("Software Lion")
# ventana.geometry("400x300")

frm = tkinter.Frame(ventana)
frm.grid(column=0, row=0, padx=(25, 25))

label1 = tkinter.Label(frm, text="Consulta DNI", font="-weight bold")
label1.grid(row=0, column=0, pady=10)

archoText = 20

#TXT DNI Buscar
txtDNIBuscar = tkinter.Entry(frm, width=archoText)
txtDNIBuscar.grid(row=1, column=0)

#Crear boton
btnBuscar = tkinter.Button(frm, text="Buscar", command= lambda: buscar(), width=17, bg="blue", fg='white')
btnBuscar.grid(row=2, column=0, pady=(0, 10))

##RESPONSE
fila = 4
lblTDni = tkinter.Label(frm, text="DNI - CUI: ")
lblTDni.grid(row=fila, column=0, sticky = "w")
fila = fila + 1

txtDniCui = tkinter.Entry(frm, width=archoText)
txtDniCui.grid(row=fila, column=0, sticky="w")
fila = fila + 1

lblTDni = tkinter.Label(frm, text="Paterno: ")
lblTDni.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtPaterno = tkinter.Entry(frm, text="",width=archoText)
txtPaterno.grid(row=fila, column=0, sticky="w")
fila = fila + 1

lblTDni = tkinter.Label(frm, text="Materno: ")
lblTDni.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtMaterno = tkinter.Entry(frm, width=archoText)
txtMaterno.grid(row=fila, column=0, sticky="w")
fila = fila + 1

lblTDni = tkinter.Label(frm, text="Nombres: ")
lblTDni.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtNombres = tkinter.Entry(frm, width=archoText)
txtNombres.grid(row=fila, column=0, sticky="w")
fila = fila + 1

lblTDni = tkinter.Label(frm, text="Sexo: ")
lblTDni.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtSexo = tkinter.Entry(frm, width=archoText)
txtSexo.grid(row=fila, column=0, sticky="w", pady=(0, 10))
##END RESPONSE

def buscar():
    dni = txtDNIBuscar.get()

    txtDniCui.delete(0, tkinter.END)
    txtPaterno.delete(0, tkinter.END)
    txtMaterno.delete(0, tkinter.END)
    txtNombres.delete(0, tkinter.END)
    txtSexo.delete(0, tkinter.END)

    url = "https://www.softwarelion.xyz/api/reniec/reniec-dni"
    _json = { "dni": dni }
    token = "Bearer $ingresa a qui tu token"
    _headers = { 'Content-Type': 'application/json', 'Authorization': token } 

    response = requests.post(url, data=json.dumps(_json), headers=_headers)

    datajson = response.json()

    if(datajson["success"] == False):
        mb.showwarning("Jesús", datajson["message"])
        return

    persona = (datajson["result"])

    txtPaterno.insert(0, persona["paterno"])
    txtMaterno.insert(0, persona["materno"])
    txtNombres.insert(0, persona["nombres"])
    txtDniCui.insert(0, dni +"-"+persona["codigoVerificacion"])
    txtSexo.insert(0, persona["sexo"])

    print(persona["paterno"])

#Abre la ventana
ventana.mainloop()