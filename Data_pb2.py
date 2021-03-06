# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Data.proto',
  package='CServer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nData.proto\x12\x07\x43Server\"}\n\x07Request\x12\r\n\x05RFWID\x18\x01 \x01(\x05\x12\x15\n\rBenchMarkType\x18\x02 \x01(\t\x12\x0e\n\x06Metric\x18\x03 \x01(\t\x12\x14\n\x0cnumOfSamples\x18\x04 \x01(\x05\x12\x14\n\x0c\x42\x61tchesStart\x18\x05 \x01(\x05\x12\x10\n\x08\x42\x61tchNum\x18\x06 \x01(\x05\"7\n\x04\x44\x61ta\x12\r\n\x05RFWID\x18\x02 \x01(\x05\x12\x12\n\nLastBatchN\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"$\n\x06ReqLog\x12\x1a\n\x03\x64\x61t\x18\x01 \x03(\x0b\x32\r.CServer.Data\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t2N\n\x10\x42idirectionalRPC\x12:\n\x11GetServerResponse\x12\x10.CServer.Request\x1a\r.CServer.Data\"\x00(\x01\x30\x01\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='CServer.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='RFWID', full_name='CServer.Request.RFWID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BenchMarkType', full_name='CServer.Request.BenchMarkType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Metric', full_name='CServer.Request.Metric', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numOfSamples', full_name='CServer.Request.numOfSamples', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BatchesStart', full_name='CServer.Request.BatchesStart', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BatchNum', full_name='CServer.Request.BatchNum', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=23,
  serialized_end=148,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='CServer.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='RFWID', full_name='CServer.Data.RFWID', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LastBatchN', full_name='CServer.Data.LastBatchN', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='CServer.Data.data', index=2,
      number=1, type=2, cpp_type=6, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=205,
)


_REQLOG = _descriptor.Descriptor(
  name='ReqLog',
  full_name='CServer.ReqLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dat', full_name='CServer.ReqLog.dat', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=243,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='CServer.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='CServer.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=245,
  serialized_end=271,
)

_REQLOG.fields_by_name['dat'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['ReqLog'] = _REQLOG
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.Request)
  })
_sym_db.RegisterMessage(Request)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.Data)
  })
_sym_db.RegisterMessage(Data)

ReqLog = _reflection.GeneratedProtocolMessageType('ReqLog', (_message.Message,), {
  'DESCRIPTOR' : _REQLOG,
  '__module__' : 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.ReqLog)
  })
_sym_db.RegisterMessage(ReqLog)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.Message)
  })
_sym_db.RegisterMessage(Message)



_BIDIRECTIONALRPC = _descriptor.ServiceDescriptor(
  name='BidirectionalRPC',
  full_name='CServer.BidirectionalRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=273,
  serialized_end=351,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='CServer.BidirectionalRPC.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BIDIRECTIONALRPC)

DESCRIPTOR.services_by_name['BidirectionalRPC'] = _BIDIRECTIONALRPC

# @@protoc_insertion_point(module_scope)
