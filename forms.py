# -*- coding: utf-8 -*-
from web import form
import re
import db

# Expresiones regulares necesarias:

#formatoVisa=re.compile(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}')


# Funciones necesarias para las validaciones

def fooFunction():
    pass


"""
EJEMPLO DE FORMULARIO PARA DARSE DE ALTA

formularioInscripcion = form.Form(
            form.Textbox(
                "nombre",
                form.notnull, 
                class_="form-control", 
                id="nombreId",
                description="Nombre: " 
            ),
            form.Textbox(
                "apellidos",
                form.notnull, 
                class_="form-control", 
                id="apellidosId", 
                description="Apellidos: "
            ),
            form.Textbox(
                "dni",
                form.notnull,
                class_="form-control", 
                id="dniId", 
                description="DNI: "
            ),
            form.Textbox(
                "email",
                form.notnull,
                form.regexp(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}',
                 'Formato de email incorrecto'), 
                class_="form-control", 
                id="emailId", 
                description=u"Correo electrónico: "
            ),
            form.Dropdown(
                "dia", 
                [(d, d) for d in range(1,32)],
                id="diaID",
                description=u"Día de nacimiento: ",
            ),
            form.Dropdown(
                "mes",
                [(1,'Enero'),(2,'Febrero'),(3,'Marzo'),(4,'Abril'),(5,'Mayo'),(6,'Junio'),
                (7,'Julio'),(8,'Agosto'),(9,'Septiembre'),(10,'Octubre'),(11,'Noviembre'),(12,'Diciembre')],
                id="mesID",
                description="Mes de nacimiento: "
            ),
            form.Dropdown(
                "anio", 
                [d for d in range(1930,2006)],
                id="anioID",
                description=u"Año de nacimiento: "
            ),
            form.Textarea(
                "direccion",
                form.notnull, 
                class_="form-control", 
                id="direccionId",
                description=u"Dirección: " 
            ),
            form.Textbox(
                "username",
                form.notnull, 
                class_="form-control", 
                id="usernameId", 
                description="Nombre de usuario: "
            ),
            form.Password(
                "password1",
                form.notnull,
                class_="form-control",
                id="password1Id",
                description=u"Contraseña: "
            ),
            form.Password(
                "password2",
                form.notnull,
                class_="form-control",
                id="password2Id",
                description=u"Repita la contraseña: "
            ),
            form.Radio(
                'formaPago',
                [["VISA","VISA  "],["contraReembolso","Contra reembolso"]],
                form.notnull,
                id="formaPagoId",
                description="Forma de pago: "
            ),
            form.Textbox(
                "visa",
                class_="form-control", 
                id="visaId", 
                description="Número de tarjeta VISA: ",
            ),
            form.Checkbox(
                "acepto",
                description="Acepto las condiciones de uso ",
                id="aceptoId",
                value="si"
            ),
            validators = [
                form.Validator(u"Fecha incorrecta", lambda x: ((int(x.mes)==2 and int(x.dia)<=28)) or 
                (int(x.mes) in [4,6,9,11] and int(x.dia)<31) or (int(x.mes) in [1,3,5,7,8,10,12]) 
                or (int(x.mes)==2 and int(x.dia)==29 and esBisiesto(x.anio))),
                form.Validator(u"La contraseña debe tener al menos 7 caracteres",lambda x: len(x.password1)>6),
                form.Validator(u"Las contraseñas no coinciden", lambda x: x.password1 == x.password2),
                form.Validator(u"Debe introducir un número de tarjeta válido",lambda x: (x.formaPago=="contraReembolso") 
                    or (x.formaPago=="VISA" and formatoVisa.match(x.visa))),
                form.Validator(u"Debe aceptar los términos y condiciones",lambda x: x.acepto=="si")
            ]
        ) 

"""
