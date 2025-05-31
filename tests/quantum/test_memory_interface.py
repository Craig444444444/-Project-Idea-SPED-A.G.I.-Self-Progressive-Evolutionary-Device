# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Quantum Memory Interface Tests
Created: 2025-05-31 17:38:57 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from core.quantum.quantum_circuit import QuantumCircuitManager
from core.quantum.error_mitigation import ErrorMitigationSystem
from core.quantum.memory_interface import QuantumMemoryInterface

class TestQuantumMemoryInterface(unittest.TestCase):
    def setUp(self):
        self.qcm = QuantumCircuitManager(n_qubits=20)
        self.ems = ErrorMitigationSystem(self.qcm)
        self.qmi = QuantumMemoryInterface(self.qcm, self.ems)
        self.test_data = np.random.rand(5)
    
    def test_initialization(self):
        """Test quantum memory interface initialization."""
        self.assertIn("direct", self.qmi.encoding_schemes)
        self.assertIn("compressed", self.qmi.encoding_schemes)
        self.assertIn("error_protected", self.qmi.encoding_schemes)
    
    def test_state_storage(self):
        """Test quantum state storage."""
        state_id = self.qmi.store_state(
            self.test_data,
            encoding_scheme="error_protected"
        )
        self.assertIn(state_id, self.qmi.memory_states)
        stored_state = self.qmi.memory_states[state_id]
        self.assertEqual(stored_state.encoding, "error_protected")
    
    def test_state_retrieval(self):
        """Test quantum state retrieval."""
        state_id = self.qmi.store_state(self.test_data)
        retrieved_data = self.qmi.retrieve_state(state_id)
        self.assertEqual(len(retrieved_data), len(self.test_data))
    
    def test_fidelity_monitoring(self):
        """Test fidelity monitoring."""
        state_id = self.qmi.store_state(self.test_data)
        fidelities = self.qmi.monitor_state_fidelity()
        self.assertIn(state_id, fidelities)
        self.assertLess(fidelities[state_id], 1.0)  # Should decay over time

if __name__ == '__main__':
    unittest.main()
