import streamlit as st
import requests

def get_reandom_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
      
        if response.status_code == 200:
            joke = response.json()
            return joke["setup"], joke["punchline"]
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "No joke available", ""


def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to get a random joke.")
    if st.button("Get Random Joke"):
        setup, punchline = get_reandom_joke()
        st.write(setup)
        st.success(punchline)

    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a href='https://github.com/Hammad8288'>Hammad Ahmed</a> using Streamlit</p>
    </div>
""", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()