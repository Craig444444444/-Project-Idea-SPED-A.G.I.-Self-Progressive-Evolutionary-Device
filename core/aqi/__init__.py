# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI Artificial Quantum Intelligence (AQI) Core Components
Created: 2025-05-31 15:56:14 UTC
Author: Craig444444444

This package provides AQI (Artificial Quantum Intelligence) capabilities for SPED-AGI,
including quantum state preparation, measurement, and error mitigation strategies
optimized for artificial intelligence applications.
"""

from .resilience import (
    AdaptiveErrorMitigation,
    AQIResilienceEngine  # Renamed from QuantumResilienceEngine
)

__all__ = [
    'AdaptiveErrorMitigation',
    'AQIResilienceEngine'
]
