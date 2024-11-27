import React, { useState } from "react";
import Button from "./components/Button";

function App() {
  // Function to handle the edit that sends the uploaded photo to the backend.
  async function handleEdit() {
    if (!file) {
      throw new Error("Something went wrong, try again later!");
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
      const res = await fetch("http://localhost:8000/api/edit-image", {
        method: "POST",
        body: formData,
      });
    } catch (error) {
      throw new Error("Request couldn't be complete, please try again later!");
    }
  }

  //  Handle change of image when you upload it to the frontend
  interface FileInputEvent extends React.ChangeEvent<HTMLInputElement> {}

  const handleChange = (e: FileInputEvent): void => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  // State for files that get added  to the frontend
  const [file, setFile] = useState<File | null>(null);

  return (
    <div>
      <input
        type="file"
        accept="image/*"
        id="imageUpload"
        onChange={handleChange}
      />
      {/* File added only if there is a file to be displayed from the state */}
      {file && (
        <img src={URL.createObjectURL(file)} alt={file.name} width={300} />
      )}

      <Button onClick={handleEdit}>Edit Image</Button>
    </div>
  );
}

export default App;
