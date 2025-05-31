# -*- coding: utf-8 -*-
# Copyright © 2023-2025 Craig Huckerby
# SPDX-License-Identifier: AGPL-3.0-only
"""
SPED-AGI State Management System
Created: 2025-05-31 16:50:50 UTC
Author: Craig444444444
"""

import json
from pathlib import Path
from .timestamp_manager import timestamp_manager
from .logging_manager import logging_manager

class StateManager:
    """State management system for SPED-AGI."""
    
    def __init__(self):
        self.metadata = timestamp_manager.get_current_state()
        self.state_file = "data/state/current_state.json"
        self.history_dir = "data/state/history"
        self.max_history = 100
        
        self._setup_directories()
        self._load_state()
    
    def _setup_directories(self):
        """Setup directory structure for state management."""
        Path(self.state_file).parent.mkdir(parents=True, exist_ok=True)
        Path(self.history_dir).mkdir(parents=True, exist_ok=True)
    
    def _load_state(self):
        """Load current state from file."""
        try:
            with open(self.state_file, 'r') as f:
                self.current_state = json.load(f)
        except:
            self.current_state = {
                "timestamp": timestamp_manager.get_current_timestamp(),
                "user": timestamp_manager.get_current_user(),
                "state": "initialized",
                "version": self.metadata["version"]
            }
            self._save_state()
    
    def _save_state(self):
        """Save current state to file."""
        with open(self.state_file, 'w') as f:
            json.dump(self.current_state, f, indent=4)
    
    def _archive_state(self):
        """Archive current state to history."""
        archive_file = f"{self.history_dir}/state_{self.current_state['timestamp'].replace(' ', '_')}.json"
        with open(archive_file, 'w') as f:
            json.dump(self.current_state, f, indent=4)
        
        # Cleanup old archives if needed
        self._cleanup_history()
    
    def _cleanup_history(self):
        """Maintain only max_history recent states."""
        archives = sorted(Path(self.history_dir).glob('*.json'))
        if len(archives) > self.max_history:
            for archive in archives[:-self.max_history]:
                archive.unlink()
    
    def update_state(self, new_state_data):
        """Update current state."""
        self._archive_state()
        
        self.current_state = {
            **self.current_state,
            **new_state_data,
            "timestamp": timestamp_manager.get_current_timestamp(),
            "user": timestamp_manager.get_current_user()
        }
        
        self._save_state()
        logging_manager.log_event(
            "system",
            "INFO",
            "State updated",
            new_state=new_state_data
        )
        
        return self.current_state
    
    def get_state(self):
        """Get current state."""
        return self.current_state
    
    def get_state_history(self):
        """Get state history."""
        history = []
        for archive in sorted(Path(self.history_dir).glob('*.json')):
            with open(archive, 'r') as f:
                history.append(json.load(f))
        return history

# Global instance
state_manager = StateManager()
