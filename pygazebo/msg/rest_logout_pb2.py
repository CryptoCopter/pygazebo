# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rest_logout.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rest_logout.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11rest_logout.proto\x12\x0bgazebo.msgs\"%\n\nRestLogout\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03url\x18\x02 \x01(\t'
)




_RESTLOGOUT = _descriptor.Descriptor(
  name='RestLogout',
  full_name='gazebo.msgs.RestLogout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.RestLogout.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='gazebo.msgs.RestLogout.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['RestLogout'] = _RESTLOGOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RestLogout = _reflection.GeneratedProtocolMessageType('RestLogout', (_message.Message,), {
  'DESCRIPTOR' : _RESTLOGOUT,
  '__module__' : 'rest_logout_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.RestLogout)
  })
_sym_db.RegisterMessage(RestLogout)


# @@protoc_insertion_point(module_scope)
