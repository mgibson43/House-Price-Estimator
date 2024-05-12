from django.db import models

class State(models.Model):
  id = models.AutoField(primary_key=True)
  state = models.CharField(max_length=100)

  def publish(self):
    self.save()

  def __str__(self):
    return self.state

class CityState(models.Model):
  id = models.AutoField(primary_key=True)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = models.CharField(max_length=100)

  def publish(self):
    self.save()

  def __str__(self):
    return f'City: {self.city} | State: {self.state}'

class CityCodes(models.Model):
  id = models.AutoField(primary_key=True)
  city = models.ForeignKey(CityState, on_delete=models.CASCADE)
  code = models.FloatField()

  def publish(self):
    self.save()

  def __str__(self):
    return f'City Code: {self.code} | City: {self.city}'