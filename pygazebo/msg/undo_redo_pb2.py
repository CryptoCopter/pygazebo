# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: undo_redo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='undo_redo.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fundo_redo.proto\x12\x0bgazebo.msgs\"$\n\x08UndoRedo\x12\x0c\n\x04undo\x18\x01 \x02(\x08\x12\n\n\x02id\x18\x02 \x01(\r'
)




_UNDOREDO = _descriptor.Descriptor(
  name='UndoRedo',
  full_name='gazebo.msgs.UndoRedo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='undo', full_name='gazebo.msgs.UndoRedo.undo', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.UndoRedo.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=32,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['UndoRedo'] = _UNDOREDO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UndoRedo = _reflection.GeneratedProtocolMessageType('UndoRedo', (_message.Message,), {
  'DESCRIPTOR' : _UNDOREDO,
  '__module__' : 'undo_redo_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.UndoRedo)
  })
_sym_db.RegisterMessage(UndoRedo)


# @@protoc_insertion_point(module_scope)
