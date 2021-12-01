# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raysensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='raysensor.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fraysensor.proto\x12\x0bgazebo.msgs\"\xc7\x02\n\tRaySensor\x12\x14\n\x0c\x64isplay_scan\x18\x01 \x01(\x08\x12\x1a\n\x12horizontal_samples\x18\x02 \x01(\x05\x12\x1d\n\x15horizontal_resolution\x18\x03 \x01(\x01\x12\x1c\n\x14horizontal_min_angle\x18\x04 \x01(\x01\x12\x1c\n\x14horizontal_max_angle\x18\x05 \x01(\x01\x12\x18\n\x10vertical_samples\x18\x06 \x01(\x05\x12\x1b\n\x13vertical_resolution\x18\x07 \x01(\x01\x12\x1a\n\x12vertical_min_angle\x18\x08 \x01(\x01\x12\x1a\n\x12vertical_max_angle\x18\t \x01(\x01\x12\x11\n\trange_min\x18\n \x01(\x01\x12\x11\n\trange_max\x18\x0b \x01(\x01\x12\x18\n\x10range_resolution\x18\x0c \x01(\x01'
)




_RAYSENSOR = _descriptor.Descriptor(
  name='RaySensor',
  full_name='gazebo.msgs.RaySensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_scan', full_name='gazebo.msgs.RaySensor.display_scan', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_samples', full_name='gazebo.msgs.RaySensor.horizontal_samples', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_resolution', full_name='gazebo.msgs.RaySensor.horizontal_resolution', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_min_angle', full_name='gazebo.msgs.RaySensor.horizontal_min_angle', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_max_angle', full_name='gazebo.msgs.RaySensor.horizontal_max_angle', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_samples', full_name='gazebo.msgs.RaySensor.vertical_samples', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_resolution', full_name='gazebo.msgs.RaySensor.vertical_resolution', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_min_angle', full_name='gazebo.msgs.RaySensor.vertical_min_angle', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_max_angle', full_name='gazebo.msgs.RaySensor.vertical_max_angle', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='gazebo.msgs.RaySensor.range_min', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='gazebo.msgs.RaySensor.range_max', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_resolution', full_name='gazebo.msgs.RaySensor.range_resolution', index=11,
      number=12, type=1, cpp_type=5, label=1,
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
  serialized_end=360,
)

DESCRIPTOR.message_types_by_name['RaySensor'] = _RAYSENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaySensor = _reflection.GeneratedProtocolMessageType('RaySensor', (_message.Message,), {
  'DESCRIPTOR' : _RAYSENSOR,
  '__module__' : 'raysensor_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.RaySensor)
  })
_sym_db.RegisterMessage(RaySensor)


# @@protoc_insertion_point(module_scope)
