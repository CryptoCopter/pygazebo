# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logical_camera_image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pose_pb2 as pose__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logical_camera_image.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1alogical_camera_image.proto\x12\x0bgazebo.msgs\x1a\npose.proto\"\xa3\x01\n\x12LogicalCameraImage\x12\x1f\n\x04pose\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Pose\x12\x34\n\x05model\x18\x02 \x03(\x0b\x32%.gazebo.msgs.LogicalCameraImage.Model\x1a\x36\n\x05Model\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1f\n\x04pose\x18\x02 \x02(\x0b\x32\x11.gazebo.msgs.Pose'
  ,
  dependencies=[pose__pb2.DESCRIPTOR,])




_LOGICALCAMERAIMAGE_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='gazebo.msgs.LogicalCameraImage.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.LogicalCameraImage.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.LogicalCameraImage.Model.pose', index=1,
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
  serialized_start=165,
  serialized_end=219,
)

_LOGICALCAMERAIMAGE = _descriptor.Descriptor(
  name='LogicalCameraImage',
  full_name='gazebo.msgs.LogicalCameraImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.LogicalCameraImage.pose', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='gazebo.msgs.LogicalCameraImage.model', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGICALCAMERAIMAGE_MODEL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=219,
)

_LOGICALCAMERAIMAGE_MODEL.fields_by_name['pose'].message_type = pose__pb2._POSE
_LOGICALCAMERAIMAGE_MODEL.containing_type = _LOGICALCAMERAIMAGE
_LOGICALCAMERAIMAGE.fields_by_name['pose'].message_type = pose__pb2._POSE
_LOGICALCAMERAIMAGE.fields_by_name['model'].message_type = _LOGICALCAMERAIMAGE_MODEL
DESCRIPTOR.message_types_by_name['LogicalCameraImage'] = _LOGICALCAMERAIMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogicalCameraImage = _reflection.GeneratedProtocolMessageType('LogicalCameraImage', (_message.Message,), {

  'Model' : _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
    'DESCRIPTOR' : _LOGICALCAMERAIMAGE_MODEL,
    '__module__' : 'logical_camera_image_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.LogicalCameraImage.Model)
    })
  ,
  'DESCRIPTOR' : _LOGICALCAMERAIMAGE,
  '__module__' : 'logical_camera_image_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.LogicalCameraImage)
  })
_sym_db.RegisterMessage(LogicalCameraImage)
_sym_db.RegisterMessage(LogicalCameraImage.Model)


# @@protoc_insertion_point(module_scope)
