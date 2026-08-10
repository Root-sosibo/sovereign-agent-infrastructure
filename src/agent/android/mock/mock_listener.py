#!/usr/bin/env python3
import sys

INTENT_NAMES = {
    1: "Focus Mode ENABLED",
    2: "Sleep Mode ENABLED",
    3: "Silent Mode ENABLED",
    4: "All modes DISABLED"
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No intent code provided.")
        sys.exit(1)
    
    code = int(sys.argv[1])
    action = INTENT_NAMES.get(code, "Unknown action")
    
    print("=" * 50)
    print(f"Received intent: {code}")
    print(f"Action state: {action}")
    print("=" * 50)
