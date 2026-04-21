# ⚙️ Finite Automata Visualizer & Simulator

An interactive web application to visually simulate how a **Deterministic Finite Automaton (DFA)** processes input strings.
Built as an educational tool to simplify concepts from **Theory of Automata and Formal Languages (TAFL)**.

---

## 🚀 Overview

This project is a **visualization-based web application** where users can:

* Design their own finite automaton
* Simulate input strings step-by-step
* Observe how states change during computation

It helps bridge the gap between **theoretical state diagrams** and **practical execution**.

---

## ✨ Key Features

### 🔧 Custom Automaton Design

* Define:

  * States (e.g., q0, q1)
  * Input alphabet (e.g., 0, 1)
  * Start state
  * Accept states
* Add transition rules using simple inputs

---

### ▶️ Step-by-Step Simulation

* Process input strings one symbol at a time
* Use a **Next Step** button to move forward gradually

---

### 🎯 Dual Highlighting Visualization

* **Current State Highlighting (Yellow)**
  Shows the active state during simulation

* **Transition Highlighting (Red)**
  Displays the exact edge/path taken for each symbol

---

### 📊 Synchronized Transition Table

* Dynamic table updates during simulation
* Highlights the exact transition being used

---

### ⚠️ Error Handling

* Detects invalid symbols (not part of the alphabet)
* Ensures correctness during execution

---

### ✅ Final Result

* Clearly displays:

  * **Accepted** → ends in an accepting state
  * **Rejected** → otherwise

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Streamlit** → Interactive UI
* **Graphviz** → State diagram visualization
* **Pandas** → Transition table management

---

## 📥 Installation & Usage

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/fa-simulator.git
```

### 2. Install Dependencies

```bash
pip install streamlit graphviz pandas
```

### 3. Run Application

```bash
streamlit run app.py
```

---

## 📖 How to Use

### 1. Define the Machine

* Enter:

  * States (e.g., q0, q1)
  * Alphabet (e.g., 0, 1)
  * Start state
  * Accept states

---

### 2. Add Transitions

Format:

```
current_state, input_symbol, next_state
```

Example:

```
q0,0,q1
q1,1,q0
```

---

### 3. Run Simulation

* Enter input string
* Click **Run Simulation**

---

### 4. Analyze Execution

* Use **Next Step** to:

  * Track state changes
  * See highlighted transitions
  * Follow table updates
