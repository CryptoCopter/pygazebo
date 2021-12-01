# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose_stamped.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import time_pb2 as time__pb2
import pose_pb2 as pose__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose_stamped.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12pose_stamped.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\x1a\npose.proto\"O\n\x0bPoseStamped\x12\x1f\n\x04time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12\x1f\n\x04pose\x18\x02 \x02(\x0b\x32\x11.gazebo.msgs.Pose'
  ,
  dependencies=[time__pb2.DESCRIPTOR,pose__pb2.DESCRIPTOR,])




_POSESTAMPED = _descriptor.Descriptor(
  name='PoseStamped',
  full_name='gazebo.msgs.PoseStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.PoseStamped.time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.PoseStamped.pose', index=1,
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
  serialized_start=59,
  serialized_end=138,
)

_POSESTAMPED.fields_by_name['time'].message_type = time__pb2._TIME
_POSESTAMPED.fields_by_name['pose'].message_type = pose__pb2._POSE
DESCRIPTOR.message_types_by_name['PoseStamped'] = _POSESTAMPED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseStamped = _reflection.GeneratedProtocolMessageType('PoseStamped', (_message.Message,), {
  'DESCRIPTOR' : _POSESTAMPED,
  '__module__' : 'pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PoseStamped)
  })
_sym_db.RegisterMessage(PoseStamped)


# @@protoc_insertion_point(module_scope)
