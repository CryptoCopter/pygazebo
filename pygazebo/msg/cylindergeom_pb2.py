# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cylindergeom.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cylindergeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63ylindergeom.proto\x12\x0bgazebo.msgs\".\n\x0c\x43ylinderGeom\x12\x0e\n\x06radius\x18\x01 \x02(\x01\x12\x0e\n\x06length\x18\x02 \x02(\x01'
)




_CYLINDERGEOM = _descriptor.Descriptor(
  name='CylinderGeom',
  full_name='gazebo.msgs.CylinderGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius', full_name='gazebo.msgs.CylinderGeom.radius', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='gazebo.msgs.CylinderGeom.length', index=1,
      number=2, type=1, cpp_type=5, label=2,
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
  serialized_start=35,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['CylinderGeom'] = _CYLINDERGEOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CylinderGeom = _reflection.GeneratedProtocolMessageType('CylinderGeom', (_message.Message,), {
  'DESCRIPTOR' : _CYLINDERGEOM,
  '__module__' : 'cylindergeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.CylinderGeom)
  })
_sym_db.RegisterMessage(CylinderGeom)


# @@protoc_insertion_point(module_scope)
