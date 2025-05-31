# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Quantum Encoding Methods Tests
Created: 2025-05-31 17:43:03 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from core.quantum.encoding_methods import QuantumEncoder

class TestQuantumEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = QuantumEncoder(n_qubits=4)
        self.test_data = np.array([0.1, 0.2, 0.3, 0.4])
    
    def test_initialization(self):
        """Test quantum encoder initialization."""
        self.assertIn("amplitude", self.encoder.configs)
        self.assertIn("phase", self.encoder.configs)
        self.assertIn("superdense", self.encoder.configs)
    
    def test_amplitude_encoding(self):
        """Test amplitude encoding method."""
        result = self.encoder.encode_quantum_state(
            self.test_data,
            method="amplitude"
        )
        self.assertEqual(len(result["state_vector"]), 2 ** 4)
        self.assertTrue(result["error_protected"])
    
    def test_phase_encoding(self):
        """Test phase encoding method."""
        result = self.encoder.encode_quantum_state(
            self.test_data,
            method="phase"
        )
        self.assertEqual(len(result["state_vector"]), 2 ** 4)
        decoded = self.encoder.decode_quantum_state(result)
        np.testing.assert_array_almost_equal(
            decoded[:len(self.test_data)],
            self.test_data,
            decimal=5
        )
    
    def test_superdense_encoding(self):
        """Test superdense encoding method."""
        result = self.encoder.encode_quantum_state(
            self.test_data,
            method="superdense"
        )
        self.assertTrue(result["error_protected"])
        decoded = self.encoder.decode_quantum_state(result)
        self.assertEqual(len(decoded), 4)
    
    def test_error_protection(self):
        """Test error protection mechanisms."""
        result = self.encoder.encode_quantum_state(
            self.test_data,
            method="amplitude",
            error_protection=True
        )
        self.assertTrue(result["error_protected"])
        self.assertGreater(result["fidelity"], 0.99)

if __name__ == '__main__':
    unittest.main()
