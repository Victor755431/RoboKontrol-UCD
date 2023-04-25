# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robotMsgs.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='robotMsgs.proto',
  package='enac',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0frobotMsgs.proto\x12\x04\x65nac\"/\n\x0c\x45mptyMessage\x12\x1f\n\x17placeHolderToMakeItWork\x18\x01 \x01(\x02\"/\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05theta\x18\x03 \x01(\x02\"L\n\tProximity\x12\x18\n\x10\x63losest_distance\x18\x01 \x01(\x02\x12%\n\x06status\x18\x02 \x01(\x0e\x32\x15.enac.ProximityStatus*0\n\x0fProximityStatus\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\x08\n\x04STOP\x10\x02\x62\x06proto3'
)

_PROXIMITYSTATUS = _descriptor.EnumDescriptor(
  name='ProximityStatus',
  full_name='enac.ProximityStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=201,
  serialized_end=249,
)
_sym_db.RegisterEnumDescriptor(_PROXIMITYSTATUS)

ProximityStatus = enum_type_wrapper.EnumTypeWrapper(_PROXIMITYSTATUS)
OK = 0
WARNING = 1
STOP = 2



_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='enac.EmptyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='placeHolderToMakeItWork', full_name='enac.EmptyMessage.placeHolderToMakeItWork', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=72,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='enac.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='enac.Position.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='enac.Position.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='theta', full_name='enac.Position.theta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=121,
)


_PROXIMITY = _descriptor.Descriptor(
  name='Proximity',
  full_name='enac.Proximity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='closest_distance', full_name='enac.Proximity.closest_distance', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='enac.Proximity.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=199,
)

_PROXIMITY.fields_by_name['status'].enum_type = _PROXIMITYSTATUS
DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Proximity'] = _PROXIMITY
DESCRIPTOR.enum_types_by_name['ProximityStatus'] = _PROXIMITYSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'robotMsgs_pb2'
  # @@protoc_insertion_point(class_scope:enac.EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'robotMsgs_pb2'
  # @@protoc_insertion_point(class_scope:enac.Position)
  })
_sym_db.RegisterMessage(Position)

Proximity = _reflection.GeneratedProtocolMessageType('Proximity', (_message.Message,), {
  'DESCRIPTOR' : _PROXIMITY,
  '__module__' : 'robotMsgs_pb2'
  # @@protoc_insertion_point(class_scope:enac.Proximity)
  })
_sym_db.RegisterMessage(Proximity)


# @@protoc_insertion_point(module_scope)
