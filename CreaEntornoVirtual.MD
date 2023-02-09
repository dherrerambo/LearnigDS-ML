# 1. Crear enviroment

Crear el entorno virtual
~~~python
python -m venv .venv
~~~

Activar el entorno virtual
~~~python
.venv\Scripts\activate
~~~

Instalar librerias
~~~python
pip install wheel
pip install dist\datatools-1.3.1-py2.py3-none-any.whl
pip install pandas snowflake-connector-python simple_salesforce unidecode pyperclip awswrangler
~~~

Necesarias para ejecucion de Notebook
~~~python
pip install ipykernel
pip install python-dotenv
~~~

Revisar librerias
~~~python
pip list
~~~

Crear listado de requerimientos
~~~python
pip freeze > test/requirements.txt
~~~

Desactivar el enviroment.
~~~python
deactivate
~~~
