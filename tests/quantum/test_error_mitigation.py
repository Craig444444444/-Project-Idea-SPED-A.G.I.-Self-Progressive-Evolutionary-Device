# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Error Mitigation Tests
Created: 2025-05-31 17:34:56 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from core.quantum.quantum_circuit import QuantumCircuitManager
from core.quantum.error_mitigation import ErrorMitigationSystem

class TestErrorMitigationSystem(unittest.TestCase):
    def setUp(self):
        self.qcm = QuantumCircuitManager(n_qubits=20)
        self.ems = ErrorMitigationSystem(self.qcm)
        self.test_circuit = self.qcm.create_learning_circuit(
            np.random.rand(10, 10)
        )
    
    def test_initialization(self):
        """Test error mitigation system initialization."""
        self.assertIn("decoherence", self.ems.error_models)
        self.assertIn("gate_error", self.ems.error_models)
        self.assertIn("measurement", self.ems.error_models)
    
    def test_apply_error_mitigation(self):
        """Test error mitigation application."""
        result = self.ems.apply_error_mitigation(self.test_circuit)
        self.assertIn("applied_strategies", result)
        self.assertEqual(len(result["applied_strategies"]), 3)
    
    def test_analyze_error_rates(self):
        """Test error rate analysis."""
        analysis = self.ems.analyze_error_rates(self.test_circuit)
        self.assertIn("error_rates", analysis)
        self.assertIn("decoherence", analysis["error_rates"])
        self.assertIn("current_rate", analysis["error_rates"]["decoherence"])
    
    def test_specific_strategy(self):
        """Test specific mitigation strategy."""
        result = self.ems.apply_error_mitigation(
            self.test_circuit,
            strategies=["decoherence"]
        )
        self.assertEqual(len(result["applied_strategies"]), 1)
        self.assertEqual(
            result["applied_strategies"][0]["model"],
            "decoherence"
        )

if __name__ == '__main__':
    unittest.main()
