import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import HostDashboard from "./pages/HostDashboard";
import HostProperties from "./pages/HostProperties";
import AddProperty from "./pages/AddProperty";

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route path="/host/dashboard" element={<HostDashboard />} />
      <Route path="/host/properties" element={<HostProperties />} />
      <Route path="/host/add-property" element={<AddProperty />} />
    </Routes>
  );
}
