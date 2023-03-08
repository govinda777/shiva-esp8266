## Como executar

sudo chmod +x start.sh 

./start.sh

## Como executar usando o mosquitto_sub

mosquitto_sub --cafile root-CA.crt -h a12sdqmvxrmcs4-ats.iot.us-east-1.amazonaws.com  -t "sdk/test/Python" -p 8883 -d --cert teste.cert.pem --key teste.private.key