# Rule-Based AI Chatbot 🤖

A lightweight, robust, and interactive Python chatbot designed to demonstrate smart control flow, efficient input normalization, and clean continuous conversation loops.

Building this project was an immensely enjoyable experience! It provided a hands-on opportunity to transform straightforward programming logic into a functional, resilient conversational agent while solving real-world coding challenges along the way.

---

## ✨ Features & Architecture Highlights

* **Input Normalization & Hygiene**: User input can be noisy and unpredictable. By applying `.strip().lower()`, the chatbot normalizes all incoming queries—eliminating whitespace bugs and handling capitalization seamlessly.
* **$O(1)$ Intent Lookup with `.get()`**: Replacing lengthy, complex `if-else` chains with Python's dictionary `.get()` method completely streamlined the codebase. It simplified logic lookup, eliminated nested conditional bottlenecks, and enabled instant $O(1)$ response fetching with built-in fallback handling.
* **Continuous Interactive Loop**: Utilizes a smooth `while True` loop that keeps the pilot active and responsive until a specific exit command (`exit`, `bye`, `quit`) is triggered, ensuring a seamless chat experience without unexpected crashes.

---

## 🛠️ Tech Stack & Requirements

* **Language**: Python 3.8+
* **Dependencies**: Python Standard Library (No external modules required)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ahmedmaheraga-ctrl/Project-1-Rule-Based-AI-Chatbot..git
cd Project-1-Rule-Based-AI-Chatbot..
```

### 2. Run the Chatbot
```bash
python main.py
```

---

## 💻 Example Usage

```text
=========================================================
          Welcome to the Rule-Based AI Chatbot!
      Type 'exit', 'bye', or 'quit' to end the chat
=========================================================

You: HELLO  
Bot: "Hi there! What can I do for you?

You: how are you
Bot: I'm just a chatbot, but I'm here to help you!"

You: random text
Bot: I'm sorry, I didn't quite understand that. Could you rephrase?

You: bye
Bot: Goodbye! Have a great day!
```

---

## 🧠 Engineering Lessons & Reflections

* **Joy of Building**: Crafting this project from scratch was both exciting and rewarding. Seeing raw logic turn into a fluid interactive agent made the build process very fulfilling.
* **Why `.get()` Beat `if-else`**: Shifting to dynamic dictionary lookups (`responses.get(user_input, fallback)`) not only made the code execution faster ($O(1)$ vs $O(N)$ comparisons) but also drastically improved readability and scalability for future intent rules.
* **Resilient Loop Design**: Structuring the session around a controlled `while` loop guaranteed continuous user engagement without premature terminations or unhandled exceptions.
