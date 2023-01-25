# API Calculadora Do Teorema de Pitágoras



### Proposta

Criar uma Api Simples com um endpoint para ser consumido, onde será feito uma requisição para  realizar o calculo do **Teorema de Pitágoras** e retornar o resultado para o **Front-End**, esse calculo será realizado com os dois parâmetros que serão encaminhados através da requisição por **Query strings**, esses valores correspondem a diferentes lados de um triangulo.

### Recursos utilizados no projeto

* ##### Python3

* ##### Flask


### COMO Consumir a API

**Base URL**: https://flask-api-app.herokuapp.com/api/pythagorean-theorem

os parâmetros devem ser enviados via query strings são: a, b ou h
**Exemplo**: Para calcular o valor passando um Cateto e Hipotenusa e descobrir o valor do outro Cateto: https://flask-api-app.herokuapp.com/api/pythagorean-theorem?a=4&h5

**Exemplo**: Para calcular o valor passando os dois Catetos e descobrir a Hipotenusa: https://flask-api-app.herokuapp.com/api/pythagorean-theorem?a=4&b3

A resposta será retornada no seguinte padrão.
`{`
  `"message": "",`
  `"payload": ,`
  `"statusCode":` 
`}`

###  Link para Testar a calculadora 

https://calculadora-teorema-pitagoras.netlify.app/


  ### Link para o Repositório da Calculadora

https://github.com/GustavoAugustoBatistaMelo/calculadora-teorema-pitagoras



