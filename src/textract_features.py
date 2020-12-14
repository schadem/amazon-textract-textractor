from enum import Enum


class TEXTRACT_FEATURES(Enum):
    TEXT = 1
    FORMS = 2
    TABLES = 3


TEXTRACT_ANALYZE_FEATURES = [TEXTRACT_FEATURES.FORMS, TEXTRACT_FEATURES.TABLES]

TEXTRACT_SUFFIXES = ['pdf', 'jpeg', 'jpg', 'png']
TEXTRACT_SYNC_SUFFIXES = ['jpeg', 'jpg', 'png']
TEXTRACT_ASYNC_ONLY_SUFFIXES = ['pdf']
