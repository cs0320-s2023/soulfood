import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';

export default function Search() {
  const [queryMode, setQueryMode] = React.useState("");
  const [query, setQuery] = React.useState("");

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>Search</Typography>
      <Grid container spacing={2} alignItems="center" justifyContent="center">
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
              <MenuItem value={"location"}>Location</MenuItem>
              <MenuItem value={"user"}>User</MenuItem>
              <MenuItem value={"restaurant"}>Restaurant</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={2}>
          <Button color="primary" variant="contained" sx={{flexGrow: 1}} size="large">Search</Button>
        </Grid>
      </Grid>
    </Box>
  );
}
