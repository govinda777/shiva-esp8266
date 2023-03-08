# Hospedagem, como maximizar sua produtividade e minimizar seu custo de desenvolvimento.

Objetivo: Passar uma visão rasa sobre as plataformas que podemos hospedar seus projetos.
Irei abordar sobre a lider de mercado em dispositivos IOT, Tuya IOT Plataform.

## Crescimento

O mercado global de Internet das Coisas (IoT) terá a receita US$ 1,1 trilhão até 2024, com grande parte do crescimento vindo de wearables (dispositivos vestíveis), diz a GlobalData, empresa líder de dados e análise.

![Crescimento global IOT](img/grafico-mercado-iot.jpeg?raw=true "Crescimento global IOT")

https://www.globaldata.com/global-iot-market-will-surpass-1-trillion-mark-2024-says-globaldata/


Um estudo da CI&T e da Opinion Box, realizado com 1241 executivos brasileiros, apontou que 44,8% dos profissionais já veem a IoT como indispensável para o crescimento das empresas. A pesquisa ainda mostra que 22% dos líderes empresariais adotaram ações em 2020 para digitalizar os negócios.

## Investimento nacional

Plano Nacional de IoT
Apesar da expansão das redes de internet de banda larga e dos dispositivos inteligentes, o ecossistema da internet das coisas (IoT) no Brasil ainda enfrenta alguns desafios. Segundo os especialistas da área, falta mais estímulo, mais monitoramento, mais inovação e menos regulamentação para o mercado de IoT avançar no país. Por isso, está em vigor desde junho de 2019 o Plano Nacional de Internet das Coisas (Decreto n°9854), que visa fomentar essa tecnologia no Brasil e melhorar a qualidade de vida e aumentar a eficiência na prestação de serviços.

## O que são?

A Internet das Coisas (IoT – Internet of Things) é conhecida pelo acrónimo IoT (do inglês Internet of Things), tendo sido definida pela Internet Society como “a extensão da conectividade de rede e capacidade de computação para objetos, dispositivos, sensores e outros artefactos que normalmente não são considerados computadores”.

https://welectric.pt/2018/03/09/o-que-e-a-internet-das-coisas-iot-internet-of-things/

## Dispositivos

- Tomadas inteligentes


- Interrupitores inteligentes


- Sensores de movimentos


- Sensores de presença



## Experiência

Nos ultimos meses venho estudando muito sobre IOT 

Já temos muitos dispositivos prontos que realizam diversas funcionalidades padrões como :

Tomadas inteligentes
Interrupitores inteligentes
Sensores de movimentos
Sensores de prossimidades

Esses produtos prontos, são muito bons pois muitas vezes para você implementar se projeto de IOT muitas vezes vocês mão precisará escrever se quer uma linha de código.

Porem muitos sensores possuem um grande custo e talves não faça exatamente o que você precisa para o seu projeto.

Por exemplo, imagine que você queira desenvolver um sistema de rega inteligente de plantas.

Você precisará dos seguintes materiais:

- Valvula solenoude 12v

- Modúlo rele wifi

- Kit rega de plantas (mangueira e irrigadores)

## Céu é o limite

Alem de você poder comprar seus componente de IOT conforme descrito anteriormente, você pode tambem criar os seus próprios dispositivos IOT, utilizando como BASE nosso amigo chamado 


## Projeto rega inteligente

Nesse projeto, utilizei os seguintes componentes:


 Modulo rele Wifi:

![Rele Wifi](img/rele-wifi.jpeg?raw=true "Rele Wifi")



# Hospedagem

* [tuya](https://www.tuya.com/)
- [video-aula](https://www.youtube.com/watch?v=qVZJyHJsF9A)
- [tuya-iot-plataform](https://iot.tuya.com/)

## Como configurar

-

## Como Autenticar ??!Important

-

## Como gerenciar um projeto
-
## Custos de Hospedagem
-
## Healph Checke dos [ESP8266]
-
## ??????
-
## Comunicação [Node MCU ESP8266] X Tuya

# Micro controlador

## [Como configurar] 
-
-
*
*


### O que vc vai precisar

* [pythom3](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
* [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)
* [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
* [esptool](https://micropython.org/download/esp8266/) (python -m pip install esptool)
* [screen](/...)

### Liberar acesso a porta serial

sudo chmod a+rw /dev/ttyUSB0 

###  Como instalar o firmware micropython esp8266

esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash

esptool.py --port /dev/ttyUSB0 --chip esp8266 --baud 115200 write_flash --flash_size=detect -fm dout 0 esp8266-20210902-v1.17.bin

###  Enviar os arquivos para o esp8266

ampy -p /dev/ttyUSB0 get boot.py
ampy -p /dev/ttyUSB0 ls

ampy -p /dev/ttyUSB0 put main.py
ampy -p /dev/ttyUSB0 mkdir infra
ampy -p /dev/ttyUSB0 put infra/mqtt.py infra/mqtt.py
ampy -p /dev/ttyUSB0 put infra/wifi.py infra/wifi.py
ampy -p /dev/ttyUSB0 put micropython/awsCer/root-CA.der
ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.cert.der
ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.private.der

###  Como entrar no dispositivo

screen /dev/ttyUSB0 115200

### Exemplo de Execução

- Execução do programa em micropython
![Execução do programa em micropython](/docs/img/exemplo-execucao.jpeg?raw=true "Execução do programa em micropython")

- Recebimento de mensagem AWS IOT CORE
![Recebimento de mensagem AWS IOT CORE](/docs/img/exemplo-recebimento-mgs-aws.jpeg?raw=true "Recebimento de mensagem AWS IOT CORE")

- Mensagem no terminal
![Mensagem no terminal](/docs/img/informativo-de-msg.jpeg?raw=true "Mensagem no terminal")

- Listagem de arquivos
![Listagem de arquivos](/docs/img/ls-no-esp.jpeg?raw=true "Listagem de arquivos")

### Como instalar as dependencias

micropython -m upip install 

### Como criar certificado .DER

openssl x509 -in teste.cert.pem -out teste.cert.der -outform DER
openssl x509 -in root-CA.crt -out root-CA.der -outform DER
openssl rsa -in teste.private.key -out teste.private.der -outform DER

## [Como testar]

### O que vc vai precisar

* ????? (https://linuxize.com/post/??????4/)
* ????? (https://linuxize.com/post/?????-20.04/)

### Como executar

python -m unittest src/leilao/test_avaliador.py

https://docs.python.org/pt-br/dev/library/unittest.html

## Links Uteis

https://create.arduino.cc/projecthub/B45i/getting-started-with-arduino-cli-7652a5

https://hub.docker.com/r/solarbotics/arduino-cli

https://hub.docker.com/r/arduino/arduino-cli

https://arduino.github.io/arduino-cli/0.20/configuration/

https://github.com/ExploreEmbedded/Hornbill-Examples/tree/master/arduino-esp32/AWS_IOT

https://platformio.org/lib/show/1743/AWS-SDK-ESP

https://pythonforundergradengineers.com/micropython-install.html

https://micropython.org/unicorn/

https://docs.micropython.org/en/latest/reference/packages.html

https://thingspeak.com/

https://pubsubclient.knolleary.net/api

https://nerdyelectronics.com/how-to-connect-nodemcu-to-aws-iot-core/

[Tutorial configuração Thing](https://www.youtube.com/watch?v=28FS2qix2u4&ab_channel=ElectronicsInnovation)

[Arduino ESP8266 filesystem uploader](https://github.com/esp8266/arduino-esp8266fs-plugin)


https://www.globaldata.com/global-iot-market-will-surpass-1-trillion-mark-2024-says-globaldata/

https://www.connectdata.net/post/o-que-falta-para-impulsionar-o-mercado-de-iot-no-brasil

https://welectric.pt/2018/03/09/o-que-e-a-internet-das-coisas-iot-internet-of-things/


https://youtu.be/uEsKZGOxNKw

https://www.youtube.com/watch?v=R26QhFQYzcw&ab_channel=Felps

https://www.youtube.com/watch?v=6XZzvliTNqo&ab_channel=MrZoreta

https://www.nodemcu.com/

https://nodemcu.readthedocs.io/en/release/

## Atalhos 

- Wifi => "VIVOFIBRA-6CA1","Pedro2203"

- AWS_IOT_ENDPOINT="a12sdqmvxrmcs4-ats.iot.us-east-1.amazonaws.com"

- ROOT_CA_CERT_PATH              "certificate/AmazonRootCA1.pem"

- CLIENT_CERT_PATH               "certificate/4a172e63c4899b4843d093b0bfe924e8abe6e8c52d05bdde7e65e7b9efafc8b7-certificate.pem.crt"

- CLIENT_PRIVATE_KEY_PATH        "certificate/4a172e63c4899b4843d093b0bfe924e8abe6e8c52d05bdde7e65e7b9efafc8b7-private.pem.key"

- Como abrir a IDE do Arduino

  sudo /home/luan-govinda/arduino-1.8.13/arduino

- Executar Docker

  docker build -t ar .

  docker run -it ar /bin/bash

- Como apagar a pasta 

  rm -rf /home/luan-govinda/projetos/Arduino/iot-monitor

- Configuração das preferencias da IDE
  
  Em "Ficheiro > Preferencia > Localização do bloco de rascunho" apontar para o diretório "iot-monitor/arduino-libs"

- Como compilar no Arduino_cli

  arduino-cli compile --fqbn esp8266:esp8266:nodemcu program