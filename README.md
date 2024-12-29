# 🦅 Perplexity AI Query Interface

Welcome to the **Perplexity AI Query Interface** project! 🎉 This is a Python Flask web application that lets you interact with the Perplexity AI API in a user-friendly way. The app is designed to be simple, modular, and efficient, with both functionality and aesthetics in mind. 

## 🚀 Features

### 🌟 Core Functionalities
1. **Query the Perplexity AI API**:
   - Send customizable user and system prompts.
   - Append uploaded `.txt` file content to the query.

2. **File Upload**:
   - Upload `.txt` files and combine their content with your query prompt.

3. **Save API Responses**:
   - Automatically save the API response as a `.json` file with a timestamped filename (e.g., `query_result_yy-dd-mm-hh-mm.json`).

4. **Display Results**:
   - View formatted query results in a table for easy readability.
   - Access the raw JSON response for advanced debugging or sharing.

### 🖥️ Front-End Features
1. **Dark-Themed Interface**:
   - Sleek, modern design with a dark color palette.

2. **Results in a New Tab**:
   - Query results are displayed in a separate browser tab.

3. **Copy JSON Results**:
   - A "Copy" button allows you to quickly copy the raw JSON output.

### 🛠️ Robust Design
1. **Error Handling**:
   - Gracefully handles missing inputs and file upload errors.
   - Logs server-side issues to `app.log` for easy debugging.

2. **Modular Code**:
   - Clean structure with helper functions and well-organized routes.

---

## 🛠️ Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/perplexity-ai-query-interface.git
cd perplexity-ai-query-interface
2. Install Dependencies
Make sure you have Python installed (version 3.7+ recommended).
Install required packages:

pip install flask requests python-magic
3. Set Up Your API Key
Create a .env file in the project root and add your Perplexity AI API key:

PERPLEXITYAI_API_KEY=your_api_key_here
4. Run the Application

python app.py
Open your browser and navigate to http://127.0.0.1:5000/.
🎨 Screenshots
Home Page

Query Results

💡 How It Works
Enter a system prompt and user prompt on the home page.
(Optional) Upload a .txt file to append its content to your query.
Submit the query to get:
A formatted view of key results.
The raw JSON output.
Save the JSON file locally for further use.
🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

❤️ Acknowledgments
Thanks to Perplexity AI for the API.
Built with 🐍 Python and ❤️ Flask.