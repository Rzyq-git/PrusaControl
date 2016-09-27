#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import tempfile

from ConfigParser import ConfigParser, RawConfigParser


__author__ = 'Tibor Vavra'



class PrintingParameters(object):
    def __init__(self, controller):
        self.controller = controller


    def get_printers(self):
        return []

    def get_materials_for_printer(self, printer):
        return []

    def get_actual_settings(self):
        return []


class AppParameters(object):
    def __init__(self, controller, local_path=''):
        self.local_path = local_path
        self.controller = controller
        self.system_platform = platform.system()

        self.config = ConfigParser()

        if self.system_platform in ['Linux']:
            self.tmp_place = tempfile.gettempdir() + '/'
            self.config_path = os.path.expanduser("~/.prusacontrol")
            self.printing_parameters_file = os.path.expanduser("data/printing_parameters.json")
            self.printers_parameters_file = os.path.expanduser("data/printers.json")
            self.config.readfp(open('data/defaults.cfg'))
        elif self.system_platform in ['Darwin']:
            self.tmp_place = tempfile.gettempdir() + '/'
            self.config_path = os.path.expanduser("~/.prusacontrol")
            self.printing_parameters_file = os.path.expanduser("data/printing_parameters.json")
            self.printers_parameters_file = os.path.expanduser("data/printers.json")
            self.config.readfp(open('data/defaults.cfg'))
        elif self.system_platform in ['Windows']:
            self.tmp_place = tempfile.gettempdir() + '\\'
            self.config_path = os.path.expanduser("~\\prusacontrol.cfg")
            self.printing_parameters_file = os.path.expanduser("data\\printing_parameters.json")
            self.printers_parameters_file = os.path.expanduser("data\\printers.json")
            self.config.readfp(open('data\\defaults.cfg'))
        else:
            self.tmp_place = './'
            self.config_path = 'prusacontrol.cfg'
            self.printing_parameters_file = "data/printing_parameters.json"
            self.printers_parameters_file = os.path.expanduser("data/printers.json")
            self.config.readfp(open('data/defaults.cfg'))

        self.config.read(self.config_path)

        #read from version.txt
        with open("v.txt", 'r') as version_file:
            self.version_full = version_file.read()
            self.version = self.version_full.split('-')
            self.version = self.version[:2]
            self.version = "_".join(self.version)[1:]
