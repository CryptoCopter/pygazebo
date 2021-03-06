# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: any.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import color_pb2 as color__pb2
import pose_pb2 as pose__pb2
import quaternion_pb2 as quaternion__pb2
import time_pb2 as time__pb2
import vector3d_pb2 as vector3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='any.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tany.proto\x12\x0bgazebo.msgs\x1a\x0b\x63olor.proto\x1a\npose.proto\x1a\x10quaternion.proto\x1a\ntime.proto\x1a\x0evector3d.proto\"\xeb\x03\n\x03\x41ny\x12.\n\x04type\x18\x01 \x02(\x0e\x32\x1a.gazebo.msgs.Any.ValueType:\x04NONE\x12\x14\n\x0c\x64ouble_value\x18\x02 \x01(\x01\x12\x11\n\tint_value\x18\x03 \x01(\x05\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12\x12\n\nbool_value\x18\x05 \x01(\x08\x12-\n\x0evector3d_value\x18\x06 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12\'\n\x0b\x63olor_value\x18\x07 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12\'\n\x0cpose3d_value\x18\x08 \x01(\x0b\x32\x11.gazebo.msgs.Pose\x12\x31\n\x10quaternion_value\x18\t \x01(\x0b\x32\x17.gazebo.msgs.Quaternion\x12%\n\ntime_value\x18\n \x01(\x0b\x32\x11.gazebo.msgs.Time\"\x85\x01\n\tValueType\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\t\n\x05INT32\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x0b\n\x07\x42OOLEAN\x10\x05\x12\x0c\n\x08VECTOR3D\x10\x06\x12\t\n\x05\x43OLOR\x10\x07\x12\n\n\x06POSE3D\x10\x08\x12\x0f\n\x0bQUATERNIOND\x10\t\x12\x08\n\x04TIME\x10\n'
  ,
  dependencies=[color__pb2.DESCRIPTOR,pose__pb2.DESCRIPTOR,quaternion__pb2.DESCRIPTOR,time__pb2.DESCRIPTOR,vector3d__pb2.DESCRIPTOR,])



_ANY_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='gazebo.msgs.Any.ValueType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VECTOR3D', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLOR', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POSE3D', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUATERNIOND', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=456,
  serialized_end=589,
)
_sym_db.RegisterEnumDescriptor(_ANY_VALUETYPE)


_ANY = _descriptor.Descriptor(
  name='Any',
  full_name='gazebo.msgs.Any',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Any.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='gazebo.msgs.Any.double_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='gazebo.msgs.Any.int_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='gazebo.msgs.Any.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='gazebo.msgs.Any.bool_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vector3d_value', full_name='gazebo.msgs.Any.vector3d_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color_value', full_name='gazebo.msgs.Any.color_value', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose3d_value', full_name='gazebo.msgs.Any.pose3d_value', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quaternion_value', full_name='gazebo.msgs.Any.quaternion_value', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_value', full_name='gazebo.msgs.Any.time_value', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANY_VALUETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=589,
)

_ANY.fields_by_name['type'].enum_type = _ANY_VALUETYPE
_ANY.fields_by_name['vector3d_value'].message_type = vector3d__pb2._VECTOR3D
_ANY.fields_by_name['color_value'].message_type = color__pb2._COLOR
_ANY.fields_by_name['pose3d_value'].message_type = pose__pb2._POSE
_ANY.fields_by_name['quaternion_value'].message_type = quaternion__pb2._QUATERNION
_ANY.fields_by_name['time_value'].message_type = time__pb2._TIME
_ANY_VALUETYPE.containing_type = _ANY
DESCRIPTOR.message_types_by_name['Any'] = _ANY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Any = _reflection.GeneratedProtocolMessageType('Any', (_message.Message,), {
  'DESCRIPTOR' : _ANY,
  '__module__' : 'any_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Any)
  })
_sym_db.RegisterMessage(Any)


# @@protoc_insertion_point(module_scope)
