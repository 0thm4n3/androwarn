#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Androwarn.
#
# Copyright (C) 2012, Thomas Debize <tdebize at mail.com>
# All rights reserved.
#
# Androwarn is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androwarn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androwarn.  If not, see <http://www.gnu.org/licenses/>.

# Global imports
import os, re, logging

# Androguard imports
from androguard.core.analysis import analysis
from androguard.core.bytecodes.apk import *
from xml.dom import minidom

# Androwarn modules import
from androwarn.core.core import *
from androwarn.util.util import *

# Constants 
ERROR_INDEX_NOT_FOUND = -2

REQUEST_TIMEOUT = 4
ERROR_APP_DESC_NOT_FOUND = 'N/A'

CONNECTION_DISABLED = 0
CONNECTION_ENABLED = 1

# Logguer
log = logging.getLogger('log')

def detect_ContactAccess_lookup(x) :
	"""
		@param x : a VMAnalysis instance
		
		@rtype : a list of formatted strings
	"""
	formatted_str = []
	
	detector_1 = search_field(x, "Landroid/provider/ContactsContract$CommonDataKinds$Phone;")
		
	detectors = [detector_1]
	
	if detectors :
		local_formatted_str = 'This application reads/edits contact data'
		formatted_str.append(local_formatted_str)
		
		for res in detectors :
			if res :
				try :
					log_result_path_information(res, "Contact access", "field")
				except :
					log.warn("Detector result '%s' is not a Path instance" % res)
					
	return formatted_str


def detect_Telephony_SMS_read(x) :
	"""
		@param x : a VMAnalysis instance
		
		@rtype : a list of formatted strings
	"""
	formatted_str = []
	
	detector_1 = search_string(x, "content://sms/inbox")
		
	detectors = [detector_1]
	
	if detectors :
		local_formatted_str = 'This application reads the SMS inbox'
		formatted_str.append(local_formatted_str)
		
		for res in detectors :
			if res :
				try :
					log_result_path_information(res, "SMS Inbox", "string")
				except :
					log.warn("Detector result '%s' is not a Path instance" % res) 
		
	return formatted_str
