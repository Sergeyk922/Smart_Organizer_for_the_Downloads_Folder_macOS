#Smart AI Organizer (macOS)

An automated file management tool that uses **Local AI** to keep your Downloads folder organized. Unlike traditional organizers, this script "understands" what your files are about by analyzing their names using **Ollama** and **Llama 3**.

## Key Features
- **Hybrid Logic**: Uses fast dictionary mapping for simple files (images, archives) and AI for complex documents (PDFs, Docx).
- **Privacy First**: Powered by **Ollama**, meaning all file analysis happens locally on your Mac. No data is sent to the cloud.
- **Smart Categorization**: Automatically detects if a document belongs to "Work", "Taxes", "Study", or "Finance" based on its semantic meaning.
- **macOS Optimized**: Designed specifically for the macOS file structure and hidden file handling.

## Prerequisites

To run this project, you need:

1. **Python 3.x** installed on your Mac.
2. **Ollama**: The engine for running local LLMs.
   - Download it from [ollama.com](https://ollama.com).
   - After installation, run `ollama pull llama3` in your terminal.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sergeyk922/Smart_Organizer_for_the_Downloads_Folder_macOS_Ollama_AI.git](https://github.com/Sergeyk922/Smart_Organizer_for_the_Downloads_Folder_macOS_Ollama_AI.git)
   cd Smart_Organizer_for_the_Downloads_Folder_macOS_Ollama_AI
