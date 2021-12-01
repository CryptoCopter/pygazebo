# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server_control.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14server_control.proto\x12\x0bgazebo.msgs\"\x98\x01\n\rServerControl\x12\x17\n\x0fsave_world_name\x18\x01 \x01(\t\x12\x15\n\rsave_filename\x18\x02 \x01(\t\x12\x15\n\ropen_filename\x18\x03 \x01(\t\x12\x11\n\tnew_world\x18\x04 \x01(\x08\x12\x0c\n\x04stop\x18\x05 \x01(\x08\x12\r\n\x05\x63lone\x18\x06 \x01(\x08\x12\x10\n\x08new_port\x18\x07 \x01(\r'
)




_SERVERCONTROL = _descriptor.Descriptor(
  name='ServerControl',
  full_name='gazebo.msgs.ServerControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='save_world_name', full_name='gazebo.msgs.ServerControl.save_world_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='save_filename', full_name='gazebo.msgs.ServerControl.save_filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open_filename', full_name='gazebo.msgs.ServerControl.open_filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_world', full_name='gazebo.msgs.ServerControl.new_world', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='gazebo.msgs.ServerControl.stop', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clone', full_name='gazebo.msgs.ServerControl.clone', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_port', full_name='gazebo.msgs.ServerControl.new_port', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=38,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['ServerControl'] = _SERVERCONTROL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerControl = _reflection.GeneratedProtocolMessageType('ServerControl', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCONTROL,
  '__module__' : 'server_control_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.ServerControl)
  })
_sym_db.RegisterMessage(ServerControl)


# @@protoc_insertion_point(module_scope)
