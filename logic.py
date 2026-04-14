class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # Format: {(state, char): next_state}
        self.start_state = start_state
        self.accept_states = accept_states

    def get_simulation_path(self, input_string):
        """Returns a list of steps taken for visualization."""
        # Check for invalid characters in the input string
        for char in input_string:
            if char not in self.alphabet:
                return None, False, f"Error: Invalid character '{char}' in input string. Character not in alphabet: {', '.join(self.alphabet)}"

        path = []
        current_state = self.start_state
        path.append({"state": current_state, "char": None, "transition_id": None})

        for char in input_string:
            # Basic DFA logic: check if transition exists
            next_state = self.transitions.get((current_state, char))
            if next_state is None:
                return path, False, f"Rejected: No transition from state '{current_state}' for character '{char}'." # Rejected due to missing transition
            
            transition_id = f"{current_state}->{next_state}[label={char}]"
            current_state = next_state
            path.append({"state": current_state, "char": char, "transition_id": transition_id})
        
        is_accepted = current_state in self.accept_states
        return path, is_accepted, "Accepted" if is_accepted else "Rejected"