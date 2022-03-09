#include <OneWire.h>


void turn_off_EC(void);
void turn_on_EC(void);
int DS18S20_Pin = 2; //DS18S20 Signal pin on digital 2
OneWire ds(DS18S20_Pin);  // on digital pin 2
//temperature

#include <TCA9548A.h>

#include "AS726X.h"

AS726X sensorIR;
AS726X sensorVS;
TCA9548A I2CMux;                  // Address can be passed into the constructor


#include "DFRobot_PH.h"
#include <EEPROM.h>
#define PH_PIN A0         // on analog pin 0
float ph_voltage,ph_Value,temperature = 25;
DFRobot_PH ph;
//pH


#include "DFRobot_EC.h"
#define EC_PIN A2         // on analog pin 1
float ec_voltage,ec_Value;
DFRobot_EC ec;


int trans_pin=6;



void turn_off_EC(void){

  digitalWrite(trans_pin,LOW);
  
}
  
  
  

void turn_on_EC(void){

  digitalWrite(trans_pin,HIGH);
}

void setup(void) {
  
  ph.begin();
  Wire.begin();
  Serial.begin(115200);
  I2CMux.begin(Wire);
  I2CMux.openChannel(0);
    sensorVS.begin();// Wire instance is passed to the library
  I2CMux.closeChannel(0);
  I2CMux.openChannel(1);
  sensorIR.begin();
  pinMode(trans_pin,OUTPUT);
  turn_off_EC();
  digitalWrite(10,LOW);
  I2CMux.closeAll();              // Set a base state which we know (also the default state on power on)
  Serial.println("test");
  while(Serial.readString() != "t\n"){}
  temperature = readTemperature();         // read your temperature sensor to execute temperature compensation
  Serial.println("Temperature: ");
  Serial.print(temperature,1);
  Serial.println("test");
  while(Serial.readString() != "t\n"){}
  Serial.println(" ");
  Serial.println("Readings: ");
}

void loop(void) {
//  float temperature = readTemperature();
//  Serial.println(temperature);
//  delay(100); //just here to slow down the output so it is easier to read
//temperature

// prints in csv format:
// temp, ph, ec, turbidity, visible light, ir sensor

    static unsigned long timepoint = millis();
    if(millis()-timepoint>1000U){                  //time interval: 1s
        timepoint = millis();
        //temperature = 32.0;
        
        ph_voltage = analogRead(PH_PIN)/1024.0*5000;  // read the ph_voltage
        ph_Value = ph.readPH(ph_voltage,temperature);  // convert ph_voltage to pH with temperature compensation
         delay(1500);
        //Serial.println("Hello");
        turn_on_EC();
        delay(1500);
        ec_voltage = analogRead(EC_PIN)/1024.0*5000;   // read the voltage
        ec_Value = ec.readEC(ec_voltage,temperature);  // convert voltage to EC with temperature compensation
        delay(1500);
        turn_off_EC();
        delay(1500);

        //Serial.print("temperature:");
        Serial.print(temperature,1);
        //Serial.println("^C");
        //Serial.print("pH:");
        Serial.print(",");
        Serial.print(ph_Value,2);
        
        //Serial.print("EC:");
        Serial.print(",");
        Serial.print(ec_Value);
        Serial.print(",");
        //Serial.println("ms/cm");
    }
    ph.calibration(ph_voltage,temperature);           // calibration process by Serail CMD
//ph & EC

    int sensorValue = analogRead(A1);// read the input on analog pin 2:
    float voltage = sensorValue * (5.0 / 1024.0); // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //Serial.print("Turbidity: ");
    Serial.print(voltage); // print out the value you read:
    Serial.print(",");
    //delay(500);
//turbidity

  I2CMux.openChannel(0);
  sensorVS.takeMeasurementsWithBulb();
  //Prints all measurements
    //Visible readings
    //Serial.print(" Reading: V[");
    Serial.print(sensorVS.getCalibratedViolet(), 2);
    Serial.print(",");
    //Serial.print("] B[");
    Serial.print(sensorVS.getCalibratedBlue(), 2);
    Serial.print(",");
    //Serial.print("] G[");
    Serial.print(sensorVS.getCalibratedGreen(), 2);
    Serial.print(",");
    //Serial.print("] Y[");
    Serial.print(sensorVS.getCalibratedYellow(), 2);
    Serial.print(",");
    //Serial.print("] O[");
    Serial.print(sensorVS.getCalibratedOrange(), 2);
    Serial.print(",");
    //Serial.print("] R[");
    Serial.print(sensorVS.getCalibratedRed(), 2);
    Serial.print(",");
    //Serial.println("]");
  I2CMux.closeChannel(0);
  //delay(1000);
  I2CMux.openChannel(1);
  sensorIR.takeMeasurementsWithBulb();

    //Near IR readings
    //Serial.print(" Reading: R[");
    Serial.print(sensorIR.getCalibratedR(), 2);
    //Serial.print("] S[");
    Serial.print(",");
    Serial.print(sensorIR.getCalibratedS(), 2);
    //Serial.print("] T[");
    Serial.print(",");
    Serial.print(sensorIR.getCalibratedT(), 2);
    //Serial.print("] U[");
    Serial.print(",");
    Serial.print(sensorIR.getCalibratedU(), 2);
    //Serial.print("] V[");
    Serial.print(",");
    Serial.print(sensorIR.getCalibratedV(), 2);
    //Serial.print("] W[");
    Serial.print(",");
    Serial.println(sensorIR.getCalibratedW(), 2);
    //Serial.println("]");
  I2CMux.closeChannel(1);

  //delay(1000);








  
}
















float readTemperature(){
  //returns the temperature from one DS18S20 in DEG Celsius

  byte data[12];
  byte addr[8];

  if ( !ds.search(addr)) {
      //no more sensors on chain, reset search
      ds.reset_search();
      return -1000;
  }

  if ( OneWire::crc8( addr, 7) != addr[7]) {
      Serial.println("CRC is not valid!");
      return -1000;
  }

  if ( addr[0] != 0x10 && addr[0] != 0x28) {
      Serial.print("Device is not recognized");
      return -1000;
  }

  ds.reset();
  ds.select(addr);
  ds.write(0x44,1); // start conversion, with parasite power on at the end

  byte present = ds.reset();
  ds.select(addr);
  ds.write(0xBE); // Read Scratchpad


  for (int i = 0; i < 9; i++) { // we need 9 bytes
    data[i] = ds.read();
  }

  ds.reset_search();

  byte MSB = data[1];
  byte LSB = data[0];

  float tempRead = ((MSB << 8) | LSB); //using two's compliment
  float TemperatureSum = tempRead / 16;

  return TemperatureSum;

}
