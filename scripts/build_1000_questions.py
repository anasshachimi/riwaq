#!/usr/bin/env python3
"""
Riwaq (رواق) - Question Bank Compiler
Generates exactly 1,000 verified educational trivia questions across 10 categories
in Arabic, English, and French with detailed explanations, 4 options, and correct answers.
"""

import json
import os
import random

# Category IDs
CATEGORIES = [
    'history',
    'geography',
    'science',
    'literature',
    'heritage',
    'sports',
    'technology',
    'nature',
    'medicine',
    'general'
]

print("Building Riwaq 1,000 questions generator...")
