# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: topic_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import publish_pb2 as publish__pb2
import subscribe_pb2 as subscribe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='topic_info.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10topic_info.proto\x12\x0bgazebo.msgs\x1a\rpublish.proto\x1a\x0fsubscribe.proto\"r\n\tTopicInfo\x12\x10\n\x08msg_type\x18\x01 \x02(\t\x12\'\n\tpublisher\x18\x02 \x03(\x0b\x32\x14.gazebo.msgs.Publish\x12*\n\nsubscriber\x18\x03 \x03(\x0b\x32\x16.gazebo.msgs.Subscribe'
  ,
  dependencies=[publish__pb2.DESCRIPTOR,subscribe__pb2.DESCRIPTOR,])




_TOPICINFO = _descriptor.Descriptor(
  name='TopicInfo',
  full_name='gazebo.msgs.TopicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='gazebo.msgs.TopicInfo.msg_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='gazebo.msgs.TopicInfo.publisher', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subscriber', full_name='gazebo.msgs.TopicInfo.subscriber', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=65,
  serialized_end=179,
)

_TOPICINFO.fields_by_name['publisher'].message_type = publish__pb2._PUBLISH
_TOPICINFO.fields_by_name['subscriber'].message_type = subscribe__pb2._SUBSCRIBE
DESCRIPTOR.message_types_by_name['TopicInfo'] = _TOPICINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TopicInfo = _reflection.GeneratedProtocolMessageType('TopicInfo', (_message.Message,), {
  'DESCRIPTOR' : _TOPICINFO,
  '__module__' : 'topic_info_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.TopicInfo)
  })
_sym_db.RegisterMessage(TopicInfo)


# @@protoc_insertion_point(module_scope)
