import React, { useState } from "react";
import Button from "./components/Button";

function App() {
  // Need to reach the backend with a function that allows me to upload a photo.
  const handleSubmit = (): void => {
    const fileInput = document.getElementById(
      "imageUpload"
    ) as HTMLInputElement | null;
    if (fileInput?.files?.[0]) {
      const file = fileInput.files[0];
    }
  };

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
      <Button onClick={handleSubmit}>Upload Image</Button>

      <Button onClick={() => {}}>Edit Image</Button>
    </div>
  );
}

export default App;
