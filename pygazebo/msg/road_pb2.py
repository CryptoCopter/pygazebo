# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: road.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import vector3d_pb2 as vector3d__pb2
import material_pb2 as material__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='road.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nroad.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\x1a\x0ematerial.proto\"r\n\x04Road\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05width\x18\x02 \x02(\x01\x12$\n\x05point\x18\x03 \x03(\x0b\x32\x15.gazebo.msgs.Vector3d\x12\'\n\x08material\x18\x04 \x01(\x0b\x32\x15.gazebo.msgs.Material'
  ,
  dependencies=[vector3d__pb2.DESCRIPTOR,material__pb2.DESCRIPTOR,])




_ROAD = _descriptor.Descriptor(
  name='Road',
  full_name='gazebo.msgs.Road',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Road.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='gazebo.msgs.Road.width', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point', full_name='gazebo.msgs.Road.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='material', full_name='gazebo.msgs.Road.material', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=59,
  serialized_end=173,
)

_ROAD.fields_by_name['point'].message_type = vector3d__pb2._VECTOR3D
_ROAD.fields_by_name['material'].message_type = material__pb2._MATERIAL
DESCRIPTOR.message_types_by_name['Road'] = _ROAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), {
  'DESCRIPTOR' : _ROAD,
  '__module__' : 'road_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Road)
  })
_sym_db.RegisterMessage(Road)


# @@protoc_insertion_point(module_scope)
