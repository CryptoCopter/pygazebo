# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collision.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pose_pb2 as pose__pb2
import geometry_pb2 as geometry__pb2
import surface_pb2 as surface__pb2
import visual_pb2 as visual__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collision.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63ollision.proto\x12\x0bgazebo.msgs\x1a\npose.proto\x1a\x0egeometry.proto\x1a\rsurface.proto\x1a\x0cvisual.proto\"\xe6\x01\n\tCollision\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x13\n\x0blaser_retro\x18\x03 \x01(\x01\x12\x14\n\x0cmax_contacts\x18\x04 \x01(\x01\x12\x1f\n\x04pose\x18\x05 \x01(\x0b\x32\x11.gazebo.msgs.Pose\x12\'\n\x08geometry\x18\x06 \x01(\x0b\x32\x15.gazebo.msgs.Geometry\x12%\n\x07surface\x18\x07 \x01(\x0b\x32\x14.gazebo.msgs.Surface\x12#\n\x06visual\x18\x08 \x03(\x0b\x32\x13.gazebo.msgs.Visual'
  ,
  dependencies=[pose__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,surface__pb2.DESCRIPTOR,visual__pb2.DESCRIPTOR,])




_COLLISION = _descriptor.Descriptor(
  name='Collision',
  full_name='gazebo.msgs.Collision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Collision.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Collision.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_retro', full_name='gazebo.msgs.Collision.laser_retro', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_contacts', full_name='gazebo.msgs.Collision.max_contacts', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.Collision.pose', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='gazebo.msgs.Collision.geometry', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='surface', full_name='gazebo.msgs.Collision.surface', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visual', full_name='gazebo.msgs.Collision.visual', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=90,
  serialized_end=320,
)

_COLLISION.fields_by_name['pose'].message_type = pose__pb2._POSE
_COLLISION.fields_by_name['geometry'].message_type = geometry__pb2._GEOMETRY
_COLLISION.fields_by_name['surface'].message_type = surface__pb2._SURFACE
_COLLISION.fields_by_name['visual'].message_type = visual__pb2._VISUAL
DESCRIPTOR.message_types_by_name['Collision'] = _COLLISION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Collision = _reflection.GeneratedProtocolMessageType('Collision', (_message.Message,), {
  'DESCRIPTOR' : _COLLISION,
  '__module__' : 'collision_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Collision)
  })
_sym_db.RegisterMessage(Collision)


# @@protoc_insertion_point(module_scope)
