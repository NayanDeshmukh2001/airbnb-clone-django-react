import { useState } from "react";
import api from "./api/axios";

function CreateBooking() {
  const [propertyId, setPropertyId] = useState("");

  const book = async () => {
    try {
      await api.post("bookings/create/", {
        property: propertyId,
        check_in: "2026-01-10",
        check_out: "2026-01-12",
      });
      alert("Booking created");
    } catch {
      alert("Booking failed");
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Guest: Create Booking</h2>
      <input
        className="w-full border p-2 mb-3 rounded"
        placeholder="Property ID"
        onChange={(e) => setPropertyId(e.target.value)}
      />
      <button
        className="w-full bg-purple-600 text-white py-2 rounded"
        onClick={book}
      >
        Book Property
      </button>
    </div>
  );
}

export default CreateBooking;
