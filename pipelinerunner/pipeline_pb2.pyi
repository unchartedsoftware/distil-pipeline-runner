# @generated by generate_proto_mypy_stubs.py.  Do not edit!
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class PipelineContext(int):
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> int: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[int]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, int]]: ...
PIPELINE_CONTEXT_UNKNOWN = typing___cast(PipelineContext, 0)
PRETRAINING = typing___cast(PipelineContext, 1)
TESTING = typing___cast(PipelineContext, 2)
EVALUATION = typing___cast(PipelineContext, 3)
PRODUCTION = typing___cast(PipelineContext, 4)

class ContainerArgument(google___protobuf___message___Message):
    data = ... # type: typing___Text

    def __init__(self,
        data : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContainerArgument: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ContainerArguments(google___protobuf___message___Message):
    data = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        data : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContainerArguments: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DataArgument(google___protobuf___message___Message):
    data = ... # type: typing___Text

    def __init__(self,
        data : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DataArgument: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DataArguments(google___protobuf___message___Message):
    data = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        data : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DataArguments: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PrimitiveArgument(google___protobuf___message___Message):
    data = ... # type: int

    def __init__(self,
        data : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrimitiveArgument: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PrimitiveArguments(google___protobuf___message___Message):
    data = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        data : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrimitiveArguments: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ValueArgument(google___protobuf___message___Message):

    @property
    def data(self) -> Value: ...

    def __init__(self,
        data : typing___Optional[Value] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ValueArgument: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PrimitiveStepArgument(google___protobuf___message___Message):

    @property
    def container(self) -> ContainerArgument: ...

    @property
    def data(self) -> DataArgument: ...

    @property
    def container_list(self) -> ContainerArguments: ...

    def __init__(self,
        container : typing___Optional[ContainerArgument] = None,
        data : typing___Optional[DataArgument] = None,
        container_list : typing___Optional[ContainerArguments] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrimitiveStepArgument: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PrimitiveStepHyperparameter(google___protobuf___message___Message):

    @property
    def container(self) -> ContainerArgument: ...

    @property
    def data(self) -> DataArgument: ...

    @property
    def primitive(self) -> PrimitiveArgument: ...

    @property
    def value(self) -> ValueArgument: ...

    @property
    def data_set(self) -> DataArguments: ...

    @property
    def primitives_set(self) -> PrimitiveArguments: ...

    def __init__(self,
        container : typing___Optional[ContainerArgument] = None,
        data : typing___Optional[DataArgument] = None,
        primitive : typing___Optional[PrimitiveArgument] = None,
        value : typing___Optional[ValueArgument] = None,
        data_set : typing___Optional[DataArguments] = None,
        primitives_set : typing___Optional[PrimitiveArguments] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrimitiveStepHyperparameter: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class StepInput(google___protobuf___message___Message):
    data = ... # type: typing___Text

    def __init__(self,
        data : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StepInput: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class StepOutput(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StepOutput: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineSource(google___protobuf___message___Message):
    name = ... # type: typing___Text
    contact = ... # type: typing___Text
    pipelines = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        contact : typing___Optional[typing___Text] = None,
        pipelines : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineSource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineDescriptionUser(google___protobuf___message___Message):
    id = ... # type: typing___Text
    reason = ... # type: typing___Text
    rationale = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        reason : typing___Optional[typing___Text] = None,
        rationale : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineDescriptionUser: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineDescriptionInput(google___protobuf___message___Message):
    name = ... # type: typing___Text

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineDescriptionInput: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineDescriptionOutput(google___protobuf___message___Message):
    name = ... # type: typing___Text
    data = ... # type: typing___Text

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineDescriptionOutput: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PrimitivePipelineDescriptionStep(google___protobuf___message___Message):
    class ArgumentsEntry(google___protobuf___message___Message):
        key = ... # type: typing___Text

        @property
        def value(self) -> PrimitiveStepArgument: ...

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PrimitiveStepArgument] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PrimitivePipelineDescriptionStep.ArgumentsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

    class HyperparamsEntry(google___protobuf___message___Message):
        key = ... # type: typing___Text

        @property
        def value(self) -> PrimitiveStepHyperparameter: ...

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[PrimitiveStepHyperparameter] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PrimitivePipelineDescriptionStep.HyperparamsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...


    @property
    def primitive(self) -> Primitive: ...

    @property
    def arguments(self) -> typing___MutableMapping[typing___Text, PrimitiveStepArgument]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StepOutput]: ...

    @property
    def hyperparams(self) -> typing___MutableMapping[typing___Text, PrimitiveStepHyperparameter]: ...

    @property
    def users(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PipelineDescriptionUser]: ...

    def __init__(self,
        primitive : typing___Optional[Primitive] = None,
        arguments : typing___Optional[typing___Mapping[typing___Text, PrimitiveStepArgument]] = None,
        outputs : typing___Optional[typing___Iterable[StepOutput]] = None,
        hyperparams : typing___Optional[typing___Mapping[typing___Text, PrimitiveStepHyperparameter]] = None,
        users : typing___Optional[typing___Iterable[PipelineDescriptionUser]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PrimitivePipelineDescriptionStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class SubpipelinePipelineDescriptionStep(google___protobuf___message___Message):

    @property
    def pipeline(self) -> PipelineDescription: ...

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StepInput]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StepOutput]: ...

    def __init__(self,
        pipeline : typing___Optional[PipelineDescription] = None,
        inputs : typing___Optional[typing___Iterable[StepInput]] = None,
        outputs : typing___Optional[typing___Iterable[StepOutput]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SubpipelinePipelineDescriptionStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PlaceholderPipelineDescriptionStep(google___protobuf___message___Message):

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StepInput]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StepOutput]: ...

    def __init__(self,
        inputs : typing___Optional[typing___Iterable[StepInput]] = None,
        outputs : typing___Optional[typing___Iterable[StepOutput]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PlaceholderPipelineDescriptionStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineDescriptionStep(google___protobuf___message___Message):

    @property
    def primitive(self) -> PrimitivePipelineDescriptionStep: ...

    @property
    def pipeline(self) -> SubpipelinePipelineDescriptionStep: ...

    @property
    def placeholder(self) -> PlaceholderPipelineDescriptionStep: ...

    def __init__(self,
        primitive : typing___Optional[PrimitivePipelineDescriptionStep] = None,
        pipeline : typing___Optional[SubpipelinePipelineDescriptionStep] = None,
        placeholder : typing___Optional[PlaceholderPipelineDescriptionStep] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineDescriptionStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PipelineDescription(google___protobuf___message___Message):
    id = ... # type: typing___Text
    context = ... # type: PipelineContext
    name = ... # type: typing___Text
    description = ... # type: typing___Text
    digest = ... # type: typing___Text

    @property
    def source(self) -> PipelineSource: ...

    @property
    def created(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def users(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PipelineDescriptionUser]: ...

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PipelineDescriptionInput]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PipelineDescriptionOutput]: ...

    @property
    def steps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PipelineDescriptionStep]: ...

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        source : typing___Optional[PipelineSource] = None,
        created : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        context : typing___Optional[PipelineContext] = None,
        name : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        users : typing___Optional[typing___Iterable[PipelineDescriptionUser]] = None,
        inputs : typing___Optional[typing___Iterable[PipelineDescriptionInput]] = None,
        outputs : typing___Optional[typing___Iterable[PipelineDescriptionOutput]] = None,
        steps : typing___Optional[typing___Iterable[PipelineDescriptionStep]] = None,
        digest : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PipelineDescription: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
