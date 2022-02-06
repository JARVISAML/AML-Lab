#include "AS726X.h"

AS726X sensor;
#define VLPIN D4
#define IRPIN D5

void setup() {
  Wire.begin();
  Serial.begin(115200);

  sensor.begin();
}

void loop() {
  sensor.takeMeasurementsWithBulb();
  //Prints all measurements
  if (sensor.getVersion() == SENSORTYPE_AS7262)
  {
    //Visible readings
    Serial.print(" Reading: V[");
    Serial.print(sensor.getCalibratedViolet(), 2);
    Serial.print("] B[");
    Serial.print(sensor.getCalibratedBlue(), 2);
    Serial.print("] G[");
    Serial.print(sensor.getCalibratedGreen(), 2);
    Serial.print("] Y[");
    Serial.print(sensor.getCalibratedYellow(), 2);
    Serial.print("] O[");
    Serial.print(sensor.getCalibratedOrange(), 2);
    Serial.print("] R[");
    Serial.print(sensor.getCalibratedRed(), 2);
  }
  else if (sensor.getVersion() == SENSORTYPE_AS7263)
  {
    //Near IR readings
    Serial.print(" Reading: R[");
    Serial.print(sensor.getCalibratedR(), 2);
    Serial.print("] S[");
    Serial.print(sensor.getCalibratedS(), 2);
    Serial.print("] T[");
    Serial.print(sensor.getCalibratedT(), 2);
    Serial.print("] U[");
    Serial.print(sensor.getCalibratedU(), 2);
    Serial.print("] V[");
    Serial.print(sensor.getCalibratedV(), 2);
    Serial.print("] W[");
    Serial.print(sensor.getCalibratedW(), 2);
   }

  Serial.print("] temp[");
  Serial.print(sensor.getTemperature(), 1);
  Serial.print("]");

  Serial.println();
}
