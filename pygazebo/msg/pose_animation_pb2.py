# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose_animation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pose_pb2 as pose__pb2
import time_pb2 as time__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose_animation.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14pose_animation.proto\x12\x0bgazebo.msgs\x1a\npose.proto\x1a\ntime.proto\"w\n\rPoseAnimation\x12\x12\n\nmodel_name\x18\x01 \x02(\t\x12\x10\n\x08model_id\x18\x02 \x01(\r\x12\x1f\n\x04pose\x18\x03 \x03(\x0b\x32\x11.gazebo.msgs.Pose\x12\x1f\n\x04time\x18\x04 \x03(\x0b\x32\x11.gazebo.msgs.Time'
  ,
  dependencies=[pose__pb2.DESCRIPTOR,time__pb2.DESCRIPTOR,])




_POSEANIMATION = _descriptor.Descriptor(
  name='PoseAnimation',
  full_name='gazebo.msgs.PoseAnimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='gazebo.msgs.PoseAnimation.model_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='gazebo.msgs.PoseAnimation.model_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.PoseAnimation.pose', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.PoseAnimation.time', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=61,
  serialized_end=180,
)

_POSEANIMATION.fields_by_name['pose'].message_type = pose__pb2._POSE
_POSEANIMATION.fields_by_name['time'].message_type = time__pb2._TIME
DESCRIPTOR.message_types_by_name['PoseAnimation'] = _POSEANIMATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseAnimation = _reflection.GeneratedProtocolMessageType('PoseAnimation', (_message.Message,), {
  'DESCRIPTOR' : _POSEANIMATION,
  '__module__' : 'pose_animation_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PoseAnimation)
  })
_sym_db.RegisterMessage(PoseAnimation)


# @@protoc_insertion_point(module_scope)
