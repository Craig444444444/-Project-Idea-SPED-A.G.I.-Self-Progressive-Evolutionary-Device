# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI Logging Manager Tests
Created: 2025-05-31 16:55:54 UTC
Author: Craig444444444
"""

import unittest
from core.utils.logging_manager import LoggingManager

class TestLoggingManager(unittest.TestCase):
    def setUp(self):
        self.manager = LoggingManager()
        self.test_message = "Test log message"
    
    def test_log_event(self):
        """Test logging events."""
        # Valid log
        result = self.manager.log_event(
            "system",
            "INFO",
            self.test_message,
            extra_data="test"
        )
        self.assertEqual(result["message"], self.test_message)
        self.assertIn("timestamp", result)
        self.assertIn("user", result)
        
        # Invalid category
        with self.assertRaises(ValueError):
            self.manager.log_event(
                "invalid_category",
                "INFO",
                self.test_message
            )
        
        # Invalid level
        with self.assertRaises(ValueError):
            self.manager.log_event(
                "system",
                "INVALID_LEVEL",
                self.test_message
            )
    
    def test_get_logs(self):
        """Test log retrieval."""
        # Log some test events
        self.manager.log_event("system", "INFO", "Test 1")
        self.manager.log_event("system", "INFO", "Test 2")
        
        # Retrieve logs
        logs = self.manager.get_logs("system")
        self.assertGreater(len(logs), 0)
        
        # Invalid category
        with self.assertRaises(ValueError):
            self.manager.get_logs("invalid_category")

if __name__ == '__main__':
    unittest.main()
