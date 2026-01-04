import { useEffect, useState } from "react";
import api from "../api/axios";

export default function HostDashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const access = localStorage.getItem("access");

    if (!access) {
      window.location.href = "/login";
      return;
    }

    api
      .get("properties/host/dashboard/")
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, []);

  const statusBadge = (status) => {
    const base = "px-3 py-1 rounded-full text-sm font-medium inline-block";

    if (status === "confirmed")
      return (
        <span className={`${base} bg-green-100 text-green-700`}>Confirmed</span>
      );

    if (status === "pending")
      return (
        <span className={`${base} bg-yellow-100 text-yellow-700`}>Pending</span>
      );

    if (status === "cancelled")
      return (
        <span className={`${base} bg-red-100 text-red-700`}>Cancelled</span>
      );

    return (
      <span className={`${base} bg-blue-100 text-blue-700`}>Completed</span>
    );
  };

  if (!data) {
    return (
      <div className="flex justify-center items-center h-screen text-xl">
        Loading dashboard...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-semibold mb-8">Host Dashboard</h1>

      {/* TOP STATS */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">Total Properties</p>
          <h2 className="text-3xl font-bold mt-2">{data.total_properties}</h2>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">Total Bookings</p>
          <h2 className="text-3xl font-bold mt-2">{data.total_bookings}</h2>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">Total Earnings</p>
          <h2 className="text-3xl font-bold mt-2">₹{data.total_earnings}</h2>
        </div>
      </div>

      {/* BOOKINGS TABLE */}
      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Recent Bookings</h2>

        {data.bookings.length === 0 ? (
          <p className="text-gray-500">No bookings yet.</p>
        ) : (
          <table className="w-full border-collapse">
            <thead>
              <tr className="border-b text-left text-gray-500">
                <th className="p-3">Property</th>
                <th className="p-3">Guest</th>
                <th className="p-3">Dates</th>
                <th className="p-3">Guests</th>
                <th className="p-3">Status</th>
                <th className="p-3">Total</th>
              </tr>
            </thead>

            <tbody>
              {data.bookings.map((booking) => (
                <tr key={booking.id} className="border-b hover:bg-gray-50">
                  <td className="p-3 font-medium">{booking.property_title}</td>

                  <td className="p-3">{booking.guest_email}</td>

                  <td className="p-3">
                    {booking.check_in} → {booking.check_out}
                  </td>

                  <td className="p-3">{booking.guests_count}</td>

                  <td className="p-3">{statusBadge(booking.status)}</td>

                  <td className="p-3 font-semibold">₹{booking.total_price}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
