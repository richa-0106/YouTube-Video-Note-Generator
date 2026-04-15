import React, { useState } from "react";
import axios from "axios";

function UrlInput() {

  const [url, setUrl] = useState("");
  const [notes, setNotes] = useState("");
  const [loading, setLoading] = useState(false);

  const generateNotes = async () => {

    if (!url) {
      alert("Enter URL first");
      return;
    }

    setLoading(true);
    setNotes("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/generate-notes",
        { url: url }
      );

      setNotes(response.data.notes);

    } catch (error) {
      console.error(error);
      alert("Error generating notes");
    }

    setLoading(false);
  };

  return (
    <div>

      <input
        type="text"
        placeholder="Paste YouTube URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "400px", padding: "10px" }}
      />

      <button onClick={generateNotes} style={{ marginLeft: "10px" }}>
        Generate Notes
      </button>

      {loading && <p>⏳ Processing...</p>}

      {notes && (
        <div style={{ marginTop: "20px" }}>
          <h3>📄 Notes</h3>
          <pre>{notes}</pre>
        </div>
      )}

    </div>
  );
}

export default UrlInput;