from django.db import models


class Project(models.Model):
    repo_owner = models.CharField()
    repo_name = models.CharField()


class DataPoint(models.Model):
    P = models.ForeignKey(Project)
    created = models.DateTimeField(auto_add_now=True)
    size = models.IntegerField(default=0)
    stargazers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    open_issues_count = models.IntegerField(default=0)
    fork = models.IntegerField(default=0)


###################### Apscheduler Stuff #######################

#XXX: Not sure if this is the right place to start the scheduler
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

import requests


def fetch_repo_stats(rep):
    api_repo_url = 'https://api.github.com/repos/' + repo_owner + '/' + repo_name
    r = requests.get(api_repo_url)
    data = r.json()
    #XXX Extract stats from data and create a datapoint for them

################# Triggers and Callbacks ###################
############################################################

from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=Project)
def update_userlimitedcredits(sender, instance, **kwargs):
    """
    To update value of net limitedcredits for MUser when a new LimitedCreditPack
    is added for him.
    """
    if kwargs['created']:
        project = instance
        #XXX: Add a job that fetches repo stats from api to the scheduler
        # Store the repo stats
    else:
        pass
