from django.db import models

# Create your models here.
class SensorData(models.Model):
    # for each product
    device_id=models.CharField(max_length=20)

    # DHT 11 values
    humidity=models.CharField(max_length=20)
    temperature=models.CharField(max_length=20)

    # soil moidture sensor values
    soil_moisture=models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


    def __str__(self) -> str:
        return f"{self.device_id}"