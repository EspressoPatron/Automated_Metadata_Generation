<header>
  <h1>Automated Metadata Generation</h1>
  <p>Extract rich metadata from PDF, DOCX, TXT, and OCR files using NLP and chunk-based summarization</p>
</header>

<main>
  <h2>📌 Project Overview</h2>
  <p>
    This project enables automated generation of metadata for unstructured document types. It supports PDFs, DOCX, TXT, and scanned image files using OCR. Designed for scalability and semantic richness, this system helps improve document discoverability and analysis in any workflow.
  </p>

  <h2>✨ Features</h2>
  <ul>
    <li>📝 Extract metadata like <strong>Title, Author, Summary, Keywords, and Document Type</strong></li>
    <li>📄 Supports <code>.pdf</code>, <code>.docx</code>, <code>.txt</code>, and image-based OCR documents</li>
    <li>🔍 Summarization powered by <code>distilbart-cnn</code> and intelligent chunk selection</li>
    <li>📊 Displays extraction in a clean, accessible web UI built with Streamlit</li>
    <li>📦 Lightweight deployment using Python + Pip + Streamlit</li>
  </ul>

  <h2>🚀 How to Run the Project Locally</h2>
  <p><strong>Requirements:</strong> Python 3.9+, pip, virtualenv (optional)</p>

  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/EspressoPatron/Automated_Metadata_Generation</code></pre>
    </li>
    <li>Navigate into the project folder:
      <pre><code>cd Automated_Metadata_Generation</code></pre>
    </li>
    <li>Install dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Launch the Streamlit app:
      <pre><code>streamlit run app.py</code></pre>
    </li>
  </ol>
  <p>Now upload your document and watch the metadata get auto-generated in seconds!</p>

  <h2>🧠 Assumptions & Enhancements</h2>
  <ul>
    <li>The document must contain a minimum of ~300 characters for meaningful summarization.</li>
    <li>Only the first <code>max_chunks = 3</code> are used to reduce response time while ensuring quality output.</li>
    <li>Uses a pretrained summarizer; model can be swapped with custom fine-tuned variants for domain-specific use.</li>
    <li>Supports scanned image OCR using <code>pytesseract</code> (make sure Tesseract is installed on system).</li>
  </ul>

  <h2>💡 Future Possibilities</h2>
  <ul>
    <li>Integrate with Elasticsearch for metadata indexing and search</li>
    <li>Add more LLM-powered enhancements like named entity extraction or auto-tagging</li>
    <li>Deploy with Docker or Hugging Face Spaces for broader access</li>
  </ul>
</main>

<footer>
  Made with ❤️ by EspressoPatron · <a href="https://github.com/EspressoPatron/Automated_Metadata_Generation" target="_blank">GitHub Repo</a>
</footer>

</body>