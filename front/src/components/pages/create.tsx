import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import { Grid, Typography } from "@mui/material";
import FormControl from "@mui/material/FormControl";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Alert from "@mui/material/Alert";

import { useUser } from "../dashboard";
import {
  doc,
  setDoc,
  updateDoc,
  arrayUnion,
  arrayRemove,
} from "firebase/firestore";
import { db } from "../../firebase/firebaseConfig";

/** create page for a new post */

// post content
interface FormValues {
  title: string;
  url: string;
  description: string;
  tags: string[];
}

const initialFormValues = {
  title: "",
  url: "",
  description: "",
  tags: [],
};

export default function Create() {
  const [formValues, setFormValues] =
    React.useState<FormValues>(initialFormValues);
  const [error, setError] = React.useState("");

  const { currentUser, postCount, setPostCount } = useUser();

  async function handleSubmit() {
    // ensure no empty values
    if (
      formValues.title === "" ||
      formValues.url === "" ||
      formValues.description === "" ||
      formValues.tags.length === 0
    ) {
      setError("Missing values.");
    }
    if (currentUser !== null && currentUser !== undefined) {
      // creates post
      const pid = postCount.toString()
      await setDoc(doc(db, "posts", pid), {
        collected_by: [],
        liked_by: [],
        labels: formValues.tags,
        paragraph: formValues.description,
        photo: formValues.url,
        title: formValues.title,
        pid: pid,
        posted_by: currentUser?.uid,
      });
      await updateDoc(doc(db, "profiles", currentUser.uid.toString()), {
        posted: arrayUnion(pid)
      });
      console.log("Post created");
      console.log(postCount);
      setPostCount(postCount + 1)
      setError("");
      setFormValues(initialFormValues);
    }
  }

  // appearance of create page, which includes four field boxes: title, url, description, and tags (pre-chosen and can be clicked & added)
  return (
    <Box sx={{ flexGrow: 1, alignItems: "end", justifyContent: "center" }}>
      <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>
        Create
      </Typography>
      <Grid
        container
        spacing={2}
        alignItems="center"
        justifyContent="left"
        sx={{ marginBottom: 4 }}
      >
        <Grid item xs={4}>
          <TextField
            value={formValues.title}
            onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
              setFormValues({
                ...formValues,
                title: event.target.value,
              });
            }}
            label="Title"
            variant="outlined"
            fullWidth
          />
        </Grid>
        <Grid item xs={8}></Grid>
        <Grid item xs={6}>
          <TextField
            value={formValues.url}
            onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
              setFormValues({
                ...formValues,
                url: event.target.value,
              });
            }}
            label="Image URL"
            variant="outlined"
            fullWidth
          />
        </Grid>
        <Grid item xs={6}></Grid>
        <Grid item xs={12}>
          <TextField
            value={formValues.description}
            onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
              setFormValues({
                ...formValues,
                description: event.target.value,
              });
            }}
            multiline
            rows={10}
            label="Description"
            variant="outlined"
            fullWidth
          />
        </Grid>
        <Grid item xs={6}>
          <Autocomplete
            multiple
            id="tags-outlined"
            value={formValues.tags}
            onChange={(event: React.SyntheticEvent, value: Array<string>) => {
              setFormValues({
                ...formValues,
                tags: value,
              });
            }}
            options={tags}
            getOptionLabel={(tag) => tag}
            filterSelectedOptions
            renderInput={(params) => <TextField {...params} label="Tags" />}
          />
        </Grid>
      </Grid>
      {error !== "" && (
        <Alert
          sx={{ marginBottom: 2 }}
          severity="error"
          onClose={() => {
            setError("");
          }}
        >
          {error}
        </Alert>
      )}
      <Button role="createPageSubmitButton" onClick={handleSubmit} variant="contained">
        Submit
      </Button>
    </Box>
  );
}

// Tags used to classify foods/restaurants
const tags = [
  "Chinese",
  "French",
  "Japanese",
  "Italian",
  "Greek",
  "Spanish",
  "Labanese",
  "Turkey",
  "Thai",
  "Indian",
  "Mexican",
  "American",
  "Food therapy",
  "Family made",
  "Food story",
  "Great restaurant",
  "Good for brunch",
  "Good for lunch",
  "Good for Dinner",
  "Best Ramen Place",
  "Best for date",
  "Best for small groups",
  "Best for large groups",
  "Best for birthday party",
  "Drinks are good",
  "Great music",
  "Clean environment",
  "Fast serving",
  "Great servers",
  "Line is too long",
];
