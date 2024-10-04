from django.db import models
class organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    suource = models.URLField(blank=True, null=True)
    documentation = models.URLField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class appid(models.Model):
    statuschoices = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )

    appid = models.CharField(max_length=255)
    appname = models.CharField(max_length=255)
    appowner = models.CharField(max_length=255)
    appcontact = models.CharField(max_length=255)
    aapstatus = models.CharField(max_length=255, choices=statuschoices)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.appid
    
# Create your models here.
class environment(models.Model):
    environmentchoices = (
        ('development', 'Development'),
        ('test', 'Test'),
        ('production', 'Production'),
        ('qa', 'QA'),
        ('preproduction', 'Pre-Production')
    )

    name = models.CharField(max_length=255, choices=environmentchoices)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
  
class region(models.Model):
    reguinchoices = (
        ('emea', 'Europe, Middle East'),
        ('apac', 'Acia Pacific'),
        ('amer', 'Americas'),
        ('afri', 'Africa')
    )
    name = models.CharField(max_length=255, choices=reguinchoices)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class zone(models.Model):
    zonechoices = (
        ('dmz', 'DMZ'),
        ('cdc', 'core'),
    ) 
    name = models.CharField(max_length=255, choices=zonechoices)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class serverrole(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    documentation = models.URLField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class server(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    appid = models.ForeignKey(appid, on_delete=models.CASCADE)
    environment = models.ForeignKey(environment, on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    # server role can be many to many
    serverrole = models.ManyToManyField(serverrole, blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    

    

    
    