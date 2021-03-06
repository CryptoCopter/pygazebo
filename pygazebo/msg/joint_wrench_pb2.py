# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: joint_wrench.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import wrench_pb2 as wrench__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='joint_wrench.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12joint_wrench.proto\x12\x0bgazebo.msgs\x1a\x0cwrench.proto\"\xb5\x01\n\x0bJointWrench\x12\x13\n\x0b\x62ody_1_name\x18\x01 \x02(\t\x12\x11\n\tbody_1_id\x18\x02 \x02(\r\x12\x13\n\x0b\x62ody_2_name\x18\x03 \x02(\t\x12\x11\n\tbody_2_id\x18\x04 \x02(\r\x12*\n\rbody_1_wrench\x18\x05 \x02(\x0b\x32\x13.gazebo.msgs.Wrench\x12*\n\rbody_2_wrench\x18\x06 \x02(\x0b\x32\x13.gazebo.msgs.Wrench'
  ,
  dependencies=[wrench__pb2.DESCRIPTOR,])




_JOINTWRENCH = _descriptor.Descriptor(
  name='JointWrench',
  full_name='gazebo.msgs.JointWrench',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='body_1_name', full_name='gazebo.msgs.JointWrench.body_1_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_1_id', full_name='gazebo.msgs.JointWrench.body_1_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_2_name', full_name='gazebo.msgs.JointWrench.body_2_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_2_id', full_name='gazebo.msgs.JointWrench.body_2_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_1_wrench', full_name='gazebo.msgs.JointWrench.body_1_wrench', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_2_wrench', full_name='gazebo.msgs.JointWrench.body_2_wrench', index=5,
      number=6, type=11, cpp_type=10, label=2,
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
  serialized_start=50,
  serialized_end=231,
)

_JOINTWRENCH.fields_by_name['body_1_wrench'].message_type = wrench__pb2._WRENCH
_JOINTWRENCH.fields_by_name['body_2_wrench'].message_type = wrench__pb2._WRENCH
DESCRIPTOR.message_types_by_name['JointWrench'] = _JOINTWRENCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JointWrench = _reflection.GeneratedProtocolMessageType('JointWrench', (_message.Message,), {
  'DESCRIPTOR' : _JOINTWRENCH,
  '__module__' : 'joint_wrench_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.JointWrench)
  })
_sym_db.RegisterMessage(JointWrench)


# @@protoc_insertion_point(module_scope)
