#!usr/bin/python3
# -*- coding: utf-8 -*-
"""Initial work."""
import boto3
import click


class IAM:
    def __init__(self, profile_name):
        self.session = boto3.Session(profile_name)

    def set_session(self, profile):
        self.p
    def nord_session(self):
        return self.session


