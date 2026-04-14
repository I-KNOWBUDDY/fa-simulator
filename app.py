import streamlit as st
import graphviz
import time
import pandas as pd
from logic import FiniteAutomaton

st.set_page_config(page_title="FA Simulator", layout="wide")

st.title("⚙️ Finite Automata Visualizer")
st.markdown("Build, simulate, and visualize DFA/NFA processing step-by-step.")

# --- SIDEBAR INPUTS ---
st.sidebar.header("1. Define Automaton")
states_input = st.sidebar.text_input("States (comma separated)", "q0, q1, q2")
alphabet_input = st.sidebar.text_input("Alphabet", "0, 1")
start_state = st.sidebar.text_input("Start State", "q0")
accept_states_input = st.sidebar.text_input("Accepting States", "q2")

st.sidebar.header("2. Define Transitions")
st.sidebar.caption("Format: current_state,char,next_state (One per line)")
transitions_raw = st.sidebar.text_area("Transitions", "q0,0,q0\nq0,1,q1\nq1,0,q1\nq1,1,q2\nq2,0,q2\nq2,1,q2")

st.sidebar.markdown("---")
st.sidebar.info("Current Version: DFA Simulator")

# --- DATA PARSING ---
states = [s.strip() for s in states_input.split(",")]
alphabet = [a.strip() for a in alphabet_input.split(",")]
accept_states = [s.strip() for s in accept_states_input.split(",")]
transitions = {}
for line in transitions_raw.strip().split("\n"):
    if line:
        curr, char, nxt = line.split(",")
        transitions[(curr.strip(), char.strip())] = nxt.strip()

fa = FiniteAutomaton(states, alphabet, transitions, start_state, accept_states)

# --- SIMULATION SECTION ---
st.subheader("🚀 Simulation")
input_string = st.text_input("Enter Input String", "101")
run_btn = st.button("Run Simulation")

if run_btn or 'current_step' in st.session_state:
    path, accepted, status_message = fa.get_simulation_path(input_string)
    
    if path is None: # This indicates an invalid character error or other early exit
        st.error(status_message)
        if 'current_step' in st.session_state:
            del st.session_state.current_step
        st.stop() # Stop further execution of the script for this run

    # Track steps in session state
    if run_btn:
        st.session_state.current_step = 0

    col1, col2 = st.columns([2, 1])

    with col1:
        # Drawing the Graph
        dot = graphviz.Digraph(format='svg')
        dot.attr(rankdir='LR')

        current_info = path[st.session_state.current_step]
        
        for s in states:
            # Highlight current state
            color = "yellow" if s == current_info['state'] else "white"
            shape = "doublecircle" if s in accept_states else "circle"
            dot.node(s, shape=shape, style="filled", fillcolor=color)

        # ... (rest of the code for highlighting edges and transition table)


        for (curr, char), nxt in transitions.items():
            edge_attrs = {}
            # Check if this is the active transition to highlight
            if current_info["char"] == char and current_info["transition_id"] == f"{curr}->{nxt}[label={char}]":
                edge_attrs = {"color": "red", "penwidth": "2.0"}
            dot.edge(curr, nxt, label=char, **edge_attrs)

        st.graphviz_chart(dot)

        st.subheader("Transition Table")
        
        # Create a DataFrame to hold the transition table
        df_display = pd.DataFrame(index=states, columns=alphabet)
        for (current, char), next_state in transitions.items():
            df_display.loc[current, char] = next_state
        
        # Apply highlighting
        if st.session_state.current_step > 0 and current_info["char"] is not None:
            prev_state_for_transition = path[st.session_state.current_step - 1]["state"]
            char_for_transition = current_info["char"]

            def style_specific_cell(df):
                # Create a DataFrame of empty strings
                styles = pd.DataFrame('', index=df.index, columns=df.columns)
                # Set background-color for the specific cell
                if prev_state_for_transition in df.index and char_for_transition in df.columns:
                    styles.loc[prev_state_for_transition, char_for_transition] = 'background-color: yellow'
                return styles

            styled_df = df_display.style.apply(style_specific_cell, axis=None)
            st.dataframe(styled_df, use_container_width=True)
        else:
            st.dataframe(df_display, use_container_width=True)


    with col2:
        st.write(f"**Step:** {st.session_state.current_step} / {len(path)-1}")
        if st.session_state.current_step < len(path)-1:
            if st.button("Next Step ➡️"):
                st.session_state.current_step += 1
                st.rerun()
        else:
            if accepted:
                st.success(f"✅ String {status_message}")
            else:
                st.error(f"❌ String {status_message}")
        
        if st.button("Reset"):
            st.session_state.current_step = 0
            st.rerun()