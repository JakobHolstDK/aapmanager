from django.db import models


# a definition of en execution environment, contains "
# name: the name of the environment
# description: a description of the environment
# version: the version of the environment
# automationhub_id: the id of the environment in the automationhub
# 1 to n relationship with pip packagesids
# 1 to n relationship with ansible collectionsids 
# 1 to n relationship with ansible rolesids 
# 1 to n relationship with redhat repositoriesids
# 1 to n relationship with redhat packagesids

class EEDefinition(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  version = models.CharField(max_length=100)
  automationhub = models.ForeignKey('AutomationHub', on_delete=models.CASCADE)
  baseimage = models.ForeignKey('Baseimages', on_delete=models.CASCADE)
  buildfiles = models.ManyToManyField('Buildfiles')
  pip_packages = models.ManyToManyField('PipPackage')
  ansible_collections = models.ManyToManyField('AnsibleCollection')
  ansible_roles = models.ManyToManyField('AnsibleRole')
  redhat_repositories = models.ManyToManyField('RedhatRepository')
  redhat_packages = models.ManyToManyField('RedhatPackage')

class Baseimages(models.Model):
  name = models.CharField(max_length=100)
  version = models.TextField()

class Buildfiles(models.Model):
  name = models.CharField(max_length=100)
  version = models.TextField()
  content = models.TextField()


class AutomationHub(models.Model):
  name = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  description = models.TextField()
  version = models.CharField(max_length=100)
  verify = models.BooleanField()
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
# a definition of a pip package
# name: the name of the package
# version: the version of the package
# automationhub_id: the id of the package in the automationhub
class PipPackage(models.Model):
  name = models.CharField(max_length=100)
  version = models.CharField(max_length=100)
  automationhub_id = models.CharField(max_length=100)

# a definition of an ansible collection
# name: the name of the collection
# version: the version of the collection
# automationhub_id: the id of the collection in the automationhub
class AnsibleCollection(models.Model):
  name = models.CharField(max_length=100)
  version = models.CharField(max_length=100)
  automationhub_id = models.CharField(max_length=100)

# a definition of an ansible role
# name: the name of the role
# version: the version of the role
# automationhub_id: the id of the role in the automationhub
class AnsibleRole(models.Model):
  name = models.CharField(max_length=100)
  version = models.CharField(max_length=100)
  automationhub_id = models.CharField(max_length=100)

# a definition of a redhat repository
# name: the name of the repository
# version: the version of the repository
# automationhub_id: the id of the repository
class RedhatRepository(models.Model):
  name = models.CharField(max_length=100)
  version = models.CharField(max_length=100)
  automationhub_id = models.CharField(max_length=100)

# a definition of a redhat package
# name: the name of the package
# version: the version of the package
# automationhub_id: the id of the package

class RedhatPackage(models.Model):
  name = models.CharField(max_length=100)
  version = models.CharField(max_length=100)
  automationhub_id = models.CharField(max_length=100)
