# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imu_sensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sensor_noise_pb2 as sensor__noise__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='imu_sensor.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10imu_sensor.proto\x12\x0bgazebo.msgs\x1a\x12sensor_noise.proto\"\xc2\x03\n\tIMUSensor\x12@\n\x10\x61ngular_velocity\x18\x01 \x01(\x0b\x32&.gazebo.msgs.IMUSensor.AngularVelocity\x12\x46\n\x13linear_acceleration\x18\x02 \x01(\x0b\x32).gazebo.msgs.IMUSensor.LinearAcceleration\x1a\x92\x01\n\x0f\x41ngularVelocity\x12)\n\x07x_noise\x18\x01 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x12)\n\x07y_noise\x18\x02 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x12)\n\x07z_noise\x18\x03 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x1a\x95\x01\n\x12LinearAcceleration\x12)\n\x07x_noise\x18\x01 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x12)\n\x07y_noise\x18\x02 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise\x12)\n\x07z_noise\x18\x03 \x01(\x0b\x32\x18.gazebo.msgs.SensorNoise'
  ,
  dependencies=[sensor__noise__pb2.DESCRIPTOR,])




_IMUSENSOR_ANGULARVELOCITY = _descriptor.Descriptor(
  name='AngularVelocity',
  full_name='gazebo.msgs.IMUSensor.AngularVelocity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_noise', full_name='gazebo.msgs.IMUSensor.AngularVelocity.x_noise', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y_noise', full_name='gazebo.msgs.IMUSensor.AngularVelocity.y_noise', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z_noise', full_name='gazebo.msgs.IMUSensor.AngularVelocity.z_noise', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=206,
  serialized_end=352,
)

_IMUSENSOR_LINEARACCELERATION = _descriptor.Descriptor(
  name='LinearAcceleration',
  full_name='gazebo.msgs.IMUSensor.LinearAcceleration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_noise', full_name='gazebo.msgs.IMUSensor.LinearAcceleration.x_noise', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y_noise', full_name='gazebo.msgs.IMUSensor.LinearAcceleration.y_noise', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z_noise', full_name='gazebo.msgs.IMUSensor.LinearAcceleration.z_noise', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=355,
  serialized_end=504,
)

_IMUSENSOR = _descriptor.Descriptor(
  name='IMUSensor',
  full_name='gazebo.msgs.IMUSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='gazebo.msgs.IMUSensor.angular_velocity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='gazebo.msgs.IMUSensor.linear_acceleration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_IMUSENSOR_ANGULARVELOCITY, _IMUSENSOR_LINEARACCELERATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=504,
)

_IMUSENSOR_ANGULARVELOCITY.fields_by_name['x_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_ANGULARVELOCITY.fields_by_name['y_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_ANGULARVELOCITY.fields_by_name['z_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_ANGULARVELOCITY.containing_type = _IMUSENSOR
_IMUSENSOR_LINEARACCELERATION.fields_by_name['x_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_LINEARACCELERATION.fields_by_name['y_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_LINEARACCELERATION.fields_by_name['z_noise'].message_type = sensor__noise__pb2._SENSORNOISE
_IMUSENSOR_LINEARACCELERATION.containing_type = _IMUSENSOR
_IMUSENSOR.fields_by_name['angular_velocity'].message_type = _IMUSENSOR_ANGULARVELOCITY
_IMUSENSOR.fields_by_name['linear_acceleration'].message_type = _IMUSENSOR_LINEARACCELERATION
DESCRIPTOR.message_types_by_name['IMUSensor'] = _IMUSENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IMUSensor = _reflection.GeneratedProtocolMessageType('IMUSensor', (_message.Message,), {

  'AngularVelocity' : _reflection.GeneratedProtocolMessageType('AngularVelocity', (_message.Message,), {
    'DESCRIPTOR' : _IMUSENSOR_ANGULARVELOCITY,
    '__module__' : 'imu_sensor_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.IMUSensor.AngularVelocity)
    })
  ,

  'LinearAcceleration' : _reflection.GeneratedProtocolMessageType('LinearAcceleration', (_message.Message,), {
    'DESCRIPTOR' : _IMUSENSOR_LINEARACCELERATION,
    '__module__' : 'imu_sensor_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.IMUSensor.LinearAcceleration)
    })
  ,
  'DESCRIPTOR' : _IMUSENSOR,
  '__module__' : 'imu_sensor_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.IMUSensor)
  })
_sym_db.RegisterMessage(IMUSensor)
_sym_db.RegisterMessage(IMUSensor.AngularVelocity)
_sym_db.RegisterMessage(IMUSensor.LinearAcceleration)


# @@protoc_insertion_point(module_scope)
