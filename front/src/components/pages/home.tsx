import * as React from "react";
import Box from "@mui/material/Box";
import { Button, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

/** home page */

export default function Home() {

    const navigate = useNavigate();

    // home page appearance, which includes a short welcome and a button to the explore page (where recommendations are taken)
    return (
        <Box sx={{ flexGrow: 1, alignItems: 'end', justifyContent: 'center' }}>
            <Typography variant="h2" sx={{ fontWeight: 'bold' }}>
                Welcome to SoulFood
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: 'lighter', mt: 2, mb: 2 }}>
                Business reviews, by your friends, for you.
            </Typography>
            <Button role="exploreButton" variant="contained" color="secondary" onClick={() => navigate('/explore')}>
                Explore
            </Button>
        </Box>
    );
}