# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Quantum Circuit Tests
Created: 2025-05-31 17:31:07 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from core.quantum.quantum_circuit import QuantumCircuitManager

class TestQuantumCircuitManager(unittest.TestCase):
    def setUp(self):
        self.qcm = QuantumCircuitManager(n_qubits=20)
        self.test_data = np.random.rand(10, 10)
    
    def test_initialization(self):
        """Test quantum circuit manager initialization."""
        self.assertEqual(self.qcm.n_qubits, 20)
        self.assertIn("learning", self.qcm.circuit_configs)
        self.assertIn("memory", self.qcm.circuit_configs)
        self.assertIn("processing", self.qcm.circuit_configs)
    
    def test_create_learning_circuit(self):
        """Test learning circuit creation."""
        circuit = self.qcm.create_learning_circuit(
            self.test_data,
            optimization_level=2
        )
        self.assertEqual(circuit["type"], "learning")
        self.assertEqual(circuit["n_qubits"], 20)
        self.assertEqual(circuit["input_shape"], self.test_data.shape)
    
    def test_optimize_circuit(self):
        """Test circuit optimization."""
        circuit = self.qcm.create_learning_circuit(self.test_data)
        optimized = self.qcm.optimize_circuit(circuit)
        self.assertIn("optimization_steps", optimized)
        self.assertIn("timestamp", optimized)
    
    def test_validate_circuit(self):
        """Test circuit validation."""
        circuit = self.qcm.create_learning_circuit(self.test_data)
        validation = self.qcm.validate_circuit(circuit)
        self.assertIn("valid", validation)
        self.assertIn("checks", validation)

if __name__ == '__main__':
    unittest.main()
