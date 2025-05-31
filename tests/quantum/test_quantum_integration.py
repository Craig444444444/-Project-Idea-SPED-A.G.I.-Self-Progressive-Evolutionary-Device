# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Quantum Integration Tests
Created: 2025-05-31 17:48:03 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from core.quantum.quantum_circuit import QuantumCircuitManager
from core.quantum.error_mitigation import ErrorMitigationSystem
from core.quantum.memory_interface import QuantumMemoryInterface
from core.quantum.encoding_methods import QuantumEncoder

class TestQuantumIntegration(unittest.TestCase):
    def setUp(self):
        # Initialize all components
        self.qcm = QuantumCircuitManager(n_qubits=20)
        self.ems = ErrorMitigationSystem(self.qcm)
        self.qmi = QuantumMemoryInterface(self.qcm, self.ems)
        self.encoder = QuantumEncoder(n_qubits=20)
        
        # Test data
        self.test_data = np.random.rand(10)
    
    def test_full_quantum_pipeline(self):
        """Test complete quantum processing pipeline."""
        # 1. Encode quantum state
        encoded_state = self.encoder.encode_quantum_state(
            self.test_data,
            method="amplitude"
        )
        self.assertTrue(encoded_state["error_protected"])
        
        # 2. Create quantum circuit
        circuit = self.qcm.create_learning_circuit(
            self.test_data,
            optimization_level=2
        )
        self.assertEqual(circuit["type"], "learning")
        
        # 3. Apply error mitigation
        mitigated = self.ems.apply_error_mitigation(circuit)
        self.assertIn("applied_strategies", mitigated)
        
        # 4. Store in quantum memory
        state_id = self.qmi.store_state(
            self.test_data,
            encoding_scheme="error_protected"
        )
        self.assertIn(state_id, self.qmi.memory_states)
        
        # 5. Retrieve and verify
        retrieved_data = self.qmi.retrieve_state(state_id)
        self.assertEqual(len(retrieved_data), len(self.test_data))
    
    def test_error_handling(self):
        """Test error handling across components."""
        with self.assertRaises(ValueError):
            # Test invalid encoding method
            self.encoder.encode_quantum_state(
                self.test_data,
                method="invalid_method"
            )
        
        with self.assertRaises(KeyError):
            # Test invalid state retrieval
            self.qmi.retrieve_state("invalid_state_id")
    
    def test_performance_monitoring(self):
        """Test performance monitoring across components."""
        # 1. Store state
        state_id = self.qmi.store_state(self.test_data)
        
        # 2. Check circuit optimization
        circuit = self.qcm.create_learning_circuit(self.test_data)
        optimized = self.qcm.optimize_circuit(circuit)
        self.assertIn("optimization_steps", optimized)
        
        # 3. Monitor error rates
        analysis = self.ems.analyze_error_rates(circuit)
        self.assertIn("error_rates", analysis)
        
        # 4. Check memory fidelity
        fidelities = self.qmi.monitor_state_fidelity()
        self.assertIn(state_id, fidelities)
    
    def test_quantum_classical_interface(self):
        """Test quantum-classical data interface."""
        # 1. Classical to quantum conversion
        encoded = self.encoder.encode_quantum_state(
            self.test_data,
            method="phase"
        )
        
        # 2. Quantum processing
        circuit = self.qcm.create_learning_circuit(
            self.test_data,
            optimization_level=3
        )
        
        # 3. Quantum to classical conversion
        decoded = self.encoder.decode_quantum_state(encoded)
        np.testing.assert_array_almost_equal(
            decoded[:len(self.test_data)],
            self.test_data,
            decimal=5
        )

if __name__ == '__main__':
    unittest.main()
