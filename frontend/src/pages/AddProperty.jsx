import { useState } from "react";
import axios from "../api/axios";

export default function AddProperty() {
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("/properties/", {
        title,
        price_per_night: price,
      });

      alert("Property created successfully");
    } catch (err) {
      console.error(err);
      alert("Error creating property");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Add Property</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Title</label>
          <br />
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div style={{ marginTop: "10px" }}>
          <label>Price per night</label>
          <br />
          <input
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
        </div>

        <button style={{ marginTop: "15px" }} type="submit">
          Save
        </button>
      </form>
    </div>
  );
}
