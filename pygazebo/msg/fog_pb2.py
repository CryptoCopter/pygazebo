# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import color_pb2 as color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fog.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tfog.proto\x12\x0bgazebo.msgs\x1a\x0b\x63olor.proto\"\xc1\x01\n\x03\x46og\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.gazebo.msgs.Fog.FogType\x12!\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12\x0f\n\x07\x64\x65nsity\x18\x03 \x01(\x02\x12\r\n\x05start\x18\x04 \x01(\x02\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x02\"B\n\x07\x46ogType\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06LINEAR\x10\x02\x12\x0f\n\x0b\x45XPONENTIAL\x10\x03\x12\x10\n\x0c\x45XPONENTIAL2\x10\x04'
  ,
  dependencies=[color__pb2.DESCRIPTOR,])



_FOG_FOGTYPE = _descriptor.EnumDescriptor(
  name='FogType',
  full_name='gazebo.msgs.Fog.FogType',
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
      name='LINEAR', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPONENTIAL', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPONENTIAL2', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_FOG_FOGTYPE)


_FOG = _descriptor.Descriptor(
  name='Fog',
  full_name='gazebo.msgs.Fog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Fog.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='gazebo.msgs.Fog.color', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='density', full_name='gazebo.msgs.Fog.density', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='gazebo.msgs.Fog.start', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='gazebo.msgs.Fog.end', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FOG_FOGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=233,
)

_FOG.fields_by_name['type'].enum_type = _FOG_FOGTYPE
_FOG.fields_by_name['color'].message_type = color__pb2._COLOR
_FOG_FOGTYPE.containing_type = _FOG
DESCRIPTOR.message_types_by_name['Fog'] = _FOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fog = _reflection.GeneratedProtocolMessageType('Fog', (_message.Message,), {
  'DESCRIPTOR' : _FOG,
  '__module__' : 'fog_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Fog)
  })
_sym_db.RegisterMessage(Fog)


# @@protoc_insertion_point(module_scope)
