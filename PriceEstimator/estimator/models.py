from django.db import models

class State(models.Model):
  # id = models.AutoField(primary_key=True)
  id = models.CharField(max_length=100, primary_key=True)

  def publish(self):
    self.save()

  def __str__(self):
    return self.id

class CityState(models.Model):
  # id = models.AutoField(primary_key=True)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  id = models.CharField(max_length=100, primary_key=True)

  def publish(self):
    self.save()

  def __str__(self):
    return self.id

class CityCode(models.Model):
  # id = models.AutoField(primary_key=True)
  city = models.ForeignKey(CityState, on_delete=models.CASCADE)
  id = models.FloatField(primary_key=True)

  def publish(self):
    self.save()

  def __str__(self):
    return f'{self.id}'