# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='value.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('Z\010pipeline'),
  serialized_pb=_b('\n\x0bvalue.proto\x1a google/protobuf/descriptor.proto\"\x1d\n\nValueError\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\tValueList\x12\x18\n\x05items\x18\x01 \x03(\x0b\x32\t.ValueRaw\"j\n\tValueDict\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x15.ValueDict.ItemsEntry\x1a\x37\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.ValueRaw:\x02\x38\x01\"\xbb\x01\n\x08ValueRaw\x12\x1a\n\x04null\x18\x01 \x01(\x0e\x32\n.NullValueH\x00\x12\x10\n\x06\x64ouble\x18\x02 \x01(\x01H\x00\x12\x0f\n\x05int64\x18\x03 \x01(\x03H\x00\x12\x0e\n\x04\x62ool\x18\x04 \x01(\x08H\x00\x12\x10\n\x06string\x18\x05 \x01(\tH\x00\x12\x0f\n\x05\x62ytes\x18\x06 \x01(\x0cH\x00\x12\x1a\n\x04list\x18\x07 \x01(\x0b\x32\n.ValueListH\x00\x12\x1a\n\x04\x64ict\x18\x08 \x01(\x0b\x32\n.ValueDictH\x00\x42\x05\n\x03raw\"\xb4\x01\n\x05Value\x12\x1c\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0b.ValueErrorH\x00\x12\x18\n\x03raw\x18\x02 \x01(\x0b\x32\t.ValueRawH\x00\x12\x15\n\x0b\x64\x61taset_uri\x18\x03 \x01(\tH\x00\x12\x11\n\x07\x63sv_uri\x18\x04 \x01(\tH\x00\x12\x14\n\npickle_uri\x18\x05 \x01(\tH\x00\x12\x15\n\x0bpickle_blob\x18\x06 \x01(\x0cH\x00\x12\x13\n\tplasma_id\x18\x07 \x01(\x0cH\x00\x42\x07\n\x05value*|\n\tValueType\x12\x18\n\x14VALUE_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03RAW\x10\x01\x12\x0f\n\x0b\x44\x41TASET_URI\x10\x02\x12\x0b\n\x07\x43SV_URI\x10\x03\x12\x0e\n\nPICKLE_URI\x10\x04\x12\x0f\n\x0bPICKLE_BLOB\x10\x05\x12\r\n\tPLASMA_ID\x10\x06*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\x42\nZ\x08pipelineb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALUE_TYPE_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATASET_URI', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSV_URI', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKLE_URI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKLE_BLOB', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLASMA_ID', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=600,
  serialized_end=724,
)
_sym_db.RegisterEnumDescriptor(_VALUETYPE)

ValueType = enum_type_wrapper.EnumTypeWrapper(_VALUETYPE)
_NULLVALUE = _descriptor.EnumDescriptor(
  name='NullValue',
  full_name='NullValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL_VALUE', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=726,
  serialized_end=753,
)
_sym_db.RegisterEnumDescriptor(_NULLVALUE)

NullValue = enum_type_wrapper.EnumTypeWrapper(_NULLVALUE)
VALUE_TYPE_UNDEFINED = 0
RAW = 1
DATASET_URI = 2
CSV_URI = 3
PICKLE_URI = 4
PICKLE_BLOB = 5
PLASMA_ID = 6
NULL_VALUE = 0



_VALUEERROR = _descriptor.Descriptor(
  name='ValueError',
  full_name='ValueError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ValueError.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=49,
  serialized_end=78,
)


_VALUELIST = _descriptor.Descriptor(
  name='ValueList',
  full_name='ValueList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ValueList.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=80,
  serialized_end=117,
)


_VALUEDICT_ITEMSENTRY = _descriptor.Descriptor(
  name='ItemsEntry',
  full_name='ValueDict.ItemsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ValueDict.ItemsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ValueDict.ItemsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=225,
)

_VALUEDICT = _descriptor.Descriptor(
  name='ValueDict',
  full_name='ValueDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ValueDict.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VALUEDICT_ITEMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=225,
)


_VALUERAW = _descriptor.Descriptor(
  name='ValueRaw',
  full_name='ValueRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='null', full_name='ValueRaw.null', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double', full_name='ValueRaw.double', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64', full_name='ValueRaw.int64', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='ValueRaw.bool', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='ValueRaw.string', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='ValueRaw.bytes', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='ValueRaw.list', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dict', full_name='ValueRaw.dict', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='raw', full_name='ValueRaw.raw',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=228,
  serialized_end=415,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='Value.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='Value.raw', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_uri', full_name='Value.dataset_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='csv_uri', full_name='Value.csv_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pickle_uri', full_name='Value.pickle_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pickle_blob', full_name='Value.pickle_blob', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plasma_id', full_name='Value.plasma_id', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='Value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=418,
  serialized_end=598,
)

_VALUELIST.fields_by_name['items'].message_type = _VALUERAW
_VALUEDICT_ITEMSENTRY.fields_by_name['value'].message_type = _VALUERAW
_VALUEDICT_ITEMSENTRY.containing_type = _VALUEDICT
_VALUEDICT.fields_by_name['items'].message_type = _VALUEDICT_ITEMSENTRY
_VALUERAW.fields_by_name['null'].enum_type = _NULLVALUE
_VALUERAW.fields_by_name['list'].message_type = _VALUELIST
_VALUERAW.fields_by_name['dict'].message_type = _VALUEDICT
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['null'])
_VALUERAW.fields_by_name['null'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['double'])
_VALUERAW.fields_by_name['double'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['int64'])
_VALUERAW.fields_by_name['int64'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['bool'])
_VALUERAW.fields_by_name['bool'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['string'])
_VALUERAW.fields_by_name['string'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['bytes'])
_VALUERAW.fields_by_name['bytes'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['list'])
_VALUERAW.fields_by_name['list'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUERAW.oneofs_by_name['raw'].fields.append(
  _VALUERAW.fields_by_name['dict'])
_VALUERAW.fields_by_name['dict'].containing_oneof = _VALUERAW.oneofs_by_name['raw']
_VALUE.fields_by_name['error'].message_type = _VALUEERROR
_VALUE.fields_by_name['raw'].message_type = _VALUERAW
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['error'])
_VALUE.fields_by_name['error'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['raw'])
_VALUE.fields_by_name['raw'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['dataset_uri'])
_VALUE.fields_by_name['dataset_uri'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['csv_uri'])
_VALUE.fields_by_name['csv_uri'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['pickle_uri'])
_VALUE.fields_by_name['pickle_uri'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['pickle_blob'])
_VALUE.fields_by_name['pickle_blob'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['plasma_id'])
_VALUE.fields_by_name['plasma_id'].containing_oneof = _VALUE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['ValueError'] = _VALUEERROR
DESCRIPTOR.message_types_by_name['ValueList'] = _VALUELIST
DESCRIPTOR.message_types_by_name['ValueDict'] = _VALUEDICT
DESCRIPTOR.message_types_by_name['ValueRaw'] = _VALUERAW
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.enum_types_by_name['ValueType'] = _VALUETYPE
DESCRIPTOR.enum_types_by_name['NullValue'] = _NULLVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValueError = _reflection.GeneratedProtocolMessageType('ValueError', (_message.Message,), dict(
  DESCRIPTOR = _VALUEERROR,
  __module__ = 'value_pb2'
  # @@protoc_insertion_point(class_scope:ValueError)
  ))
_sym_db.RegisterMessage(ValueError)

ValueList = _reflection.GeneratedProtocolMessageType('ValueList', (_message.Message,), dict(
  DESCRIPTOR = _VALUELIST,
  __module__ = 'value_pb2'
  # @@protoc_insertion_point(class_scope:ValueList)
  ))
_sym_db.RegisterMessage(ValueList)

ValueDict = _reflection.GeneratedProtocolMessageType('ValueDict', (_message.Message,), dict(

  ItemsEntry = _reflection.GeneratedProtocolMessageType('ItemsEntry', (_message.Message,), dict(
    DESCRIPTOR = _VALUEDICT_ITEMSENTRY,
    __module__ = 'value_pb2'
    # @@protoc_insertion_point(class_scope:ValueDict.ItemsEntry)
    ))
  ,
  DESCRIPTOR = _VALUEDICT,
  __module__ = 'value_pb2'
  # @@protoc_insertion_point(class_scope:ValueDict)
  ))
_sym_db.RegisterMessage(ValueDict)
_sym_db.RegisterMessage(ValueDict.ItemsEntry)

ValueRaw = _reflection.GeneratedProtocolMessageType('ValueRaw', (_message.Message,), dict(
  DESCRIPTOR = _VALUERAW,
  __module__ = 'value_pb2'
  # @@protoc_insertion_point(class_scope:ValueRaw)
  ))
_sym_db.RegisterMessage(ValueRaw)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'value_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  ))
_sym_db.RegisterMessage(Value)


DESCRIPTOR._options = None
_VALUEDICT_ITEMSENTRY._options = None
# @@protoc_insertion_point(module_scope)
