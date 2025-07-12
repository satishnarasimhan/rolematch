# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 11:55:53 2025

@author: Satish Narasimhan
Run this file when you need to download certain sub packages of nltk. You will be displayed a prompt that you can then select
the required sub packages that need downloading
This is required as not all nltk subpackages download by default
"""
import nltk
import ssl

# Run this when you
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()