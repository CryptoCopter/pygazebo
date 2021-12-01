# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: publishers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import publish_pb2 as publish__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='publishers.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10publishers.proto\x12\x0bgazebo.msgs\x1a\rpublish.proto\"5\n\nPublishers\x12\'\n\tpublisher\x18\x01 \x03(\x0b\x32\x14.gazebo.msgs.Publish'
  ,
  dependencies=[publish__pb2.DESCRIPTOR,])




_PUBLISHERS = _descriptor.Descriptor(
  name='Publishers',
  full_name='gazebo.msgs.Publishers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='publisher', full_name='gazebo.msgs.Publishers.publisher', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=48,
  serialized_end=101,
)

_PUBLISHERS.fields_by_name['publisher'].message_type = publish__pb2._PUBLISH
DESCRIPTOR.message_types_by_name['Publishers'] = _PUBLISHERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Publishers = _reflection.GeneratedProtocolMessageType('Publishers', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHERS,
  '__module__' : 'publishers_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Publishers)
  })
_sym_db.RegisterMessage(Publishers)


# @@protoc_insertion_point(module_scope)
