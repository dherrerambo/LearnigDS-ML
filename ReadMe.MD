# Learning DataScience & MachineLearning

...

## Links
- https://github.com/krishnaik06
- Entendiendo las metricas: https://aprendeia.com/evaluando-el-error-en-los-modelos-de-regresion/

## Update all packages
- upgrade all packages: **`pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`**
- upgrade all packages: **`"C:\Python\py39\Scripts\pip.exe" freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`**
- upgrade all packages: **`C:\Python\py39\Scripts\pip.exe freeze | %{$_.split('==')[0]} | %{C:\Python\py39\Scripts\pip.exe install --upgrade $_}`***