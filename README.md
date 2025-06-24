<header>
  <h1>Automated Metadata Generation</h1>
  <p>Extract metadata from PDF, DOCX, TXT, and OCR files using NLP and chunk-based summarization</p>
</header>

<main>
  <h2>📌 Project Overview</h2>
  <p>
    Designed for scalability and semantic richness, this system helps improve document discoverability, classification, and analysis in any workflow. It delivers structured metadata including summaries, keywords, language detection, and text statistics — all accessible through a user-friendly Streamlit interface.
  </p>
  <h4>🔧 Key Features:</h4>
  <ul>
    <li>Language detection</li>
    <li>Chunked text summarization using transformer models</li>
    <li>Keyword extraction via TF-IDF</li>
    <li>Support for image-based documents using Tesseract OCR</li>
    <li>A simple and interactive Streamlit web app interface</li>
  </ul>

  <h2>✨ Features</h2>
  <ul>
    <li>Extract metadata like <strong>File Name, Extracted Date and Time, Language, Summary, Keywords, number of characters and words</strong></li>
    <li>Supports <code>.pdf</code>, <code>.docx</code>, <code>.txt</code>, and image-based OCR documents</li>
    <li>Summarization powered by <code>distilbart-cnn</code> and intelligent chunk selection</li>
    <li>Displays extraction in a clean, accessible web UI built with Streamlit</li>
    <li>Lightweight deployment using Python + Pip + Streamlit</li>
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
      <pre><code>streamlit run app/app.py</code></pre>
    </li>
  </ol>
  <p>Now upload your document and watch the metadata get auto-generated in seconds!</p>

  <h2>🧠 Assumptions & Enhancements</h2>
  <ul>
    <li>The document must contain a minimum of ~300 characters for meaningful summarization.</li>
    <li>You can add files upto 200 MB.</li>
    <li>To maintain a balance between <b>accuracy and performance</b>, the text is processed in chunks, with a default setting of <code>max_chunks = 3</code>. This limits the number of segments sent through the summarization model, helping reduce latency while still capturing key content from various parts of the document.</li>
    <li>This model can be easily swapped with a domain-specific or fine-tuned variant (e.g., medical, legal, academic) depending on the target use case, offering flexibility for customization.</li>
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
  Made with ❤️ by Prachi · <a href="https://github.com/EspressoPatron/Automated_Metadata_Generation" target="_blank">GitHub Repo</a>
</footer>

</body>