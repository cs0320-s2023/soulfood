import * as React from "react";
import Box from "@mui/material/Box";
import { Button, Typography } from "@mui/material";

export default function Home() {
    return (
        <Box sx={{ flexGrow: 1, alignItems: 'end', justifyContent: 'center' }}>
            <Typography variant="h2" sx={{ fontWeight: 'bold' }}>
                Welcome to SoulFood
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: 'lighter', mt: 2, mb: 2 }}>
                Business reviews, by your friends, for you.
            </Typography>
            <Button variant="contained" color="secondary">
                Explore
            </Button>
        </Box>
    );
}