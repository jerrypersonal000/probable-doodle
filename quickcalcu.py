import streamlit as st
from collections import deque

def shortest_path_to_range(A, B, C):
    queue = deque([(A, 0, [])])
    visited = set()
    operations = list(range(1, 10))
    max_limit = 30000  # Adjusted limit to 30000

    while queue:
        current, steps, path = queue.popleft()
        
        if B <= current <= C:
            return steps, path
        
        if abs(current) > max_limit:
            continue
        
        for op in operations:
            next_steps = [
                (current + op, f"{current} + {op} = {current + op}"),
                (current - op, f"{current} - {op} = {current - op}"),
                (current * op, f"{current} * {op} = {current * op}"),
                (current // op if op != 0 else None, f"{current} // {op} = {current // op}" if op != 0 else None)
            ]
            for result, desc in next_steps:
                if result is not None and result not in visited and abs(result) <= max_limit:
                    visited.add(result)
                    queue.append((result, steps + 1, path + [desc]))
    
    return -1, []

# Initialize session state variables if not already initialized
if 'A' not in st.session_state:
    st.session_state.A = 0
if 'B' not in st.session_state:
    st.session_state.B = 0
if 'C' not in st.session_state:
    st.session_state.C = 0

# Input fields
st.session_state.A = st.number_input("Enter the initial value A: ", step=1, value=st.session_state.A)
st.session_state.B = st.number_input("Enter the lower bound B: ", step=1, value=st.session_state.B)
st.session_state.C = st.number_input("Enter the upper bound C: ", step=1, value=st.session_state.C)

# Clear button
if st.button("Clear"):
    st.session_state.A = 0
    st.session_state.B = 0
    st.session_state.C = 0

steps, path = shortest_path_to_range(st.session_state.A, st.session_state.B, st.session_state.C)
if steps != -1:
    st.write(f"The shortest path from {st.session_state.A} to the range [{st.session_state.B}, {st.session_state.C}] takes {steps} steps")
    st.write("The steps are as follows:")
    for p in path:
        st.write(p)
else:
    st.write(f"No path found from {st.session_state.A} to the range [{st.session_state.B}, {st.session_state.C}].")
