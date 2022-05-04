# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TYPE_CHECKING

from ...utils import _LazyModule, is_flax_available, is_tf_available, is_tokenizers_available, is_torch_available


_import_structure = {
    "configuration_opt": ["OPT_PRETRAINED_CONFIG_ARCHIVE_MAP", "OPTConfig", "OPTOnnxConfig"],
    "tokenization_opt": ["OPTTokenizer"],
}

if is_tokenizers_available():
    _import_structure["tokenization_opt_fast"] = ["OPTTokenizerFast"]

if is_torch_available():
    _import_structure["modeling_opt"] = [
        "OPT_PRETRAINED_MODEL_ARCHIVE_LIST",
        "OPTForCausalLM",
        "OPTForConditionalGeneration",
        "OPTForQuestionAnswering",
        "OPTForSequenceClassification",
        "OPTModel",
        "OPTPretrainedModel",
        "PretrainedOPTModel",
    ]

if is_tf_available():
    _import_structure["modeling_tf_opt"] = ["TFOPTForConditionalGeneration", "TFOPTModel", "TFOPTPretrainedModel"]

if is_flax_available():
    _import_structure["modeling_flax_opt"] = [
        "FlaxOPTDecoderPreTrainedModel",
        "FlaxOPTForCausalLM",
        "FlaxOPTForConditionalGeneration",
        "FlaxOPTForQuestionAnswering",
        "FlaxOPTForSequenceClassification",
        "FlaxOPTModel",
        "FlaxOPTPreTrainedModel",
    ]

if TYPE_CHECKING:
    from .configuration_opt import OPT_PRETRAINED_CONFIG_ARCHIVE_MAP, OPTConfig, OPTOnnxConfig
    from .tokenization_opt import OPTTokenizer

    if is_tokenizers_available():
        from .tokenization_opt_fast import OPTTokenizerFast

    if is_torch_available():
        from .modeling_opt import (
            OPT_PRETRAINED_MODEL_ARCHIVE_LIST,
            OPTForCausalLM,
            OPTForConditionalGeneration,
            OPTForQuestionAnswering,
            OPTForSequenceClassification,
            OPTModel,
            OPTPretrainedModel,
            PretrainedOPTModel,
        )

    if is_tf_available():
        from .modeling_tf_opt import TFOPTForConditionalGeneration, TFOPTModel, TFOPTPretrainedModel

    if is_flax_available():
        from .modeling_flax_opt import (
            FlaxOPTDecoderPreTrainedModel,
            FlaxOPTForCausalLM,
            FlaxOPTForConditionalGeneration,
            FlaxOPTForQuestionAnswering,
            FlaxOPTForSequenceClassification,
            FlaxOPTModel,
            FlaxOPTPreTrainedModel,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)