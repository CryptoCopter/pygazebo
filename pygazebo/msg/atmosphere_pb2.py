# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: atmosphere.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='atmosphere.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x61tmosphere.proto\x12\x0bgazebo.msgs\"\xb2\x01\n\nAtmosphere\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\x1c.gazebo.msgs.Atmosphere.Type:\tADIABATIC\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12\x10\n\x08pressure\x18\x03 \x01(\x01\x12\x14\n\x0cmass_density\x18\x04 \x01(\x01\x12\x19\n\x11\x65nable_atmosphere\x18\x05 \x01(\x08\"\x15\n\x04Type\x12\r\n\tADIABATIC\x10\x01'
)



_ATMOSPHERE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='gazebo.msgs.Atmosphere.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADIABATIC', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=191,
  serialized_end=212,
)
_sym_db.RegisterEnumDescriptor(_ATMOSPHERE_TYPE)


_ATMOSPHERE = _descriptor.Descriptor(
  name='Atmosphere',
  full_name='gazebo.msgs.Atmosphere',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Atmosphere.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='gazebo.msgs.Atmosphere.temperature', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='gazebo.msgs.Atmosphere.pressure', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mass_density', full_name='gazebo.msgs.Atmosphere.mass_density', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_atmosphere', full_name='gazebo.msgs.Atmosphere.enable_atmosphere', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATMOSPHERE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=212,
)

_ATMOSPHERE.fields_by_name['type'].enum_type = _ATMOSPHERE_TYPE
_ATMOSPHERE_TYPE.containing_type = _ATMOSPHERE
DESCRIPTOR.message_types_by_name['Atmosphere'] = _ATMOSPHERE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Atmosphere = _reflection.GeneratedProtocolMessageType('Atmosphere', (_message.Message,), {
  'DESCRIPTOR' : _ATMOSPHERE,
  '__module__' : 'atmosphere_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Atmosphere)
  })
_sym_db.RegisterMessage(Atmosphere)


# @@protoc_insertion_point(module_scope)
