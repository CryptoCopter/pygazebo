# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magnetometer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import time_pb2 as time__pb2
import vector3d_pb2 as vector3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='magnetometer.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12magnetometer.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\x1a\x0evector3d.proto\"[\n\x0cMagnetometer\x12\x1f\n\x04time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12*\n\x0b\x66ield_tesla\x18\x02 \x02(\x0b\x32\x15.gazebo.msgs.Vector3d'
  ,
  dependencies=[time__pb2.DESCRIPTOR,vector3d__pb2.DESCRIPTOR,])




_MAGNETOMETER = _descriptor.Descriptor(
  name='Magnetometer',
  full_name='gazebo.msgs.Magnetometer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.Magnetometer.time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_tesla', full_name='gazebo.msgs.Magnetometer.field_tesla', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=63,
  serialized_end=154,
)

_MAGNETOMETER.fields_by_name['time'].message_type = time__pb2._TIME
_MAGNETOMETER.fields_by_name['field_tesla'].message_type = vector3d__pb2._VECTOR3D
DESCRIPTOR.message_types_by_name['Magnetometer'] = _MAGNETOMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Magnetometer = _reflection.GeneratedProtocolMessageType('Magnetometer', (_message.Message,), {
  'DESCRIPTOR' : _MAGNETOMETER,
  '__module__' : 'magnetometer_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Magnetometer)
  })
_sym_db.RegisterMessage(Magnetometer)


# @@protoc_insertion_point(module_scope)
