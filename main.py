# main.py

import streamlit as st
import requests
from Agents import Agents
from Tasks import Tugas

# Fungsi untuk mendapatkan respons dari API
def get_chat_response(user_input):
    url = "https://api.ryzendesu.vip/api/ai/blackbox"
    params = {"chat": user_input, "options": "gpt-4o"}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "Tidak ada respons")
        else:
            return f"Terjadi kesalahan saat menghubungi API. Status: {response.status_code}"
    except Exception as e:
        return f"Terjadi kesalahan dalam memproses JSON: {str(e)}"

# Kelas Crew untuk mengelola agen dan tugas
class Crew:
    def __init__(self, agents, tasks, process):
        self.agents = agents
        self.tasks = tasks
        self.process = process

    def kickoff(self):
        # Menyusun deskripsi eksekusi agen dan tugas
        result = f"Menjalankan proses {self.process} dengan agen: {', '.join([agent.name for agent in self.agents])}"
        result += f"\nTugas yang sedang dijalankan: {', '.join(self.tasks)}"
        return result

# Menangani logika utama aplikasi
def main():
    st.markdown('<h1>Selamat datang di chatbot dengan AI TKJ 2!</h1>', unsafe_allow_html=True)

    # Memasukkan input pengguna
    user_input = st.text_input('Sila masukkan pertanyaan Anda:')
    insert = st.button("TANYAKAN BAE LANGSONG")

    # Menangani apabila input diberikan
    if insert and user_input:
        # Membuat instance agen dan tugas
        agents = [Agents().Agent1(), Agents().Agent2()]  # Mendapatkan agen dengan role "programming handal"
        tasks = [Tugas().task1(), Tugas().task2()]  # Menjalankan tugas yang relevan

        # Membuat instance Crew dengan agen dan tugas
        crew = Crew(agents=agents, tasks=tasks, process="sequential")

        # Menampilkan hasil kickoff
        st.markdown(crew.kickoff())

        # Mendapatkan respons dari API
        response = get_chat_response(user_input)

        # Menampilkan respons chatbot
        st.write(f"**Chatbot**: {response}")

if __name__ == "__main__":
    main()
