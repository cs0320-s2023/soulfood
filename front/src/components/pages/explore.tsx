import * as React from "react";
import Box from "@mui/material/Box";
import { Button, Typography } from "@mui/material";
import BusinessCard from "../businessCard";

export default function Explore() {
  return (
    <Box sx={{ flexGrow: 1, alignItems: "end", justifyContent: "center" }}>
        <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>Explore</Typography>
        <BusinessCard />
    </Box>
  );
}
