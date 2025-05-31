# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: Proprietary
"""
SPED-AGI Quantum System Usage Example
Created: 2025-05-31 17:48:03 UTC
Author: Craig444444444
"""

import numpy as np
from core.quantum.quantum_circuit import QuantumCircuitManager
from core.quantum.error_mitigation import ErrorMitigationSystem
from core.quantum.memory_interface import QuantumMemoryInterface
from core.quantum.encoding_methods import QuantumEncoder

def demonstrate_quantum_processing():
    """Demonstrate quantum processing capabilities."""
    # Initialize components
    qcm = QuantumCircuitManager(n_qubits=20)
    ems = ErrorMitigationSystem(qcm)
    qmi = QuantumMemoryInterface(qcm, ems)
    encoder = QuantumEncoder(n_qubits=20)
    
    # Create test data
    data = np.random.rand(10)
    print(f"Original data: {data}\n")
    
    # 1. Quantum encoding
    print("1. Encoding quantum state...")
    encoded = encoder.encode_quantum_state(
        data,
        method="amplitude",
        error_protection=True
    )
    print(f"Encoding fidelity: {encoded['fidelity']:.4f}\n")
    
    # 2. Create quantum circuit
    print("2. Creating quantum circuit...")
    circuit = qcm.create_learning_circuit(
        data,
        optimization_level=2
    )
    print(f"Circuit type: {circuit['type']}\n")
    
    # 3. Apply error mitigation
    print("3. Applying error mitigation...")
    mitigated = ems.apply_error_mitigation(circuit)
    print(f"Applied strategies: {len(mitigated['applied_strategies'])}\n")
    
    # 4. Store in quantum memory
    print("4. Storing in quantum memory...")
    state_id = qmi.store_state(
        data,
        encoding_scheme="error_protected"
    )
    print(f"State ID: {state_id}\n")
    
    # 5. Monitor state fidelity
    print("5. Monitoring state fidelity...")
    fidelities = qmi.monitor_state_fidelity()
    print(f"Current fidelity: {fidelities[state_id]:.4f}\n")
    
    # 6. Retrieve and decode
    print("6. Retrieving and decoding...")
    retrieved = qmi.retrieve_state(state_id)
    decoded = encoder.decode_quantum_state(encoded)
    
    print(f"Retrieved data: {retrieved}\n")
    print(f"Decoded data: {decoded[:len(data)]}\n")
    
    # 7. Calculate accuracy
    accuracy = np.mean(np.abs(data - decoded[:len(data)]))
    print(f"Average accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    demonstrate_quantum_processing()
