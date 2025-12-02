import streamlit as st
import random

st.set_page_config(page_title="Simple Shooting Game", layout="centered")

st.title("🔫 Simple Shooting Game Demo")
st.write("Try to shoot the moving target!")

# --- Initialize session state ---
if "target_pos" not in st.session_state:
    st.session_state.target_pos = random.randint(1, 5)

if "score" not in st.session_state:
    st.session_state.score = 0


# --- Display the target positions ---
cols = st.columns(5)

for i in range(5):
    if i + 1 == st.session_state.target_pos:
        cols[i].write("🎯")  # target
    else:
        cols[i].write("▫️")

# --- Shooting buttons ---
shot_col = st.columns(5)

for i in range(5):
    if shot_col[i].button(f"Shoot {i+1}"):
        if i + 1 == st.session_state.target_pos:
            st.success("🔥 HIT! +1 point")
            st.session_state.score += 1
        else:
            st.error("💨 Missed!")

        # Move target after each shot
        st.session_state.target_pos = random.randint(1, 5)

        st.rerun()

st.write(f"### Score: {st.session_state.score}")
