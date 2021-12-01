# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: link.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import inertial_pb2 as inertial__pb2
import collision_pb2 as collision__pb2
import light_pb2 as light__pb2
import visual_pb2 as visual__pb2
import sensor_pb2 as sensor__pb2
import projector_pb2 as projector__pb2
import pose_pb2 as pose__pb2
import battery_pb2 as battery__pb2
import density_pb2 as density__pb2
import vector3d_pb2 as vector3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='link.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nlink.proto\x12\x0bgazebo.msgs\x1a\x0einertial.proto\x1a\x0f\x63ollision.proto\x1a\x0blight.proto\x1a\x0cvisual.proto\x1a\x0csensor.proto\x1a\x0fprojector.proto\x1a\npose.proto\x1a\rbattery.proto\x1a\rdensity.proto\x1a\x0evector3d.proto\"\x93\x04\n\x04Link\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0cself_collide\x18\x03 \x01(\x08\x12\x0f\n\x07gravity\x18\x04 \x01(\x08\x12\x11\n\tkinematic\x18\x05 \x01(\x08\x12\x0f\n\x07\x65nabled\x18\x06 \x01(\x08\x12%\n\x07\x64\x65nsity\x18\x07 \x01(\x0b\x32\x14.gazebo.msgs.Density\x12\'\n\x08inertial\x18\x08 \x01(\x0b\x32\x15.gazebo.msgs.Inertial\x12\x1f\n\x04pose\x18\t \x01(\x0b\x32\x11.gazebo.msgs.Pose\x12#\n\x06visual\x18\n \x03(\x0b\x32\x13.gazebo.msgs.Visual\x12)\n\tcollision\x18\x0b \x03(\x0b\x32\x16.gazebo.msgs.Collision\x12#\n\x06sensor\x18\x0c \x03(\x0b\x32\x13.gazebo.msgs.Sensor\x12)\n\tprojector\x18\r \x03(\x0b\x32\x16.gazebo.msgs.Projector\x12\x11\n\tcanonical\x18\x0e \x01(\x08\x12%\n\x07\x62\x61ttery\x18\x0f \x03(\x0b\x32\x14.gazebo.msgs.Battery\x12\x13\n\x0b\x65nable_wind\x18\x10 \x01(\x08\x12#\n\x04wind\x18\x11 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12!\n\x05light\x18\x12 \x03(\x0b\x32\x12.gazebo.msgs.Light'
  ,
  dependencies=[inertial__pb2.DESCRIPTOR,collision__pb2.DESCRIPTOR,light__pb2.DESCRIPTOR,visual__pb2.DESCRIPTOR,sensor__pb2.DESCRIPTOR,projector__pb2.DESCRIPTOR,pose__pb2.DESCRIPTOR,battery__pb2.DESCRIPTOR,density__pb2.DESCRIPTOR,vector3d__pb2.DESCRIPTOR,])




_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='gazebo.msgs.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Link.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Link.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_collide', full_name='gazebo.msgs.Link.self_collide', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gravity', full_name='gazebo.msgs.Link.gravity', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinematic', full_name='gazebo.msgs.Link.kinematic', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='gazebo.msgs.Link.enabled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='density', full_name='gazebo.msgs.Link.density', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inertial', full_name='gazebo.msgs.Link.inertial', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.Link.pose', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visual', full_name='gazebo.msgs.Link.visual', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collision', full_name='gazebo.msgs.Link.collision', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor', full_name='gazebo.msgs.Link.sensor', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='projector', full_name='gazebo.msgs.Link.projector', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canonical', full_name='gazebo.msgs.Link.canonical', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='gazebo.msgs.Link.battery', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_wind', full_name='gazebo.msgs.Link.enable_wind', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wind', full_name='gazebo.msgs.Link.wind', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='light', full_name='gazebo.msgs.Link.light', index=17,
      number=18, type=11, cpp_type=10, label=3,
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
  serialized_start=177,
  serialized_end=708,
)

_LINK.fields_by_name['density'].message_type = density__pb2._DENSITY
_LINK.fields_by_name['inertial'].message_type = inertial__pb2._INERTIAL
_LINK.fields_by_name['pose'].message_type = pose__pb2._POSE
_LINK.fields_by_name['visual'].message_type = visual__pb2._VISUAL
_LINK.fields_by_name['collision'].message_type = collision__pb2._COLLISION
_LINK.fields_by_name['sensor'].message_type = sensor__pb2._SENSOR
_LINK.fields_by_name['projector'].message_type = projector__pb2._PROJECTOR
_LINK.fields_by_name['battery'].message_type = battery__pb2._BATTERY
_LINK.fields_by_name['wind'].message_type = vector3d__pb2._VECTOR3D
_LINK.fields_by_name['light'].message_type = light__pb2._LIGHT
DESCRIPTOR.message_types_by_name['Link'] = _LINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
  'DESCRIPTOR' : _LINK,
  '__module__' : 'link_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Link)
  })
_sym_db.RegisterMessage(Link)


# @@protoc_insertion_point(module_scope)
