import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import { useParams } from "react-router-dom";

/** user box */
export default function User() {

    let { uid } = useParams();
    
    useEffect(() => {
        fetch(`http://127.0.0.1:5000/search/user/${uid}`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
    }, [])

    return (
        <Box sx={{ flexGrow: 1, alignItems: "end", justifyContent: "center" }}>
            
        </Box>
    );
}