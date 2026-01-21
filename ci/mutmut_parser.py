#!/usr/bin/env python3
"""
Script to parse mutmut results and display details for each mutation.
"""
import subprocess
import re
import sys


def execute_command(cmd):
    """Execute a shell command and return stdout."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {cmd}", file=sys.stderr)
        print(f"Error message: {e.stderr}", file=sys.stderr)
        return None


def parse_mutation_ids(output):
    """
    Parse mutmut results output and extract mutation IDs.
    
    Example line:
    sample_web_svc.web.user_controller.xǁUserControllerǁget_users__mutmut_10: survived
    
    Returns list of mutation IDs like:
    ['sample_web_svc.web.user_controller.xǁUserControllerǁget_users__mutmut_10', ...]
    """
    mutation_ids = []
    
    # Pattern to match lines with mutation IDs
    # Captures everything before the colon
    pattern = r'^(.+?):\s+\w+$'
    
    for line in output.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
            
        match = re.match(pattern, line)
        if match:
            mutation_id = match.group(1).strip()
            mutation_ids.append(mutation_id)
    
    return mutation_ids


def show_mutation_details(mutation_id):
    """Execute 'mutmut show' for a given mutation ID and return the output."""
    cmd = f"mutmut show {mutation_id}"
    return execute_command(cmd)


def main():
    print("=" * 80)
    print("Fetching mutmut results...")
    print("=" * 80)
    print()
    
    # Execute mutmut results
    results_output = execute_command("mutmut results")
    
    if results_output is None:
        print("Failed to execute 'mutmut results'", file=sys.stderr)
        sys.exit(1)
    
    # Parse mutation IDs
    mutation_ids = parse_mutation_ids(results_output)
    
    if not mutation_ids:
        print("No mutation IDs found in output.")
        sys.exit(0)
    
    print(f"Found {len(mutation_ids)} mutation(s)\n")
    
    # Show details for each mutation
    for i, mutation_id in enumerate(mutation_ids, 1):
        print("=" * 80)
        print(f"Mutation {i}/{len(mutation_ids)}: {mutation_id}")
        print("=" * 80)
        
        details = show_mutation_details(mutation_id)
        
        if details:
            print(details)
        else:
            print(f"Failed to retrieve details for: {mutation_id}", file=sys.stderr)
        
        print()  # Add blank line between mutations


if __name__ == "__main__":
    main()
