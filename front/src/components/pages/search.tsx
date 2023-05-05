import React, { useState } from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';
import { ContentCardData } from "../Card";
import ContentCard from "../Card";

export default function Search() {
  const [queryMode, setQueryMode] = useState("");
  const [query, setQuery] = useState("");
  const [searchData, setSearchData] = useState<Array<ContentCardData> | undefined>();
  const [error, setError] = useState("");

  function handleSearch() {
    setError("");
    if (queryMode === "") {
      alert("Please specify a query mode.");
    } 
    let url = "http://127.0.0.1:5000/";
    switch(queryMode) {
      case "label":
        url += `search/label/${query}`;
        break;
      case "keyword":
        url += `search/post/${query}`
        break;
      case "user":
        url += `search/post/${query}`
        break;
      default:
        alert("default case reached");
    }
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data['error'] !== undefined) {
          setError(data['error']);
          setSearchData(undefined);
        } else {
          setSearchData(data);
        }
      })
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>Search</Typography>
      <Grid container spacing={2} alignItems="center" justifyContent="center" sx={{ marginBottom: 4 }}>
        <Grid item xs={8}>
          <TextField
            label="Search"
            fullWidth
            variant="outlined"
            value={query}
            
            onChange={(e) => setQuery(e.target.value)}
          />
        </Grid>
        <Grid item xs={2}>
          <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">Query</InputLabel>
            <Select
              labelId="query-label"
              id="query-select"
              value={queryMode}
              label="Query"
              onChange={(e) => setQueryMode(e.target.value)}
            >
              <MenuItem value={"label"}>Label</MenuItem>
              <MenuItem value={"keyword"}>Keyword</MenuItem>
              <MenuItem value={"user"}>User</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={2}>
          <Button onClick={handleSearch} color="primary" variant="contained" sx={{flexGrow: 1}} size="large">Search</Button>
        </Grid>
      </Grid>
      {error !== "" && <Alert sx={{ marginBottom: 2 }} severity="error" onClose={() => {setError("")}}>{error}</Alert>}
      <Grid container spacing={2}>
          {searchData !== undefined && searchData.map((data) => {
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
