# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: laserscan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pose_pb2 as pose__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='laserscan.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0flaserscan.proto\x12\x0bgazebo.msgs\x1a\npose.proto\"\xc2\x02\n\tLaserScan\x12\r\n\x05\x66rame\x18\x01 \x02(\t\x12%\n\nworld_pose\x18\x02 \x02(\x0b\x32\x11.gazebo.msgs.Pose\x12\x11\n\tangle_min\x18\x03 \x02(\x01\x12\x11\n\tangle_max\x18\x04 \x02(\x01\x12\x12\n\nangle_step\x18\x05 \x02(\x01\x12\x11\n\trange_min\x18\x06 \x02(\x01\x12\x11\n\trange_max\x18\x07 \x02(\x01\x12\r\n\x05\x63ount\x18\x08 \x02(\r\x12\x1a\n\x12vertical_angle_min\x18\t \x01(\x01\x12\x1a\n\x12vertical_angle_max\x18\n \x01(\x01\x12\x1b\n\x13vertical_angle_step\x18\x0b \x01(\x01\x12\x16\n\x0evertical_count\x18\x0c \x01(\r\x12\x0e\n\x06ranges\x18\r \x03(\x01\x12\x13\n\x0bintensities\x18\x0e \x03(\x01'
  ,
  dependencies=[pose__pb2.DESCRIPTOR,])




_LASERSCAN = _descriptor.Descriptor(
  name='LaserScan',
  full_name='gazebo.msgs.LaserScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='gazebo.msgs.LaserScan.frame', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='world_pose', full_name='gazebo.msgs.LaserScan.world_pose', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_min', full_name='gazebo.msgs.LaserScan.angle_min', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_max', full_name='gazebo.msgs.LaserScan.angle_max', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_step', full_name='gazebo.msgs.LaserScan.angle_step', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='gazebo.msgs.LaserScan.range_min', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='gazebo.msgs.LaserScan.range_max', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='gazebo.msgs.LaserScan.count', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_angle_min', full_name='gazebo.msgs.LaserScan.vertical_angle_min', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_angle_max', full_name='gazebo.msgs.LaserScan.vertical_angle_max', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_angle_step', full_name='gazebo.msgs.LaserScan.vertical_angle_step', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_count', full_name='gazebo.msgs.LaserScan.vertical_count', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='gazebo.msgs.LaserScan.ranges', index=12,
      number=13, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intensities', full_name='gazebo.msgs.LaserScan.intensities', index=13,
      number=14, type=1, cpp_type=5, label=3,
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
  serialized_start=45,
  serialized_end=367,
)

_LASERSCAN.fields_by_name['world_pose'].message_type = pose__pb2._POSE
DESCRIPTOR.message_types_by_name['LaserScan'] = _LASERSCAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LaserScan = _reflection.GeneratedProtocolMessageType('LaserScan', (_message.Message,), {
  'DESCRIPTOR' : _LASERSCAN,
  '__module__' : 'laserscan_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.LaserScan)
  })
_sym_db.RegisterMessage(LaserScan)


# @@protoc_insertion_point(module_scope)
