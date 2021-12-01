# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gps_sensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sensor_noise_pb2 as sensor__noise__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gps_sensor.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10gps_sensor.proto\x12\x0bgazebo.msgs\x1a\x12sensor_noise.proto\"\xe0\x01\n\tGPSSensor\x12\x30\n\x08position\x18\x01 \x01(\x0b\x32\x1e.gazebo.msgs.GPSSensor.Sensing\x12\x30\n\x08velocity\x18\x02 \x01(\x0b\x32\x1e.gazebo.msgs.GPSSensor.Sensing\x1ao\n\x07Sensing\x12\x32\n\x10horizontal_noise\x18\x01 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x12\x30\n\x0evertical_noise\x18\x02 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise'
  ,
  dependencies=[sensor__noise__pb2.DESCRIPTOR,])




_GPSSENSOR_SENSING = _descriptor.Descriptor(
  name='Sensing',
  full_name='gazebo.msgs.GPSSensor.Sensing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='horizontal_noise', full_name='gazebo.msgs.GPSSensor.Sensing.horizontal_noise', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_noise', full_name='gazebo.msgs.GPSSensor.Sensing.vertical_noise', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=167,
  serialized_end=278,
)

_GPSSENSOR = _descriptor.Descriptor(
  name='GPSSensor',
  full_name='gazebo.msgs.GPSSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='gazebo.msgs.GPSSensor.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='gazebo.msgs.GPSSensor.velocity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GPSSENSOR_SENSING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=278,
)

_GPSSENSOR_SENSING.fields_by_name['horizontal_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_GPSSENSOR_SENSING.fields_by_name['vertical_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_GPSSENSOR_SENSING.containing_type = _GPSSENSOR
_GPSSENSOR.fields_by_name['position'].message_type = _GPSSENSOR_SENSING
_GPSSENSOR.fields_by_name['velocity'].message_type = _GPSSENSOR_SENSING
DESCRIPTOR.message_types_by_name['GPSSensor'] = _GPSSENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GPSSensor = _reflection.GeneratedProtocolMessageType('GPSSensor', (_message.Message,), {

  'Sensing' : _reflection.GeneratedProtocolMessageType('Sensing', (_message.Message,), {
    'DESCRIPTOR' : _GPSSENSOR_SENSING,
    '__module__' : 'gps_sensor_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.GPSSensor.Sensing)
    })
  ,
  'DESCRIPTOR' : _GPSSENSOR,
  '__module__' : 'gps_sensor_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.GPSSensor)
  })
_sym_db.RegisterMessage(GPSSensor)
_sym_db.RegisterMessage(GPSSensor.Sensing)


# @@protoc_insertion_point(module_scope)
