# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polylinegeom.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import vector2d_pb2 as vector2d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='polylinegeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12polylinegeom.proto\x12\x0bgazebo.msgs\x1a\x0evector2d.proto\"@\n\x08Polyline\x12\x0e\n\x06height\x18\x01 \x02(\x01\x12$\n\x05point\x18\x02 \x03(\x0b\x32\x15.gazebo.msgs.Vector2d'
  ,
  dependencies=[vector2d__pb2.DESCRIPTOR,])




_POLYLINE = _descriptor.Descriptor(
  name='Polyline',
  full_name='gazebo.msgs.Polyline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='gazebo.msgs.Polyline.height', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point', full_name='gazebo.msgs.Polyline.point', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=51,
  serialized_end=115,
)

_POLYLINE.fields_by_name['point'].message_type = vector2d__pb2._VECTOR2D
DESCRIPTOR.message_types_by_name['Polyline'] = _POLYLINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINE,
  '__module__' : 'polylinegeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Polyline)
  })
_sym_db.RegisterMessage(Polyline)


# @@protoc_insertion_point(module_scope)
