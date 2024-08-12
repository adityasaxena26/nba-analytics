import os
import webbrowser
import toml


def run_streamlit_app():
    os.system('streamlit run src/ui/dashboard.py')


if __name__ == "__main__":
    run_streamlit_app()
