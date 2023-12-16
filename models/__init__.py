#!/usr/bin/python3
"""
package initialization model
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
