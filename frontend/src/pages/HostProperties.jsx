import { useEffect, useState } from "react";
import axios from "../api/axios";

function HostProperties() {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        const response = await axios.get("/properties/host/");
        setProperties(response.data);
      } catch (error) {
        console.error("Failed to load properties", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProperties();
  }, []);

  if (loading) {
    return <p>Loading properties...</p>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>My Listings</h1>

      {properties.length === 0 && (
        <p>No properties yet. Add your first listing.</p>
      )}

      {properties.map((property) => (
        <div
          key={property.id}
          style={{
            border: "1px solid #ccc",
            padding: "12px",
            marginBottom: "10px",
            borderRadius: "6px",
          }}
        >
          <h3>{property.title}</h3>
          <p>
            {property.city}, {property.country}
          </p>
          <p>₹ {property.price_per_night} / night</p>
          <p>Status: {property.is_active ? "Active" : "Inactive"}</p>
        </div>
      ))}
    </div>
  );
}

export default HostProperties;
