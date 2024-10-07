from django.db import models
class organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=255, unique=True)
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

    appid = models.CharField(max_length=255 , unique=True)
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

    name = models.CharField(max_length=255, choices=environmentchoices, unique=True)
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
    name = models.CharField(max_length=255, choices=reguinchoices,  unique=True)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class zone(models.Model):
    zonechoices = (
        ('dmz', 'DMZ'),
        ('cdc', 'core'),
    ) 
    name = models.CharField(max_length=255, choices=zonechoices,    unique=True)
    description = models.TextField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class serverrole(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    documentation = models.URLField(blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class server(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    #appid = models.ForeignKey(appid, on_delete=models.CASCADE)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    environment = models.ForeignKey(environment, on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    # server role can be many to many
    serverrole = models.ManyToManyField(serverrole, blank=True, null=True)
    configitems = models.JSONField(blank=True,null=True)
    def __str__(self):
        return self.name
    

# application 
# "Identifier","Name","Application Lifecycle Stage","SLA Applications","Crown Jewel","Application is owned by IT Vertical","Application has Service Owner.Name","Application has Service Owner.E-Mail","Planned Retiring Date","Actual Retiring Date","TIME Evaluation","Justification for Tolerate (TIME)","Application Subtype","Application has IT Service.ApnlId","Application has IT Service.IT Service Name","Description","Application has primary Capability","Application has primary Capability IT Owner","Application has primary Capability Business Owner","Application has secondary Capability","Deployment","Developed / Purchased","Application has Business Releationship Manager.Name","Application has Business Releationship Manager.E-Mail","Application has Business Owner.Name","Application has Business Owner.E-Mail","Application has Technical Subject Matter Expert.Name","Application has Technical Subject Matter Expert.E-Mail","Application has Product Owner.Name","Application has Product Owner.E-Mail","Application has Release Manager.Name","Application has Release Manager.E-Mail","Application has Application Subject Matter Expert.Name","Application has Application Subject Matter Expert.E-Mail","Application has Contract.ContractNumber","Application has Company Code.Code","Application has Company Code.Name","Application is used by Division","Application is used by Country.Iso","Application is used by Country.Name","Origin","Recovery Time Objective","Recovery Point Objective","Application requires Application","Application is required by Application","Alias","System of Record","System of Record Source Date","Top/Supporting Top","Application is supplied by Vendor","BRM Comment"
# 


    
    