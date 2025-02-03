# Prueba tecnica data engineer

## Objetivos
**El objetivo consiste en tranformar un archivo csv infectado en un archivo psv que pueda ser leido por los cientificos tanto en formato csv como psv**

La prueba busca alcanzar los siguientes objetivos especificos:

- Cada valor debe estar separada por el cáracter ‘|’ (Pipe). Ej: (v_1|v_2|v_3)
- Cada línea debe tener el mismo número de columnas.
- Cada valor debe tener el quotechar ‘”’(Doble comillas). Ej. Ej: (“v_1”|”v_2”|”v_3”)
- El archivo deberá estar almacenado con un enconding de UTF-8

## Pasos
La prueba 1 fue desarrollada siguiendo los pasos a continuación:

1. Se codifico un script que pueda simplificar todo el proceso en una sola funcion [fix_and_convert_csv_to_psv.py](fix_and_convert_csv_to_psv.py) (Pasos del proceso detallados en el script)
2. Se realizo un test para verificar que el script cumpla con los objetivos especificos leyendo el psv en el formato correspondiente tanto en psv como en csv [test_fix_and_convert_csv_to_psv.ipynb](test_fix_and_convert_csv_to_psv.ipynb)

<div align="center">
  <strong style="font-size: 24px;">Desarrollador</strong>
</div>

<div align="center">
    <img src="https://media.licdn.com/dms/image/v2/D4D03AQE1TSjtN5JVdA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1692654837750?e=1744243200&v=beta&t=toedh8ucnlZs336eqJVei73vfH8Js_MMS7Zf9ZlambU" alt="LinkedIn">
</div>

<div align="center">

  Aquí esta mi Linkedin si te quieres poner en contacto conmigo: </br>
  <a href="https://www.linkedin.com/in/franco-aguilera-0686ba255/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</div>