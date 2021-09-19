from rest_framework import serializers
from upload.models import Value,Sensor,Device,Reading

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Value
        fields=('val1', 'val2', 'val3')

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('sensor_id', 'values')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'sensors')

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('reading_id', 'devices')