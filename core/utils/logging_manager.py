# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI Enhanced Logging System
Created: 2025-05-31 16:50:50 UTC
Author: Craig444444444
"""

import logging
import json
from pathlib import Path
from .timestamp_manager import timestamp_manager

class LoggingManager:
    """Advanced logging system for SPED-AGI."""
    
    def __init__(self):
        self.metadata = timestamp_manager.get_current_state()
        self.log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        
        self.log_categories = {
            "system": "logs/system",
            "quantum": "logs/quantum",
            "security": "logs/security",
            "performance": "logs/performance",
            "audit": "logs/audit"
        }
        
        self._setup_logging_structure()
    
    def _setup_logging_structure(self):
        """Setup logging directory structure and configurations."""
        self.loggers = {}
        
        for category, path in self.log_categories.items():
            # Create directory if it doesn't exist
            Path(path).mkdir(parents=True, exist_ok=True)
            
            # Setup logger for category
            logger = logging.getLogger(f'SPED-AGI-{category}')
            logger.setLevel(logging.DEBUG)
            
            # File handler for category
            handler = logging.FileHandler(f'{path}/{category}.log')
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
            self.loggers[category] = logger
    
    def log_event(self, category, level, message, **kwargs):
        """Log an event with metadata."""
        if category not in self.loggers:
            raise ValueError(f"Invalid log category: {category}")
        
        if level not in self.log_levels:
            raise ValueError(f"Invalid log level: {level}")
        
        event_data = {
            "timestamp": timestamp_manager.get_current_timestamp(),
            "user": timestamp_manager.get_current_user(),
            "message": message,
            **kwargs
        }
        
        self.loggers[category].log(
            self.log_levels[level],
            json.dumps(event_data)
        )
        return event_data
    
    def get_logs(self, category, start_time=None, end_time=None):
        """Retrieve logs for a category within timeframe."""
        if category not in self.log_categories:
            raise ValueError(f"Invalid log category: {category}")
        
        log_path = Path(f'{self.log_categories[category]}/{category}.log')
        if not log_path.exists():
            return []
        
        logs = []
        with open(log_path, 'r') as f:
            for line in f:
                try:
                    log_entry = json.loads(line.split(' - ')[-1])
                    if self._is_in_timeframe(log_entry, start_time, end_time):
                        logs.append(log_entry)
                except:
                    continue
        
        return logs
    
    def _is_in_timeframe(self, log_entry, start_time, end_time):
        """Check if log entry is within specified timeframe."""
        if not start_time and not end_time:
            return True
            
        log_time = log_entry.get('timestamp', '')
        return (not start_time or log_time >= start_time) and \
               (not end_time or log_time <= end_time)

# Global instance
logging_manager = LoggingManager()
