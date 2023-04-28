import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Dashboard from "./components/dashboard";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NotFound from "./components/pages/404";
import Home from "./components/pages/home";
import Explore from "./components/pages/explore";
import Search from "./components/pages/search";
import Profile from "./components/pages/profile";
import Login from "./components/pages/login";
import Signup from "./components/pages/signup";

const mdTheme = createTheme({
  palette: {
    primary: {
      main: "#000",
    },
    secondary: {
      main: "#fff",
    }
  },
});

function App() {
  return (
    <ThemeProvider theme={mdTheme}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Dashboard />}>
            <Route path="home" element={<Home />} />
            <Route path="explore" element={<Explore />} />
            <Route path="search" element={<Search />} />
            <Route path="profile" element={<Profile />} />
            <Route path="*" element={<NotFound />} />
          </Route>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
