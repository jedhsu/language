from __future__ import annotations

# ugh this is ahrd

# class Term:
#     __metaclass__ = Form

# class Form(type):
#     @classmethod
#     def __prepare__(mcls, *args, **kwargs):
#         dct = dict()

#         dct["__bases__"] = (Term, type, object)
#         dct["__mro__"] = (Form, Term, type, object)

#         return dct

#     def __subclasshook__(self):
