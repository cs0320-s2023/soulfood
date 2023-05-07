import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

/** 404 server error appearance, overrides default */
export default function NotFound() {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Typography variant="h2">
        404: Page Not Found
      </Typography>
    </Box>
  );
}
