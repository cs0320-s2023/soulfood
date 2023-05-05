import React, { useState, useEffect } from "react";
import Box from "@mui/material/Box";
import { Typography } from "@mui/material";
import ContentCard from "../Card";
import Grid from "@mui/material/Grid";
import { ContentCardData } from "../Card";
import { useUser } from "../dashboard";

export default function Explore() {
  const [exploreData, setExploreData] = useState<Array<ContentCardData>>([]);
  const { currentUser } = useUser();

  useEffect(() => {
    console.log('user:')
    console.log(currentUser);
    if (currentUser !== null) {
      // `http://127.0.0.1:5000/recommend/${}/12`
      fetch(`http://127.0.0.1:5000/recommend/1/12`)
        .then((res) => res.json())
        .then((data) => {
          setExploreData(data);
        });
    }
  }, [currentUser]);

  
  return (
    <Box sx={{ flexGrow: 1, alignItems: "end", justifyContent: "center" }}>
        <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>Explore</Typography>
        <Grid container spacing={2}>
          {exploreData.map((data) => {
            return (
              <Grid item xs={4} key={data.pid}>
                <ContentCard data={data}/>
              </Grid>
            );
          })}
        </Grid>
    </Box>
  );
}
