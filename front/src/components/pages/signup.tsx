import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import { auth } from "../../firebase/firebaseConfig";
import { createUserWithEmailAndPassword } from "@firebase/auth";
import { useNavigate } from "react-router";

/** signup page */
export default function Signup() {
    const navigate = useNavigate();

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // checks whether stored password is the same as inputted password
    const data = new FormData(event.currentTarget);
    if (data.get("password") !== data.get("verify-password")) {
      alert("Passwords do not match");
    } else {
      // creates a new account if the user already does not have one with that email
      if (data.get("email") !== null && data.get("password") !== null) {
        createUserWithEmailAndPassword(
          auth,
          data.get("email") as string,
          data.get("password") as string
        )
          .then((userCredential: any) => {
            // Signed in
            // const user = userCredential.user;
            navigate('/home');
            // ...
          })
          .catch((error: any) => {
            // const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage);
            // ..
          });
      }
    }
  };

  // appearance of signup area, which includes  email/password/verify password boxes
  return (
    <Grid
      container
      spacing={0}
      direction="column"
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: "90vh" }}
    >
      <Grid item xs={3}>
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Avatar sx={{ m: 1 }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}
          >
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="verify-password"
              label="Verify Password"
              type="password"
              id="verify-password"
              autoComplete="current-password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
          </Box>
        </Box>
      </Grid>
    </Grid>
  );
}
