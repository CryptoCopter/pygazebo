# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spheregeom.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spheregeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10spheregeom.proto\x12\x0bgazebo.msgs\"\x1c\n\nSphereGeom\x12\x0e\n\x06radius\x18\x01 \x02(\x01'
)




_SPHEREGEOM = _descriptor.Descriptor(
  name='SphereGeom',
  full_name='gazebo.msgs.SphereGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius', full_name='gazebo.msgs.SphereGeom.radius', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=33,
  serialized_end=61,
)

DESCRIPTOR.message_types_by_name['SphereGeom'] = _SPHEREGEOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SphereGeom = _reflection.GeneratedProtocolMessageType('SphereGeom', (_message.Message,), {
  'DESCRIPTOR' : _SPHEREGEOM,
  '__module__' : 'spheregeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.SphereGeom)
  })
_sym_db.RegisterMessage(SphereGeom)


# @@protoc_insertion_point(module_scope)
