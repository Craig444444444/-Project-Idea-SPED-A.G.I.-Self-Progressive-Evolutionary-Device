# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI State Manager Tests
Created: 2025-05-31 16:55:54 UTC
Author: Craig444444444
"""

import unittest
from core.utils.state_manager import StateManager

class TestStateManager(unittest.TestCase):
    def setUp(self):
        self.manager = StateManager()
        self.test_state = {"test_key": "test_value"}
    
    def test_update_state(self):
        """Test state updates."""
        result = self.manager.update_state(self.test_state)
        self.assertEqual(result["test_key"], "test_value")
        self.assertIn("timestamp", result)
        self.assertIn("user", result)
    
    def test_get_state(self):
        """Test state retrieval."""
        # Update state first
        self.manager.update_state(self.test_state)
        
        # Get state
        state = self.manager.get_state()
        self.assertEqual(state["test_key"], "test_value")
        self.assertIn("timestamp", state)
    
    def test_get_state_history(self):
        """Test state history retrieval."""
        # Create multiple states
        states = [
            {"key": f"value_{i}"} for i in range(3)
        ]
        
        for state in states:
            self.manager.update_state(state)
        
        # Get history
        history = self.manager.get_state_history()
        self.assertGreater(len(history), 0)

if __name__ == '__main__':
    unittest.main()
