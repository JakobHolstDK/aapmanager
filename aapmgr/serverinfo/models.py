from django.db import models
class Server(models.Model):
    environment_choices = [
        ('TEST / DEV', 'Test and Development'),
        ('QA / PREPROD', 'Quality Assurance and Pre-Production'),
        ('PROD', 'Production')
    ]
    os_choices = [
        ('RHEL', 'Red Hat Enterprise Linux'),
        ('Oracle Linux', 'Oracle Linux'),
        ('Rocky Linux', 'Rocky Linux'),
        ('CentOS', 'CentOS'),
        ('Ubuntu', 'Ubuntu'),
        ('Debian', 'Debian'),
        ('SLES', 'SUSE Linux Enterprise Server'),
        ('Windows', 'Windows Server'),
        ('AIX', 'AIX'),
        ('IBM i', 'IBM i')
    ]
    os_arch_choices = [
        ('x86_64', '64-bit'),
        ('i386', '32-bit'),
        ('ppc64', 'PowerPC 64-bit'),
    ]

    healthball_choices = [
        ('green', 'https://img.shields.io/badge/ok-green.svg'),
        ('yellow', 'https://img.shields.io/badge/warning-yellow.svg'),
        ('red', 'https://img.shields.io/badge/error-red.svg'),
        ('blue', 'https://img.shields.io/badge/info-blue.svg')
    ]

    aap_patch_env_choices = [
        ('TEST / DEV', 'Test and Development'),
        ('QA / PREPROD', 'Quality Assurance and Pre-Production'),
        ('PROD', 'Production')
    ]

    aap_patch_batch_choices = [
        ('1', 'Patch on day one of the patch window'),
        ('2', 'Patch on day two of the patch window'),
        ('3', 'Patch on day three of the patch window'),
        ('4', 'Patch on day four of the patch window')
    ]

    aap_patch_patchtime_choices = [
        ('00', 'Patch at 00:00 and 4 hours ahead'),
        ('01', 'Patch at 01:00 and 4 hours ahead'),
        ('02', 'Patch at 02:00 and 4 hours ahead'),
        ('03', 'Patch at 03:00 and 4 hours ahead'),
        ('04', 'Patch at 04:00 and 4 hours ahead'),
        ('05', 'Patch at 05:00 and 4 hours ahead'),
        ('06', 'Patch at 06:00 and 4 hours ahead'),
        ('07', 'Patch at 07:00 and 4 hours ahead'),
        ('08', 'Patch at 08:00 and 4 hours ahead'),
        ('09', 'Patch at 09:00 and 4 hours ahead'),
        ('10', 'Patch at 10:00 and 4 hours ahead'),
        ('11', 'Patch at 11:00 and 4 hours ahead'),
        ('12', 'Patch at 12:00 and 4 hours ahead'),
        ('13', 'Patch at 13:00 and 4 hours ahead'),
        ('14', 'Patch at 14:00 and 4 hours ahead'),
        ('15', 'Patch at 15:00 and 4 hours ahead'),
        ('16', 'Patch at 16:00 and 4 hours ahead'),
        ('17', 'Patch at 17:00 and 4 hours ahead'),
        ('18', 'Patch at 18:00 and 4 hours ahead'),
        ('19', 'Patch at 19:00 and 4 hours ahead'),
        ('20', 'Patch at 20:00 and 4 hours ahead'),
        ('21', 'Patch at 21:00 and 4 hours ahead'),
        ('22', 'Patch at 22:00 and 4 hours ahead'),
        ('23', 'Patch at 23:00 and 4 hours ahead')
    ]
    os_eol_state_choices = [
        ('active', 'Active'),
        ('eol', 'End of Life'),
        ('eol-extended', 'End of Life Extended Support'),
        ('eol-unsupported', 'End of Life Unsupported')
    ]


    hostname = models.CharField(max_length=128, primary_key=True)
    cname = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    appid = models.ForeignKey('appid', on_delete=models.CASCADE)
    environment = models.CharField(max_length=50, choices=environment_choices, null=True, blank=True)
    detected = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='active')
    healthball = models.URLField(max_length=200, blank=True, null=True, default='https://img.shields.io/badge/ok-green.svg')
    os = models.CharField(max_length=50, choices=os_choices)
    os_version = models.CharField(max_length=50, blank=True, null=True)
    os_arch = models.CharField(max_length=50, choices=os_arch_choices)
    os_lastboot = models.CharField(max_length=50,  blank=True, null=True)
    os_lastpatch = models.CharField(max_length=50,  blank=True, null=True)
    os_uptime = models.CharField(max_length=50, blank=True, null=True)
    os_installed = models.DateField(null=True, blank=True)
    os_lastmodified = models.DateTimeField(null=True, blank=True)
    os_eol = models.DateField(null=True, blank=True)
    os_eol_state = models.CharField(max_length=50, choices=os_eol_state_choices, blank=True, null=True)
    aap_autopatch = models.BooleanField(default=False)
    aap_lastpatch = models.CharField(max_length=50, blank=True, null=True)
    aap_nextpatch = models.CharField(max_length=50, blank=True, null=True)
    aap_scheduled_patching = models.JSONField(blank=True, null=True)
    aap_patch_env = models.CharField(max_length=50, choices=aap_patch_env_choices, blank=True, null=True)
    aap_patch_batch = models.CharField(max_length=50, choices=aap_patch_batch_choices, blank=True, null=True)
    aap_patch_patchtime = models.CharField(max_length=50, choices=aap_patch_patchtime_choices, blank=True, null=True)
    aap_patch_window_scheduled_url_jan = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_feb = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_mar = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_apr = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_may = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_jun = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_jul = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_aug = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_sep = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_oct = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_nov = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_url_dec = models.URLField(max_length=512, blank=True, null=True)
    aap_patch_window_scheduled_date = models.DateField(null=True, blank=True)
    aap_patch_window_scheduled_jan = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_feb = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_mar = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_apr = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_may = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_jun = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_jul = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_aug = models.CharField(max_length=50, null=True, blank=True) 
    aap_patch_window_scheduled_sep = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_oct = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_nov = models.CharField(max_length=50, null=True, blank=True)
    aap_patch_window_scheduled_dec = models.CharField(max_length=50, null=True, blank=True)

        

        


    def __str__(self):
        return self.hostname
    
    class Meta:
        db_table = 'server'
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'
        ordering = ['os', 'hostname']
# the id must auto increment, otherwise the data will be overwritten
# patchpeers table holds the pears 1:n relationship with the server table
# the hostname is the foreign key

class patchpeers(models.Model):
    hostname = models.CharField(max_length=128, primary_key=True)
    peername = models.CharField(max_length=128)

    def __str__(self):
        return self.hostname
    
    class Meta:
        db_table = 'patchpeers'
        verbose_name = 'Patch Peer'
        verbose_name_plural = 'Patch Peers'
        ordering = ['hostname']

    



class appid(models.Model):
    appid = models.CharField(max_length=50, primary_key=True)
    appname = models.CharField(max_length=255)
    appowner = models.CharField(max_length=255)
    appcontact = models.CharField(max_length=255)
    appstatus = models.CharField(max_length=50, default='active')

    def __str__(self):
        return self.appid

    class Meta:
        db_table = 'appid'
        verbose_name = 'Application ID'
        verbose_name_plural = 'Application IDs'
        ordering = ['appid']

class aap_patchday(models.Model):
    aap_patch_env_choices = [
        ('TEST / DEV', 'Test and Development'),
        ('QA / PREPROD', 'Quality Assurance and Pre-Production'),
        ('PROD', 'Production')
    ]
    aap_patch_env = models.CharField(max_length=50, choices=aap_patch_env_choices, primary_key=True)
    aap_patch_date_january = models.DateField(null=True, blank=True)
    aap_patch_date_february = models.DateField(null=True, blank=True)
    aap_patch_date_march = models.DateField(null=True, blank=True)
    aap_patch_date_april = models.DateField(null=True, blank=True)
    aap_patch_date_may = models.DateField(null=True, blank=True)
    aap_patch_date_june = models.DateField(null=True, blank=True)
    aap_patch_date_july = models.DateField(null=True, blank=True)
    aap_patch_date_august = models.DateField(null=True, blank=True)
    aap_patch_date_september = models.DateField(null=True, blank=True)
    aap_patch_date_october = models.DateField(null=True, blank=True)    
    aap_patch_date_november = models.DateField(null=True, blank=True)
    aap_patch_date_december = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.aap_patch_env
    
    class Meta:
        db_table = 'aap_patchday'
        verbose_name = 'AAP Patch Day'
        verbose_name_plural = 'AAP Patch Days'
        ordering = ['aap_patch_env']




class Asset(models.Model):
    host_name = models.CharField(max_length=255, primary_key=True) 
    computer_name = models.CharField(max_length=255, null=True, blank=True)
    environment = models.CharField(max_length=255, null=True, blank=True)
    data_center_location = models.CharField(max_length=255, null=True, blank=True)
    vmware_datacenter = models.CharField(max_length=255, null=True, blank=True)
    function = models.CharField(max_length=255, null=True, blank=True)
    technical_contacts = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    support_hours = models.CharField(max_length=255, null=True, blank=True)
    guard = models.CharField(max_length=255, null=True, blank=True)
    application_id = models.CharField(max_length=50, null=True, blank=True)
    application_name = models.CharField(max_length=255, null=True, blank=True)
    a_number = models.CharField(max_length=50, blank=True, null=True)
    deploy_date = models.DateField(null=True, blank=True)
    asset_status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.host_name
    
    class Meta:
        db_table = 'asset'
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        ordering = ['host_name']

    