__version__ = '0.1.0b'
__author__ = 'LeGDieS'
__email__ = '94766942+Legdies@users.noreply.github.com'
__license__ = 'MIT'
__doc__ = '''
Module was developed as a temporal wrapper for new rule34.gg API and will be reworked later. 
It will provide basic functionality
until Autor [SyperAlexKomp] will create better API solution.

Has components:
    --ListPosts
    
Future changes:
    --FindPostByID
    --UserAPIKey
    

'''
from . import ListPosts
__all__ : tuple[str, ...] = ("ListPosts",
                              )
