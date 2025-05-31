# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI Timestamp Manager Tests
Created: 2025-05-31 16:55:54 UTC
Author: Craig444444444
"""

import unittest
from core.utils.timestamp_manager import TimestampManager

class TestTimestampManager(unittest.TestCase):
    def setUp(self):
        self.manager = TimestampManager()
        self.current_timestamp = "UTC - 2025-05-31 16:55:54"
        self.current_user = "Craig444444444"
    
    def test_validate_timestamp_format(self):
        """Test timestamp validation."""
        # Valid timestamp
        result = self.manager.validate_timestamp_format(self.current_timestamp)
        self.assertTrue(result["valid"])
        
        # Invalid timestamp
        invalid_timestamp = "2025-05-31"
        result = self.manager.validate_timestamp_format(invalid_timestamp)
        self.assertFalse(result["valid"])
    
    def test_validate_user_format(self):
        """Test user format validation."""
        # Valid user
        result = self.manager.validate_user_format(self.current_user)
        self.assertTrue(result["valid"])
        
        # Invalid user
        invalid_user = "User@123"
        result = self.manager.validate_user_format(invalid_user)
        self.assertFalse(result["valid"])
    
    def test_get_current_state(self):
        """Test current state retrieval."""
        state = self.manager.get_current_state()
        self.assertEqual(state["user"], self.current_user)
        self.assertIn("timestamp", state)
        self.assertIn("version", state)

if __name__ == '__main__':
    unittest.main()
