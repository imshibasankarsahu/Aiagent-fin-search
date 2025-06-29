
# 🧠 AI Finance & News Assistant

This is a real-world Generative AI project (Day 4 of 30-Day GenAI Challenge) that combines financial insights and web search into one intelligent assistant using:

- **Agno Agents**
- **Groq LLMs** (`llama3-70b-8192`)
- **YFinanceTools** for stock data
- **DuckDuckGoTools** for latest news
- **Streamlit** for user interface

---

## 💡 Features

- Ask any question related to finance or news (e.g., "Tesla stock update", "NVIDIA news")
- Agents automatically pick the correct tool to fetch data
- Finance agent shows stock data using tables
- Web agent fetches the latest news and includes source links

---

## 📁 Requirements

Install the required libraries:

```bash
pip install streamlit agno python-dotenv
```

Set your `.env` file:

```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## 🚀 How to Run

```bash
streamlit run just1.py
```

---

## 📄 Code Snippet

```python
query = st.text_input("Ask anything...")
if query:
    result = agent_team.run(message=query)
    st.markdown(result.content)
```

---

## 📌 Credits

This is part of my **30 Days of GenAI Real-World Projects** initiative.  
Connect with me on [LinkedIn](https://www.linkedin.com/) if you're working on GenAI too!

---

## 🔖 Tags

`#GenerativeAI` `#Streamlit` `#Groq` `#FinanceAI` `#AIProjects` `#Python` `#OpenSource` `#LLMs`
