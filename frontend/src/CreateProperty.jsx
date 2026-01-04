import { useState } from "react";
import api from "./api/axios";

function CreateProperty() {
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");

  const createProperty = async () => {
    try {
      await api.post("properties/", {
        title,
        description: "Nice place",
        city: "Pune",
        address: "Baner",
        price_per_night: price,
        max_guests: 2,
      });
      alert("Property created");
    } catch {
      alert("Only host can create property");
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Host: Create Property</h2>
      <input
        className="w-full border p-2 mb-3 rounded"
        placeholder="Title"
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        className="w-full border p-2 mb-3 rounded"
        placeholder="Price"
        onChange={(e) => setPrice(e.target.value)}
      />
      <button
        className="w-full bg-green-600 text-white py-2 rounded"
        onClick={createProperty}
      >
        Create Property
      </button>
    </div>
  );
}

export default CreateProperty;
