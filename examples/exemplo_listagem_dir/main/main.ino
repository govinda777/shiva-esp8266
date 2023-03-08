#include <FS.h>

void setup() {
  Serial.begin(115200);

  Serial.println("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");
  delay(5000);
  Serial.println("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");
  delay(5000);
  Serial.println("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");

  Serial.println("Iniciando SPIFFS-----------------");

  if(SPIFFS.begin())
  {
    Serial.println("SPIFFS iniciado");
  }
  else {
    Serial.println("ERRO: SPIFFS");
  }

  infoFiles();
  
  listFiles();

  //saveFile();

  //listFiles();
  
  //infoFiles();

  //readFile();

  
  Serial.println("------------End-----------------");
}

void readFile()
{
  delay(5000);
  
  Serial.println("Read File-----------------");

  File file = SPIFFS.open("/log.txt", "r");

  if(file) {
    Serial.printf("Nome: %s - %u bytes\n", file.name(), file.size());
    while (file.available()){
      Serial.println(file.readStringUntil('\n'));  
    }

    file.close();
  }

  Serial.println("End Read File-----------------");  
}

void saveFile() 
{
  delay(5000);
  
  Serial.println("Save File-----------------");

  File file;

  file = SPIFFS.open("/log.txt", "a");

  if(file) {
    file.println("Inicializando...");
    file.printf("Registro %u\r\n", millis());
    file.close();
  }
}

void infoFiles()
{
  delay(5000);
  
  Serial.println("Informações sobre SPIFFS-----------------");

  FSInfo fsInfo;
  SPIFFS.info(fsInfo);

  Serial.printf("totalBytes: %u\nusedBytes: %u\nfreeBytes: %u\nblockSize: %u\npageSize: %u\nmaxOpenFiles: %u\nmaxPathLength: %u\n",
                fsInfo.totalBytes,
                fsInfo.usedBytes,
                fsInfo.totalBytes - fsInfo.usedBytes,
                fsInfo.blockSize,
                fsInfo.pageSize,
                fsInfo.maxOpenFiles,
                fsInfo.maxPathLength);

}

void listFiles()
{
  delay(5000);
  
  Serial.println("Listando aquivos-----------------");
                
  Dir dir = SPIFFS.openDir("/");
  while(dir.next()) {
    Serial.printf(" %s - %u bytes\n", dir.fileName().c_str(), dir.fileSize());
  }

  Serial.println("End Listando aquivos-----------------");
}

void loop() {
  // put your main code here, to run repeatedly:

}